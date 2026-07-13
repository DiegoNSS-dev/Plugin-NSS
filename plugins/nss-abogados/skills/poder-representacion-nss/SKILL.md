---
name: poder-representacion-nss
description: "Redacta y genera en Word (.docx) poderes especiales de representación de NSS para actuar ante el SII, la Tesorería General de la República (TGR) y Municipalidades, distinguiendo si el mandante es persona natural (PN) o persona jurídica (PJ). Usa esta skill SIEMPRE que el usuario pida crear, redactar, armar, completar o emitir un poder, mandato de representación, poder tributario, poder ante el SII, poder ante Tesorería, poder para inicio de actividades, timbraje, término de giro o convenios TGR, sea para un cliente o en lote, y aunque no diga 'persona jurídica', 'persona natural' ni '.docx'. La skill decide sola la estructura PN vs PJ según los datos del mandante y aplica el formato canónico NSS. Dispara también ante 'poder simple', 'mandato para el SII', 'poder de representación tributaria' o cuando entreguen una planilla de mandantes para emitir estos poderes."
---

# Poder de representación NSS (SII / TGR / Municipalidades)

Genera el poder especial de representación con que NSS actúa por cuenta de sus clientes ante el SII, la TGR y Municipalidades. El entregable es un `.docx` que debe verse como si saliera de la firma. La única variable estructural relevante es **quién otorga el poder**: una persona natural (PN) o una persona jurídica (PJ). Todo lo demás (facultades, formato, nómina de mandatarios NSS) se mantiene estable.

## Base legal (para redactar con criterio, no para citar en el cuerpo)

El poder NO se cita en su propio texto, pero conviene tener presente el marco al redactar:

- **Art. 9 Código Tributario**: quien actúe por cuenta de un contribuyente debe acreditar su representación, y el mandato "no tendrá otra formalidad que la de constar por escrito". Por eso este poder es un **poder simple/privado**, no notarial: basta que conste por escrito para actuar ante el SII. El Servicio puede aceptar la representación sin acompañar el título, pero puede exigir ratificación o prueba del vínculo dentro de **10 días** bajo apercibimiento de tener por no presentada la actuación. La extinción del mandato se comunica conforme al Art. 68.
- **Arts. 2116 y ss. Código Civil**: régimen general del mandato.
- **PJ**: cuando el mandante es una sociedad, el poder lo otorga su representante legal, a quien se identifica junto con la sociedad. **No se embebe la personería en el cuerpo del poder**: por el mismo Art. 9, el Servicio acepta la representación sin acompañar el título y puede exigir su prueba después, de modo que la personería se acredita por separado solo si la piden.

No incluyas artículos ni "[VERIFICAR CITA]" en el cuerpo del poder: es un documento operativo, no un informe.

## Datos que necesitas antes de redactar

Pide (o extrae de lo entregado) los datos del **mandante**. Con eso decides PN o PJ:

**Persona natural (PN)** — el mandante es un individuo:
- Nombre completo
- Cédula de identidad (o cédula para extranjeros → rotular `C.I.E.`)
- Domicilio

**Persona jurídica (PJ)** — el mandante es una sociedad/empresa:
- Razón social y tipo social (SpA, Ltda., S.A., EIRL, etc.)
- RUT de la sociedad
- Domicilio social
- Representante(s) legal(es) que firma(n): nombre, cédula

No se incluye personería en el cuerpo del poder: la representación se acredita por separado ante el Servicio si este la exige. No agregues referencia a escrituras, notarías ni fechas de personería.

Si falta un dato variable, márcalo `[COMPLETAR]` en el documento en vez de suponerlo. Nunca inventes RUT, cédulas ni fechas.

## Mandatarios NSS (parte fija)

Los mandatarios son los abogados de NSS, que actúan **indistintamente** ("uno cualquiera de"), todos domiciliados en Cerro El Plomo 5855, Of. 1407, Las Condes, Región Metropolitana. La nómina vigente está en `references/mandatarios-nss.md`. **Léela y confirma con el usuario que sigue vigente** antes de emitir (los nombres/cédulas de la firma cambian con el tiempo). No agregues ni quites mandatarios sin instrucción.

## Flujo de trabajo

1. Determina PN o PJ a partir de los datos del mandante.
2. Lee la plantilla correspondiente:
   - PN → `references/plantilla-pn.md`
   - PJ → `references/plantilla-pj.md`
   - Ambas comparten el cuerpo de facultades (SII, firma/suscripción, TGR/Municipalidades y cláusula de amplitud); solo cambian el encabezado de identificación y el bloque de firma.
3. Lee `references/mandatarios-nss.md` e inserta la nómina vigente.
4. Aplica el **formato canónico NSS** (ver abajo) y genera el `.docx` con docx-js.
5. Revisa el checklist y entrega con `present_files`.

Si te entregan una **planilla/lista de mandantes** (emisión en lote), repite el flujo por cada uno, generando un archivo por mandante con su propio nombre de archivo.

## Formato (estándar NSS)

Este poder se rige por el estándar `estandar-docx-nss`. En síntesis, y sin excepciones:

| Parámetro | Valor |
|-----------|-------|
| Motor | docx-js (Node). Instalar local: `npm init -y && npm install docx` |
| Página | Carta / US Letter (12240 × 15840 DXA) |
| Márgenes | 1 pulgada (1440 DXA) los 4 lados |
| Fuente | Arial 11pt (`size: 22`) en todo el documento, color negro |
| Interlineado | 1.5 (`spacing: { line: 360 }`) |
| Cuerpo | Justificado (`AlignmentType.JUSTIFIED`) |
| Título y firma | Centrados |
| Header | Logo NSS (`assets/nss-logo.png`, 1000×259, ratio ≈ 3.86; render `width: 110, height: 28`) + línea "Cerro El Plomo 5855, of.1407 — Las Condes, RM, Chile" |
| Footer | Número de página, centrado |

Si `assets/nss-logo.png` faltara, usa el de la skill `estandar-docx-nss` o pídelo al usuario; no inventes dimensiones. Para el andamiaje docx-js puedes apoyarte en `references/plantilla-docx-js.md` de la skill `estandar-docx-nss`.

**Dos trampas de docx-js (verificadas):**
- Fija el tamaño de página explícito, o docx-js sale en A4: `page: { size: { width: 12240, height: 15840 }, margin: { top:1440, right:1440, bottom:1440, left:1440 } }`.
- `ImageRun` requiere `type` en las versiones actuales: `new ImageRun({ data: logo, type: "png", transformation: { width: 110, height: 28 } })`.

## Convención de nombre de archivo

`YYYYMMDD_poder-sii-tgr_[apellido-o-razonsocial].docx` (siempre `YYYYMMDD` para ordenar cronológicamente).

Ejemplos:
- `20260624_poder-sii-tgr_eisenmann.docx`
- `20260624_poder-sii-tgr_inversiones-xy-spa.docx`

## Checklist antes de entregar

1. ¿PN o PJ correctamente identificado y con el encabezado/firma que corresponde?
2. En PJ: ¿sin cláusula de personería (nada de escrituras, notarías ni fechas)?
3. ¿Nómina de mandatarios NSS confirmada como vigente?
4. ¿Campos variables completos o marcados `[COMPLETAR]`? Cero datos inventados.
5. ¿Formato NSS (Arial 11 negro, 1.5, justificado, carta, márgenes 1", logo con ratio correcto)?
6. ¿El cuerpo del poder está libre de citas legales y de "[VERIFICAR CITA]"?
7. ¿Nombre de archivo en formato `YYYYMMDD_poder-sii-tgr_...`?
