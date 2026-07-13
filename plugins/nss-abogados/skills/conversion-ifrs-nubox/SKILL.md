---
name: conversion-ifrs-nubox
description: Convierte la contabilidad tributaria chilena (exportada de Nubox u otro software SII) de una PyME a un set paralelo bajo IFRS, listo para cargar de vuelta en Nubox. Cubre extraer libros diarios y balances, adaptar el plan de cuentas IFRS, mapear cuenta-por-cuenta tributario a IFRS, calcular ajustes (depreciacion NIC 16, vacaciones NIC 19, impuestos diferidos NIC 12, reverso de correccion monetaria, NIIF 16), traducir asientos, completar auxiliares (RUT), generar archivos de carga .xls y producir estados financieros (ESF, ER y notas). Usa este skill siempre que el usuario quiera pasar contabilidad chilena a IFRS, convertir saldos de Nubox a normas internacionales, armar estados financieros IFRS de una empresa chilena, calcular ajustes IFRS sobre base tributaria, trabajar con regimen ProPyme 14D, o cargar comprobantes IFRS en Nubox, aunque no nombre IFRS explicitamente pero describa tener contabilidad tributaria y necesitar reporteria internacional.
---

# Conversión de Contabilidad Tributaria Chilena a IFRS (Nubox)

## Qué hace este skill

Transforma la contabilidad tributaria de una PyME chilena (la que vive en Nubox, sobre base SII) en un **set paralelo bajo IFRS**. El resultado es doble:
1. Archivos de **carga masiva** (.xls) para subir los asientos IFRS de vuelta a un set paralelo en Nubox.
2. Un **informe de estados financieros IFRS** (Estado de Situación Financiera, Estado de Resultados y notas explicativas).

La filosofía central: la contabilidad tributaria es el **punto de partida**; sobre ella se aplican ajustes de norma para llegar a IFRS. Se mantiene la trazabilidad Tributario → Ajuste → IFRS en todo momento.

## Principios que no se negocian

- **Todo debe cuadrar**: cada comprobante (debe=haber) y el balance completo (Activo = Pasivo + Patrimonio). Validar numéricamente en cada paso, nunca afirmar que cuadra sin comprobarlo con código.
- **No inventar datos**: si un RUT o un documento no se puede identificar con certeza (ej. líneas centralizadas), usar genéricos aceptados (55.555.555-5 proveedores varios, 66.666.666-6 boletas) en vez de adivinar un proveedor real.
- **No es asesoría tributaria/legal definitiva**: los criterios (vida útil, tasa, reconocimiento de activos por pérdidas) se proponen y se marcan para validación con el contador.
- **El usuario decide los criterios contables**; el skill ejecuta y verifica. Preguntar ante bifurcaciones reales (régimen tributario, arriendos como costo o gasto, nivel de desglose de proveedores).

## Flujo general (8 fases)

```
1. Recopilar insumos          → libros diarios, balance, plan de cuentas, ventas, compras, pagos, remuneraciones
2. Validar y extraer datos    → parsear a estructura limpia, cuadrar contra el balance tributario
3. Plan de cuentas IFRS       → adaptar la plantilla IFRS de Nubox + mapeo cuenta-por-cuenta
4. Calcular ajustes IFRS      → NIC 16, NIC 19, NIC 12, reverso CM, NIIF 16
5. Traducir asientos          → remapear cada movimiento al plan IFRS; excluir CM
6. Completar auxiliares       → RUT/razón social/documento donde aplique
7. Generar archivos de carga  → formato .xls (BIFF), un comprobante por asiento + asientos de ajuste
8. Informe y verificación     → ESF + ER + notas; verificar que la carga = el informe al peso
```

Cada fase está detallada en los archivos de `references/`. **Leer la referencia correspondiente antes de ejecutar cada fase.**

## Cuándo leer cada referencia

- `references/01-insumos-y-extraccion.md` — qué archivos pedir, formatos de Nubox (.xls binario vs HTML disfrazado), cómo parsear libros diarios y balances, cómo cuadrar. **Leer al empezar.**
- `references/02-plan-cuentas-y-mapeo.md` — cómo adaptar la plantilla IFRS de Nubox, qué cuentas nuevas crear, tabla de mapeo tributario→IFRS. **Leer en fase 3.**
- `references/03-ajustes-ifrs.md` — cálculo de cada ajuste (depreciación, vacaciones, impuesto diferido, corrección monetaria, NIIF 16) con fórmulas. **Leer en fase 4.**
- `references/04-traduccion-y-carga.md` — formato exacto de la plantilla de carga de Nubox, manejo de auxiliares, conversión a .xls, errores comunes y cómo resolverlos. **Leer en fases 5-7.**
- `references/05-informe-financiero.md` — estructura del informe de EEFF, cómo construir ESF/ER, notas explicativas. **Leer en fase 8.**

## Preguntas que SIEMPRE hay que resolver al inicio

Antes de calcular nada, confirmar con el usuario (idealmente con `ask_user_input_v0`):

1. **Régimen tributario**: ProPyme 14D (tasa 12,5%) vs régimen general (27%). Define la tasa de impuestos diferidos. Verificar también si hay utilidad o pérdida tributaria.
2. **Período a convertir**: ¿solo el año en curso, o desde la apertura del año anterior? Define si se necesita asiento de apertura (NIIF 1).
3. **Destino**: ¿cargar de vuelta en Nubox (set paralelo) o llevarlo en archivo aparte? Define cuán estricto es el formato.
4. **Codificación del plan**: ¿adaptar la plantilla IFRS de Nubox (recomendado) o crear desde cero?
5. **Nivel de detalle de proveedores**: ¿centralizado con genérico, o desglosado por RUT real? (depende de qué reportes tenga el usuario).
6. **Arriendos**: ¿costo de explotación o gasto de administración? ¿aplica NIIF 16 (contratos > 12 meses)?

## Errores conocidos y sus soluciones (resumen)

- **"Archivo inválido" al cargar**: el archivo debe ser **.xls binario (MS Excel 97/BIFF)**, no .xlsx. Convertir con LibreOffice: `soffice --convert-to "xls:MS Excel 97"`.
- **"No se encontró código de cuenta (XXXX)"**: la cuenta no existe en el plan del set IFRS. Crearla manualmente en Nubox antes de cargar.
- **Errores de RUT / "campos requeridos" / "descripción código bancario"**: las cuentas con atributo (bancario, auxiliar, honorarios) exigen datos adicionales. Completar las columnas de auxiliar, o quitar el atributo en el set IFRS si es solo reportería.
- **Comprobante carga incompleto (le falta una línea)**: Nubox omite las líneas cuya cuenta no existe. Crear la cuenta faltante y recargar el comprobante completo.
- **Código de tipo de documento inválido**: para boletas de honorarios el código SII no es 48 (vale vista). Verificar el código correcto en la fuente oficial del SII (ver referencia 04).

## Verificación final obligatoria

El skill no está completo hasta confirmar, **con código**, que:
- La suma de (asientos reales traducidos + asientos de ajuste IFRS) reproduce **exactamente** el ESF y ER del informe.
- Activo = Pasivo + Patrimonio, diferencia cero.
- El resultado del ejercicio del ER coincide con el del ESF.

Mostrar al usuario la comparación rubro por rubro antes de dar por terminado el trabajo.

## Tono y comunicación

El usuario suele ser dueño de PyME o contador, no necesariamente experto en IFRS. Explicar los conceptos contables (qué es un impuesto diferido, por qué se reversa la corrección monetaria) con analogías simples cuando se pregunten. Ser transparente sobre los límites: cuando algo no se puede hacer con precisión (ej. desglosar compras centralizadas sin el reporte adecuado), decirlo claramente en vez de forzar un resultado dudoso.
