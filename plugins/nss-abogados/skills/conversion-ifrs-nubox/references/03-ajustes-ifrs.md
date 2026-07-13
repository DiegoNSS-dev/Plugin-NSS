# Fase 4: Cálculo de Ajustes IFRS

Cada ajuste se calcula sobre la base tributaria. Marcar los supuestos (vida útil, tasa) para validación con el contador. Todos los montos deben quedar documentados y cada asiento debe cuadrar.

## NIC 16 — Propiedad, Planta y Equipo (depreciación)

Problema típico: el SII permite depreciación instantánea/acelerada, dejando el activo en valor libro $1. IFRS exige depreciar a la **vida útil económica**.

Cálculo:
1. Costo de adquisición del activo (ej. equipos $4.040.005, comprados en un mes M de año anterior).
2. Vida útil IFRS (ej. 36 meses para equipos computacionales — confirmar con usuario).
3. Depreciación mensual = costo / vida útil.
4. **Ajuste de apertura** (si el activo se compró el año anterior): reversar el exceso de depreciación tributaria. Valor libro IFRS al cierre del año anterior = costo − (meses transcurridos × dep. mensual). El ajuste va contra **resultados acumulados** (NIIF 1, no contra resultado del período).
5. **Depreciación del período actual** = meses del período × dep. mensual. Va al gasto del período.

Asientos:
- Apertura: DEBE Equipos (sube a valor IFRS) / HABER Resultados acumulados.
- Período: DEBE Gasto depreciación / HABER Depreciación acumulada.

## NIC 19 — Provisión de Vacaciones

IFRS reconoce el costo de vacaciones a medida que se devengan; el SII solo al pagarlas.

Cálculo por empleado (no usar promedios si hay sueldos dispares como un gerente):
1. Días devengados al cierre = meses trabajados × tasa legal (1,25 días hábiles/mes).
   - Meses trabajados = (fecha cierre − fecha ingreso) en días / 30,4375.
   - **Importante**: calcular al cierre del período que se reporta, NO a la fecha actual. Si el usuario manda un reporte de vacaciones "a hoy", recalcular a la fecha de cierre.
   - Empleados que ingresaron después del cierre NO devengan.
2. Valor día = remuneración mensual imponible (sueldo + gratificación, del LRE) / 21,67 días hábiles promedio mes.
3. Provisión por empleado = días devengados × valor día.
4. Provisión total = suma de todos los empleados.

Verificar la tasa contra un reporte conocido: meses × 1,25 debe reproducir los días que muestra el sistema.

Asiento: DEBE Gasto remuneraciones (provisión vacaciones) / HABER Provisión de vacaciones (pasivo).

## NIC 12 — Impuestos Diferidos

Tasa según régimen: **ProPyme 14D = 12,5%**; régimen general = 27%. Confirmar con el usuario.

Por cada diferencia temporaria (diferencia entre valor contable IFRS y base tributaria de un activo/pasivo):
- **Activo mayor en IFRS que en tributario** → diferencia imponible → **pasivo** por impuesto diferido.
  Ej. equipos: (valor IFRS − valor tributario) × tasa. Si IFRS=3.366.671 y trib=1: 3.366.670 × 12,5% = 420.834.
- **Pasivo en IFRS sin equivalente tributario** → diferencia deducible → **activo** por impuesto diferido.
  Ej. provisión vacaciones: 1.569.106 × 12,5% = 196.138.

Efecto neto en resultado = pasivo − activo (ej. 420.834 − 196.138 = 224.696 gasto neto).

**Pérdidas tributarias acumuladas**: NO reconocer activo por impuesto diferido sobre ellas si la empresa tiene pérdidas recurrentes (NIC 12.34-36: solo se reconoce si es probable tener utilidades futuras). Es un criterio de prudencia; documentarlo y decir que se reevalúa cuando proyecte utilidades.

**Impuesto a la renta corriente**: si hay pérdida tributaria, el impuesto del período es $0. Los PPM pagados son un anticipo (activo), no gasto. Mostrar la línea de impuesto corriente en $0 para transparencia.

Asientos:
- Pasivo ID: DEBE Gasto impuesto diferido / HABER Pasivo imp. diferido.
- Activo ID: DEBE Activo imp. diferido / HABER (Ingreso) impuesto diferido.

## Corrección Monetaria — se elimina

IFRS no la reconoce. Identificar los comprobantes de CM en el libro:
- Si un comprobante es **CM pura** (solo toca cuentas de CM e IVA/PPM por corrección de remanente), se **excluye completo** del set IFRS (no deja descuadre porque sus dos líneas se van juntas).
- Si la CM está mezclada en un comprobante con otros movimientos, reversar solo las líneas de CM y verificar el cuadre.

El total IFRS será levemente menor al tributario por estos montos excluidos. Documentar la diferencia.

## NIC 21 — Diferencias de Cambio

Si hay cuentas en moneda extranjera (ej. banco USD): el ajuste por tipo de cambio del saldo se reconoce al **cierre del ejercicio anual**. Si no hubo movimientos en el período intermedio, el saldo se mantiene y no hay ajuste de conversión (consistente con el criterio tributario). No forzar ajustes intermedios.

## NIIF 16 — Arrendamientos

Aplica a contratos de arriendo > 12 meses (salvo bajo valor). Requiere datos que el usuario debe proveer: **plazo contractual, tasa de descuento, opciones de renovación** de cada contrato. Sin esos datos, queda **pendiente** y se documenta como tal en las notas. No inventar el cálculo.

Cuando haya datos: reconocer activo por derecho de uso y pasivo por arrendamiento (valor presente de los pagos), amortizar el activo y devengar interés sobre el pasivo.

## Asiento de apertura consolidado (NIIF 1)

Si se convierte solo el año en curso pero hay ajustes que vienen de años anteriores (ej. apertura de equipos), va un asiento de apertura con fecha primer día del período, contra resultados acumulados. Este asiento es lo que hace que los activos y el patrimonio lleguen al valor IFRS correcto. Es frecuente que se olvide al cargar; verificar siempre que esté.
