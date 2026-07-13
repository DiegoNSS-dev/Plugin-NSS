# Fase 8: Informe de Estados Financieros IFRS

## Cuándo y qué generar

El usuario suele querer dos cosas distintas, no confundirlas:
- **Modelo de trabajo (Excel)**: conciliación Tributario → Ajuste → IFRS, con todas las hojas de cálculo. Es la herramienta interna.
- **Informe formal (Word/PDF)**: estados financieros presentables, normalmente **solo columna IFRS** (sin lo tributario, que es información interna). Es lo que se entrega/comparte.

Preguntar cuál necesita. Para el informe formal en Word, leer primero `/mnt/skills/public/docx/SKILL.md`.

## Estructura del informe formal (solo IFRS)

1. **Portada**: razón social, RUT, representante legal, período, "Estados Financieros bajo IFRS", moneda (CLP$).
2. **Nota 1 — Bases de preparación**: que la contabilidad es tributaria y se ajusta a IFRS; tratamiento de transición (NIIF 1); nota sobre cuentas transitorias de remuneración si aplica.
3. **Estado de Situación Financiera**: activos corrientes/no corrientes, pasivos corrientes/no corrientes, patrimonio. Cifras negativas entre paréntesis.
4. **Estado de Resultados**: por función, con subtotales de margen bruto y resultado operacional. Incluir línea de impuesto corriente (aunque sea $0) y de impuesto diferido.
5. **Notas explicativas**:
   - 4.1 Normas aplicadas (NIC 16, 12, 19, 21, NIIF 16)
   - PPE y depreciación
   - Provisión de vacaciones (con tabla por empleado)
   - Impuesto a la renta e impuestos diferidos (régimen, tasa, por qué no se reconoce activo por pérdidas)
   - Diferencias de cambio
   - NIIF 16 (pendiente si no hay datos)
   - Situación financiera (comentario de gestión)
6. Firmas (Contador / Representante Legal).

## Presentación visual

Si el usuario pide una identidad visual (ej. colores de su empresa o estudio), respetarla. Patrón que funcionó: paleta de un color principal para títulos + un tono de acento para encabezados de tabla y totales + negro para texto, fuente sans-serif (Calibri/Arial). Tablas con encabezado en color, totales destacados, filas con bordes suaves.

Generar en Word con docx-js (Node, la librería `docx` suele estar disponible) y convertir a PDF con LibreOffice. Validar el .docx con `/mnt/skills/public/docx/scripts/office/validate.py` y revisar visualmente rasterizando el PDF.

## Verificación cruzada final (lo más importante)

El informe y la contabilidad cargada deben coincidir **al peso**. Verificar con código que:
```
Suma de saldos (asientos reales traducidos + ajustes IFRS) por rubro
   == ESF/ER del informe
```
Calcular desde los movimientos:
- Activos = saldo deudor de cuentas de activo (grupo 1) + ajustes de activo.
- Pasivos = saldo acreedor de cuentas de pasivo (grupo 2 excepto patrimonio) + ajustes de pasivo.
- Patrimonio = cuentas de patrimonio + resultado del ejercicio.
- Resultado = ingresos − gastos (atención: en el plan IFRS de Nubox 4=gastos, 5=ingresos; verificar la convención del plan específico).

Mostrar al usuario la comparación rubro por rubro con diferencia. Debe ser cero. Si hay diferencia, lo más común es que falte cargar el **asiento de apertura** (su monto suele ser exactamente el ajuste de transición de años anteriores).

## Recursos de salud financiera / wellbeing

Si los estados muestran pérdidas recurrentes o estructura de costos pesada, se puede incluir un comentario de gestión objetivo (ej. peso de arriendos sobre ventas), pero sin alarmismo ni recomendaciones de inversión específicas (no es asesoría financiera). Mantener tono profesional y factual.
