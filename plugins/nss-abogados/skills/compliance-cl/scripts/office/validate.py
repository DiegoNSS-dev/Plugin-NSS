#!/usr/bin/env python3
"""
validate.py — Validador de integridad de archivos Office (.docx / .xlsx).

Uso:
    python scripts/office/validate.py <archivo.docx|archivo.xlsx> [más archivos...]

Qué hace (de forma determinista, sin heurísticas):
    - Confirma que el archivo existe y no está vacío.
    - Confirma que es un ZIP válido (los .docx y .xlsx son contenedores OOXML zip).
    - Verifica que exista [Content_Types].xml y que todo el XML interno parsee sin error.
    - Para .docx: exige word/document.xml.
    - Para .xlsx: exige xl/workbook.xml.
    - Ejecuta la verificación de CRC interna del ZIP (detecta corrupción de bytes).

Salida:
    - Imprime una línea por archivo: OK o FAIL con el motivo.
    - Código de salida 0 si todos válidos; 1 si alguno falla.

No modifica el archivo. Es solo lectura.
"""

import sys
import os
import zipfile
import xml.etree.ElementTree as ET

REQUIRED = {
    ".docx": ["word/document.xml"],
    ".xlsx": ["xl/workbook.xml"],
    ".dotx": ["word/document.xml"],
    ".xltx": ["xl/workbook.xml"],
}


def validate(path: str) -> tuple[bool, str]:
    if not os.path.exists(path):
        return False, "no existe"
    if os.path.getsize(path) == 0:
        return False, "archivo vacío (0 bytes)"

    ext = os.path.splitext(path)[1].lower()
    if ext not in REQUIRED:
        return False, f"extensión no soportada: {ext}"

    if not zipfile.is_zipfile(path):
        return False, "no es un contenedor OOXML válido (zip corrupto o incompleto)"

    try:
        with zipfile.ZipFile(path) as z:
            bad = z.testzip()
            if bad is not None:
                return False, f"CRC inválido en '{bad}' (bytes corruptos)"

            names = set(z.namelist())
            if "[Content_Types].xml" not in names:
                return False, "falta [Content_Types].xml"

            for req in REQUIRED[ext]:
                if req not in names:
                    return False, f"falta la parte obligatoria '{req}'"

            # Parsear todo el XML interno para detectar mal formado.
            for name in names:
                if name.endswith(".xml") or name.endswith(".rels"):
                    try:
                        ET.fromstring(z.read(name))
                    except ET.ParseError as e:
                        return False, f"XML mal formado en '{name}': {e}"
    except zipfile.BadZipFile as e:
        return False, f"zip ilegible: {e}"

    return True, "OK"


def main(argv):
    if len(argv) < 2:
        print("Uso: python validate.py <archivo.docx|.xlsx> [...]", file=sys.stderr)
        return 2
    all_ok = True
    for path in argv[1:]:
        ok, msg = validate(path)
        status = "OK  " if ok else "FAIL"
        print(f"{status} {path}" + ("" if ok else f"  ->  {msg}"))
        all_ok = all_ok and ok
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
