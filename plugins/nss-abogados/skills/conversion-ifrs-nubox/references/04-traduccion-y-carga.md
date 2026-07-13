# Fases 5-7: Traducción, Auxiliares y Archivos de Carga

## Formato de la plantilla de carga de comprobantes de Nubox

17 columnas (en este orden exacto):

1. **Número** — 0 en la primera línea de cada comprobante, vacío en las demás
2. **Tipo** — I (ingreso), E (egreso), T (traspaso). Solo en la primera línea
3. **Fecha** — datetime real (no texto). Solo en la primera línea
4. **Glosa** — glosa del comprobante. Solo en la primera línea
5. **Cuenta Detalle** — código de cuenta IFRS (todas las líneas)
6. **Glosa Detalle** — se repite en cada línea
7. **Centro Costo** — opcional
8. **Sucursal** — opcional
9. **Debe** — entero
10. **Haber** — entero
11. **Tipo Auxiliar** — A (auxiliar cliente/proveedor), B (bancario), H (honorarios)
12. **RUT** — A: RUT cliente/proveedor; H: RUT prestador
13. **Razón Social / Desc. Bancaria / Nombre Prestador** — según tipo
14. **Tipo de Documento** — código SII (A) o tipo boleta honorario (H)
15. **Folio / N° Documento / Folio Boleta**
16. **Monto** — del auxiliar
17. **Fecha Vencimiento/Emisión** — formato DD/MM/AAAA

Reglas:
- Un comprobante por cada asiento original del libro (salvo desgloses).
- Cabecera (cols 1-4) solo en la primera línea de cada comprobante.
- Fecha como datetime, montos como enteros.

## EL ARCHIVO DEBE SER .XLS BINARIO (no .xlsx)

Nubox rechaza .xlsx con "archivo inválido". Generar con openpyxl en .xlsx y convertir:
```
python3 /mnt/skills/public/docx/scripts/office/soffice.py --headless --convert-to "xls:MS Excel 97" --outdir <dir> archivo.xlsx
```
Verificar que el resultado empieza con `\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1`. Comparar siempre contra un ejemplo de carga que el usuario sepa que funciona.

## Traducción de asientos

Para cada movimiento: buscar su cuenta en la tabla de mapeo y reemplazar por la cuenta IFRS. Excluir los comprobantes de corrección monetaria pura. Validar:
- Todas las cuentas tienen mapeo (ninguna sin traducir).
- Cada comprobante cuadra (debe=haber) tras traducir.
- El total cuadra.

## Datos auxiliares (la parte más delicada)

Las cuentas con atributo exigen datos extra o Nubox da error ("campos requeridos", "RUT formato inválido", "descripción código bancario"):

- **Bancarias (tipo B)**: descripción del movimiento (col 13), monto (col 16), fecha (col 17).
- **Auxiliar clientes/proveedores (tipo A)**: RUT (col 12), razón social (col 13), tipo documento (col 14, ej. 33 factura), folio (col 15), monto (col 16), fecha (col 17).
- **Honorarios (tipo H)**: RUT prestador, nombre, tipo boleta, folio, monto, fecha.

### El problema de las líneas centralizadas

El libro diario agrupa movimientos: "centralización compras", "movimientos auxiliares", "centralización pagos #41;50;44...". Estas líneas representan **muchos documentos/proveedores a la vez**, así que no tienen un RUT único.

Estrategia (confirmar con usuario): **RUT real donde se puede, genérico donde no**:
- Identificar RUT real por palabras clave en la glosa (ej. "pago nss" → buscar NSS en la exportación de compras).
- **Pagos centralizados**: si la glosa lista los # de pago, cruzar con el archivo de pagos (que tiene # PAGO → RUT → proveedor → monto). Este cruce es **exacto** y permite desglosar cada pago en su proveedor real, abriendo la línea en varias (una por proveedor). Verificar que la suma de los pagos cuadre con el monto de la línea original.
- **Compras centralizadas**: el cruce con la exportación de compras es **aproximado** (el libro registra valores con IVA en subcuentas distintas a la exportación). Si no calza con precisión, dejar genérico en vez de adivinar.
- **Genéricos aceptados**: 55.555.555-5 (proveedores varios), 66.666.666-6 (clientes/boletas genérico).
- **Honorarios individuales**: usar el RUT real de la boleta (pedir al usuario el informe de boletas de honorarios recibidas, que trae RUT, folio, montos).

### Alternativa: quitar atributos en el set IFRS

Si el usuario solo necesita reportería (balance y EEFF) y no el detalle auxiliar, se puede quitar el atributo (bancario/auxiliar/honorarios) a esas cuentas en el set IFRS. El detalle por proveedor ya vive en el set tributario. Es lo más simple y los estados financieros quedan idénticos. Ofrecer esta opción.

## Dos archivos separados

Generar (según preferencia del usuario):
1. **Asientos reales traducidos** — los comprobantes del libro, mapeados, con auxiliares.
2. **Ajustes IFRS** — los asientos de ajuste calculados en la fase 4 (apertura, depreciación, vacaciones, impuestos diferidos).

## Código SII de tipos de documento

Para boletas de honorarios, el código 48 es **incorrecto** (es vale vista). El código correcto debe verificarse en la fuente oficial del SII: https://www1.sii.cl/TMP/InfoP001/IECVCodigosDocs.pdf (códigos como 70/71 para boletas de honorarios/prestación de servicios de terceros). Verificar qué código acepta la importación de Nubox antes de generar. Factura electrónica = 33.

## Orden de carga en Nubox

1. Crear las cuentas faltantes en el plan (especialmente las de ajuste como 1212-03).
2. Cargar primero los **asientos reales** (prueba grande del formato y mapeo).
3. Cargar después los **ajustes** (incluido el de apertura).
4. Si un comprobante carga incompleto, es porque una cuenta no existía: crearla y recargar ese comprobante.
