---
name: subarriendo-tributario-nss
description: "Rellena y genera el Contrato de Subarrendamiento para Fines Tributarios ante el SII (oficina virtual / domiciliación tributaria y comercial) de NSS Abogados SpA. Usa esta skill SIEMPRE que el usuario quiera generar, armar, completar o emitir este contrato de oficina virtual / domicilio tributario para uno o varios clientes (subarrendatarios), sea persona natural o jurídica, aunque no diga el nombre exacto del contrato. Dispara también ante frases como 'contrato de oficina virtual', 'domiciliación tributaria', 'subarriendo para el SII', 'domicilio comercial para un cliente', 'contrato de dirección tributaria', o cuando entreguen una lista/planilla de clientes para emitir estos contratos en lote. NSS es siempre el subarrendador; el subarrendatario es el cliente y sus datos cambian en cada caso."
---

# Contrato de subarrendamiento tributario (oficina virtual) — NSS

Genera el contrato por el que **NSS Abogados SpA subarrienda** a un cliente una
dirección para domiciliación tributaria y comercial ante el SII (oficina
virtual). NSS es **siempre** el subarrendador; el cliente es el subarrendatario.

El trabajo consiste en recolectar los datos variables del caso, rellenar la
plantilla correcta (persona natural o jurídica) y entregar el `.docx` con el
formato NSS intacto. Las plantillas ya traen el logo, el header, los márgenes y
la tipografía canónica de NSS: **no regeneres el documento desde cero** ni
reescribas su redacción; solo rellenas tokens sobre el template real.

## Qué es fijo y qué es variable

**Fijo (no lo toques — ya está en la plantilla):** subarrendador (NSS Abogados
SpA, RUT 77.682.183-7, rep. Clemente Hernández Gemignani, RUT 18.397.099-2),
individualización de la propiedad (Cerro El Plomo 5855, of. 1407, Las Condes,
Rol 839-430), titulares del dominio, datos bancarios (Santander cta. 89789478,
pagos@nss.cl), giro 681012 exento de IVA, correos de notificación
(esaez@nss.cl, chernandez@nss.cl) y toda la redacción de las cláusulas 1ª a 11ª.

**Variable por caso:** fecha, datos del subarrendatario y canon. Nada más.

## Datos que debes recolectar por cada caso

| Campo | Persona jurídica | Persona natural |
|-------|------------------|-----------------|
| `tipo` | `juridica` | `natural` |
| Razón social / Nombre | razón social | nombre completo |
| RUT (empresa o persona) | ✔ | ✔ |
| Representante | ✔ | — |
| RUT representante | ✔ | — |
| Correo electrónico | ✔ | ✔ |
| Canon | ✔ (**pregúntalo siempre**) | ✔ (**pregúntalo siempre**) |
| Fecha | opcional | opcional |

La **firma del cliente se deriva sola**: en jurídica firma el representante "pp."
la razón social; en natural firma la persona por sí misma (sin línea "pp.").

## Reglas clave

1. **El canon se pregunta SIEMPRE.** Nunca asumas un monto ni lo copies de un
   contrato anterior. Pregunta el valor y en qué unidad (UF o pesos) va. Al
   pasarlo al script, entrégalo ya redactado tal como debe imprimirse. Convención
   chilena para montos en pesos: cifra + monto en palabras, p. ej.
   `$1.200.000 (un millón doscientos mil pesos)`. En UF: `UF 30 (treinta Unidades de Fomento)`.
   Recuerda que la cláusula CUARTA dice "anuales" y que el pago corre **a contar
   del segundo año** (el primer año va sin cobro) — no alteres eso salvo instrucción expresa.

2. **Persona natural vs jurídica.** Si el cliente es persona natural, usa
   `tipo: natural`: la plantilla ya elimina las filas de representante y la línea
   "pp.". Si es empresa, usa `tipo: juridica`. Si no está claro, pregúntalo.

3. **Fecha.** Si el usuario no la indica, el script usa la fecha de generación en
   formato chileno ("9 de julio de 2026"). Si prefieren dejarla en blanco para
   completar al firmar, pásala como `fecha` con un guion largo o "______".

4. **De a uno o en lote.** Un caso o muchos usan el mismo script. Para lote,
   arma un JSON (lista de casos) o lee un CSV/planilla que aporte el usuario.

## Flujo

1. Identifica si es **uno** o **varios** casos y si cada cliente es **natural o jurídica**.
2. Reúne los campos de la tabla de arriba. **Pregunta el canon** (monto + unidad).
   Si falta cualquier campo requerido, pídelo antes de generar.
3. Ejecuta el script (una llamada sirve para uno o para todos):

   ```bash
   # De a uno (por flags)
   python scripts/generar_contrato.py --tipo juridica \
     --razon-social "Comercial Andes SpA" --rut "76.111.222-3" \
     --representante "Juana Pérez Soto" --rut-rep "15.555.666-7" \
     --correo "juana@andes.cl" \
     --canon '$1.200.000 (un millón doscientos mil pesos)' \
     --out /mnt/user-data/outputs

   # En lote (JSON con lista de casos)
   python scripts/generar_contrato.py --json casos.json --out /mnt/user-data/outputs

   # En lote (CSV/planilla con encabezados: tipo,razon_social,nombre,rut,representante,rut_rep,correo,canon,fecha)
   python scripts/generar_contrato.py --csv casos.csv --out /mnt/user-data/outputs
   ```

   Formato del JSON de lote:
   ```json
   [
     {"tipo":"juridica","razon_social":"Comercial Andes SpA","rut":"76.111.222-3",
      "representante":"Juana Pérez Soto","rut_rep":"15.555.666-7",
      "correo":"juana@andes.cl","canon":"$1.200.000 (un millón doscientos mil pesos)"},
     {"tipo":"natural","nombre":"Pedro Rojas Díaz","rut":"12.345.678-9",
      "correo":"pedro@correo.cl","canon":"UF 30 (treinta Unidades de Fomento)"}
   ]
   ```

4. **Verifica antes de entregar.** Convierte a PDF y revisa que los datos
   quedaron bien y el formato NSS intacto:
   ```bash
   python /mnt/skills/public/docx/scripts/office/soffice.py --headless --convert-to pdf <archivo>.docx
   pdftoppm -jpeg -r 100 <archivo>.pdf page && ls page-*.jpg
   ```
   Lee las imágenes y confirma: tabla del subarrendatario correcta (jurídica con
   representante / natural sin él), canon, fecha, y bloque de firma coherente
   (jurídica con "pp." / natural sin él).

5. Entrega el/los `.docx` con `present_files`. El nombre sigue la convención NSS
   `YYYYMMDD_contrato_oficina-virtual_<cliente>.docx` (ya lo aplica el script).

## Nomenclatura de archivos

El script nombra automáticamente como `YYYYMMDD_contrato_oficina-virtual_<slug-del-cliente>.docx`
(fecha de generación + razón social o nombre normalizado), coherente con el
estándar de nombres de NSS.

## Advertencias legales a tener presentes (no las metas en el .docx)

- El contrato factura **exento de IVA** por el giro 681012 sin servicio
  complementario; si el usuario pide agregar servicios (recepción de
  correspondencia, atención, etc.), advierte que eso puede desnaturalizar la
  exención y cambiar el tratamiento tributario antes de modificar la redacción.
- No inventes ni "ajustes" las cláusulas fijas. Si piden cambios de fondo a la
  redacción, hazlos explícitos y sepáralos de este rellenado estándar.

## Assets

- `assets/plantilla_juridica.docx` — template tokenizado, subarrendatario empresa.
- `assets/plantilla_natural.docx` — template tokenizado, subarrendatario persona natural.
- `scripts/generar_contrato.py` — rellena uno o varios casos.

Ambas plantillas se derivaron del documento original de NSS, por lo que
conservan el formato exacto. Si NSS actualiza la redacción del contrato,
reemplaza estos assets regenerándolos desde el nuevo `.docx` original (los
tokens usados son: FECHA, SUB_RAZON_SOCIAL/SUB_NOMBRE, SUB_RUT, SUB_REPRESENTANTE,
SUB_RUT_REP, SUB_CORREO, CANON, FIRMA_NOMBRE, FIRMA_RUT, FIRMA_PP).
