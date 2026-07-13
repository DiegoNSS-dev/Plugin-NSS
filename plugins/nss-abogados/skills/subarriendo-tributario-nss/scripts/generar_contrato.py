#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rellena el Contrato de Subarrendamiento para Fines Tributarios (Oficina
Virtual) de NSS Abogados SpA, para uno o varios casos, preservando el formato
y el logo del template original.

Uso tipico:
    python generar_contrato.py --json casos.json --out /mnt/user-data/outputs
    python generar_contrato.py --csv casos.csv  --out /mnt/user-data/outputs
    python generar_contrato.py --tipo juridica --razon-social "..." --rut "..." \
        --representante "..." --rut-rep "..." --correo "..." --canon "..." \
        --out /mnt/user-data/outputs

Cada "caso" es un diccionario con:
    tipo            : "juridica" | "natural"   (requerido)
    fecha           : texto de la fecha (opcional; ver DEFAULT_FECHA)
    canon           : texto EXACTO a imprimir del canon (requerido)
    correo          : correo del subarrendatario (requerido)
    rut             : RUT del subarrendatario (empresa o persona) (requerido)
  Solo juridica:
    razon_social    : razon social (requerido)
    representante   : nombre del representante (requerido)
    rut_rep         : RUT del representante (requerido)
  Solo natural:
    nombre          : nombre de la persona natural (requerido)

La firma se deriva automaticamente:
    juridica -> nombre=representante, rut=rut_rep, pp.=razon_social
    natural  -> nombre=nombre,        rut=rut
"""
import argparse, csv, json, os, re, shutil, subprocess, sys, datetime
from xml.sax.saxutils import escape

MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
         "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

def hoy_largo():
    d = datetime.date.today()
    return "%d de %s de %d" % (d.day, MESES[d.month - 1], d.year)

# Si un caso no trae 'fecha', se usa esta (fecha de generacion, formato chileno).
DEFAULT_FECHA = hoy_largo()

ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")

def slug(s):
    s = (s or "sin-nombre").lower().strip()
    s = (s.replace("á", "a").replace("é", "e").replace("í", "i")
           .replace("ó", "o").replace("ú", "u").replace("ñ", "n"))
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "sin-nombre"

def build_tokens(case):
    tipo = (case.get("tipo") or "").strip().lower()
    if tipo not in ("juridica", "natural"):
        raise ValueError("tipo debe ser 'juridica' o 'natural' (caso: %r)" % case)
    fecha = case.get("fecha") or DEFAULT_FECHA
    canon = case.get("canon")
    if not canon:
        raise ValueError("Falta 'canon' en el caso: %r" % case)
    correo = case.get("correo", "")
    rut = case.get("rut", "")
    common = {"FECHA": fecha, "CANON": canon, "SUB_CORREO": correo, "SUB_RUT": rut}
    if tipo == "juridica":
        req = ["razon_social", "representante", "rut_rep", "rut", "correo"]
        miss = [k for k in req if not case.get(k)]
        if miss:
            raise ValueError("Faltan campos %s en caso juridico: %r" % (miss, case))
        common.update({
            "SUB_RAZON_SOCIAL": case["razon_social"],
            "SUB_REPRESENTANTE": case["representante"],
            "SUB_RUT_REP": case["rut_rep"],
            "FIRMA_NOMBRE": case["representante"],
            "FIRMA_RUT": case["rut_rep"],
            "FIRMA_PP": case["razon_social"],
        })
        etiqueta = case["razon_social"]
    else:
        req = ["nombre", "rut", "correo"]
        miss = [k for k in req if not case.get(k)]
        if miss:
            raise ValueError("Faltan campos %s en caso natural: %r" % (miss, case))
        common.update({
            "SUB_NOMBRE": case["nombre"],
            "FIRMA_NOMBRE": case["nombre"],
            "FIRMA_RUT": case["rut"],
        })
        etiqueta = case["nombre"]
    return tipo, common, etiqueta

def generar(case, outdir):
    tipo, tokens, etiqueta = build_tokens(case)
    tmpl = os.path.join(ASSETS, "plantilla_%s.docx" % tipo)
    if not os.path.exists(tmpl):
        raise FileNotFoundError("No existe la plantilla: %s" % tmpl)

    work = "/tmp/_gen_%s" % slug(etiqueta)
    shutil.rmtree(work, ignore_errors=True)
    os.makedirs(work)
    subprocess.run(["unzip", "-q", tmpl, "-d", work], check=True)
    doc = os.path.join(work, "word/document.xml")
    xml = open(doc, encoding="utf-8").read()

    for key, val in tokens.items():
        xml = xml.replace("{{%s}}" % key, escape(str(val)))
    # aviso si quedan tokens sin reemplazar
    leftover = re.findall(r"\{\{[A-Z_]+\}\}", xml)
    if leftover:
        raise ValueError("Tokens sin reemplazar %s en caso %r" % (set(leftover), etiqueta))
    open(doc, "w", encoding="utf-8").write(xml)

    os.makedirs(outdir, exist_ok=True)
    ymd = datetime.date.today().strftime("%Y%m%d")
    fname = "%s_contrato_oficina-virtual_%s.docx" % (ymd, slug(etiqueta))
    out = os.path.join(outdir, fname)
    if os.path.exists(out):
        os.remove(out)
    subprocess.run("cd %s && zip -Xrq %s ." % (work, os.path.abspath(out)),
                   shell=True, check=True)
    shutil.rmtree(work, ignore_errors=True)
    return out

def load_cases(args):
    if args.json:
        data = json.load(open(args.json, encoding="utf-8"))
        return data if isinstance(data, list) else [data]
    if args.csv:
        with open(args.csv, encoding="utf-8-sig", newline="") as f:
            return [dict(row) for row in csv.DictReader(f)]
    # caso unico via flags
    case = {k: v for k, v in {
        "tipo": args.tipo, "fecha": args.fecha, "canon": args.canon,
        "correo": args.correo, "rut": args.rut, "razon_social": args.razon_social,
        "representante": args.representante, "rut_rep": args.rut_rep,
        "nombre": args.nombre,
    }.items() if v}
    if not case.get("tipo"):
        sys.exit("Debe indicar --json, --csv o al menos --tipo y los campos del caso.")
    return [case]

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--json"); p.add_argument("--csv")
    p.add_argument("--out", default="/mnt/user-data/outputs")
    p.add_argument("--tipo"); p.add_argument("--fecha"); p.add_argument("--canon")
    p.add_argument("--correo"); p.add_argument("--rut")
    p.add_argument("--razon-social", dest="razon_social")
    p.add_argument("--representante"); p.add_argument("--rut-rep", dest="rut_rep")
    p.add_argument("--nombre")
    args = p.parse_args()

    cases = load_cases(args)
    hechos = []
    for i, c in enumerate(cases, 1):
        out = generar(c, args.out)
        hechos.append(out)
        print("[%d/%d] %s" % (i, len(cases), out))
    print("\nListo: %d contrato(s) generado(s)." % len(hechos))
    for h in hechos:
        print("  -", h)

if __name__ == "__main__":
    main()
