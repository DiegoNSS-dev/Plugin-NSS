# Fase 1-2: Insumos y Extracción de Datos

## Archivos a pedir al usuario

Pedir, idealmente exportados de Nubox en **Excel/CSV** (no PDF, que es difícil de parsear):

| Archivo | Para qué sirve | Imprescindible |
|---|---|---|
| Libro Diario del período (Excel) | Fuente de todos los asientos a traducir | Sí |
| Balance General / de 8 columnas | Validar cuadre y saldos | Sí |
| Plan de cuentas actual (tributario) | Base del mapeo | Sí |
| Plantilla "IFRS - Plantilla Nubox" | Base del plan IFRS destino | Sí |
| Plantilla de carga de comprobantes | Formato exacto de salida | Sí |
| Exportación de compras | RUT de proveedores | Para desglose |
| Exportación de ventas | RUT de clientes | Para desglose |
| Detalle de pagos (con # de pago) | Desglosar pagos centralizados | Para desglose |
| Libro de Remuneraciones Electrónico (LRE) | Sueldos por empleado para vacaciones | Para NIC 19 |
| Nómina de trabajadores (fechas ingreso) | Días devengados de vacaciones | Para NIC 19 |

## Formatos de archivo de Nubox (crítico)

Nubox exporta en dos formatos que se ven como `.xls` pero son distintos:

1. **XLS binario real (BIFF / MS Excel 97)**: empieza con bytes `\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1`. Son los planes de cuenta y la plantilla de carga.
2. **HTML disfrazado de .xls**: contiene `<html>` o `<table>`. Son las exportaciones de compras, ventas, pagos, comprobantes aprobados.

Detectar el tipo antes de leer:
```python
with open(path,'rb') as f: head=f.read(300)
if head[:8]==b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1': tipo="XLS binario"
elif b'<html' in head.lower() or b'<table' in head.lower(): tipo="HTML disfrazado"
elif head[:2]==b'PK': tipo="XLSX"
```

- Para **XLS binario**: convertir con LibreOffice a xlsx para leer con openpyxl:
  `python3 /mnt/skills/public/docx/scripts/office/soffice.py --headless --convert-to xlsx --outdir <dir> <archivo.xls>`
- Para **HTML disfrazado**: parsear con regex sobre el HTML (encoding latin-1):
```python
import re, html
data=open(path,encoding='latin-1',errors='replace').read()
rows=re.findall(r'<tr[^>]*>(.*?)</tr>',data,re.S|re.I)
for r in rows:
    cells=re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>',r,re.S|re.I)
    clean=[html.unescape(re.sub(r'<[^>]+>','',c)).strip() for c in cells]
```
- `xlrd` normalmente NO está disponible (la red bloquea pip). Usar LibreOffice.

## Parsear el Libro Diario en Excel

El libro diario de Nubox en Excel tiene encabezados dispersos y celdas combinadas. Los datos reales suelen empezar varias filas más abajo. Detectar las posiciones reales:

1. Buscar la fila donde aparecen "Fecha", "Cuenta", "Debe", "Haber".
2. Inspeccionar las primeras filas de datos para ver en qué columna cae cada valor (las posiciones del encabezado y de los datos pueden diferir por celdas combinadas).

Estructura típica observada (índices de columna, base 0): Fecha=1, Tipo=2, N°comp=4, Secuencia=6, Cuenta=8 (formato "1101-03 BANCO CLP"), Glosa=12, Debe=21, Haber=27.

Reglas al extraer:
- Arrastrar fecha/tipo/comprobante a las líneas de detalle (solo la primera línea de cada comprobante los trae).
- Excluir filas con "Acumulado", "Total", "www.nubox".
- Convertir 0 a None para debe/haber vacíos.
- Separar código de cuenta (ej. "1101-03") de su descripción.

**NO parsear el libro diario desde PDF**: los montos de debe/haber se solapan en posición X y el resultado descuadra. Siempre pedir el Excel.

## Validación de cuadre (obligatoria)

Después de extraer, verificar SIEMPRE:
```python
D=sum(a['debe'] or 0 for a in movimientos)
H=sum(a['haber'] or 0 for a in movimientos)
assert abs(D-H)<1, f"Descuadre: {D-H}"
```
Y cuadrar contra el balance tributario: el total debe coincidir con las sumas del balance de 8 columnas. Si no cuadra, revisar la extracción antes de seguir.

## Entender el balance de 8 columnas chileno

Columnas: Débitos | Créditos | Deudor | Acreedor | Activo | Pasivo | Pérdidas | Ganancias.

- El **Inventario Activo** incluye los resultados acumulados (pérdida) como saldo deudor.
- Cuadre del balance: `Inventario Activo + Pérdida del ejercicio = Inventario Pasivo`.
- **Cuentas transitorias de remuneración** (sueldos/honorarios/retención por pagar) a veces se presentan netas porque rotan dentro del ejercicio y están saldadas al cierre. No confundir su saldo con deuda real. Verificar rastreando sus movimientos mes a mes.

## Calcular vacaciones desde el LRE

El LRE (Libro de Remuneraciones Electrónico, CSV de la Dirección del Trabajo) tiene columnas codificadas. Columnas clave observadas: Sueldo base (col 40), Gratificación (col 45), Total haberes imponibles (col 133). La remuneración imponible (sueldo + gratificación) es la base para valorizar el día de vacaciones. Ver `references/03-ajustes-ifrs.md` para el cálculo.
