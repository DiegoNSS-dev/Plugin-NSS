# Fase 3: Plan de Cuentas IFRS y Mapeo

## Estrategia recomendada: partir de la plantilla IFRS de Nubox

Nubox trae **dos planes predeterminados**: "Plantilla Nubox" (tributaria tradicional) e **"IFRS - Plantilla Nubox"**. La plantilla IFRS ya tiene estructura correcta (corriente/no corriente, ingresos y gastos por función) y muchas cuentas listas.

**No crear el plan desde cero.** En su lugar:
1. El usuario copia la plantilla IFRS a nuevo (botón "Copiar a Nuevo" en Configuración → Plan de Cuentas) y la nombra para la empresa.
2. Sobre esa copia, agrega solo las cuentas que falten.

No existe carga masiva del plan de cuentas en Nubox: las cuentas se crean/editan una por una en Configuración → Plan de Cuentas. Por eso conviene minimizar las cuentas nuevas.

## Qué suele traer la plantilla IFRS de Nubox (no recrear)

- 1212 Activos por impuestos diferidos (con subcuentas por pérdidas fiscales y revaluaciones)
- 2206 Pasivo por impuestos diferidos
- 2106-01 Provisión de vacaciones ← clave, ya viene
- 1209 Propiedades, planta y equipo (con depreciación acumulada)
- 1207 Activos intangibles
- 1104-01 Deudores clientes [auxiliar]
- 2102-01 Facturas por pagar [auxiliar], 2102-11 Honorarios por pagar [honorarios]
- 1113 Activos por impuestos corrientes (PPM, IVA CF); 2105 Pasivos por impuestos
- 2104-01 Provisión PPM

## Qué suele FALTAR y hay que crear

La plantilla trae cuentas de balance para impuesto diferido, pero NO las de **resultado**. Cuentas que típicamente hay que crear:

**De balance:**
- Bancos específicos de la empresa (ej. 1101-04 Banco CLP, 1101-05 Banco USD) [atributo Bancario]
- Anticipos a proveedores, arriendos pagados por anticipado
- CxC / CxP con entidades relacionadas (mutuos, holding)
- Garantías de arriendo
- 1212-03 Activo imp. diferido por **diferencias temporarias** (la plantilla solo trae por pérdidas fiscales) ← causa frecuente de error de carga
- 2206-01 Pasivo imp. diferido por diferencias temporarias
- Equipos computacionales y su depreciación acumulada si no están

**De resultado (las que más faltan):**
- Depreciación del ejercicio (la plantilla no trae depreciación en resultado)
- Diferencia de cambio en resultado
- Impuesto a la renta corriente
- Gasto (ingreso) por impuesto diferido
- Subcuentas de gasto específicas (arriendos, servicios legales, contables, marketing, comisiones de plataformas, gastos de viaje, etc.)

**NIIF 16 (si aplica):**
- Activo por derecho de uso + su amortización acumulada
- Pasivo por arrendamiento corriente y no corriente
- Amortización del derecho de uso (resultado)

## Corrección monetaria: cuentas inactivas

IFRS no reconoce corrección monetaria (NIC 29, Chile no es hiperinflacionario). Las cuentas de CM **no se usan** en el set IFRS. Si Nubox las exige por validación, crearlas pero sin movimiento (inactivas). Confirmar con el usuario si su Nubox las requiere.

## La tabla de mapeo (el corazón del proceso)

Construir un diccionario cuenta tributaria → cuenta IFRS. Solo se mapean las cuentas que efectivamente aparecen en los asientos del período (no las 260 del plan). Reglas observadas:

- Reclasificaciones importantes: arriendos de "costo de explotación" (41xx) → "gasto de administración" (si las oficinas son administrativas).
- "Gastos no aceptados/rechazados" (concepto tributario) → gasto del período en IFRS.
- Corrección monetaria → no se mapea (se elimina).
- Cuentas transitorias de remuneración → su equivalente IFRS.
- Atributos: trasladar al destino (banco→bancario, clientes/proveedores→auxiliar, honorarios→honorarios).

Producir un Excel con tres hojas: (1) Plan IFRS completo, (2) Leyenda de criterios, (3) Mapeo de las cuentas usadas. Marcar con color las cuentas nuevas a crear y las inactivas.

## Entregable de esta fase

Una **lista corta y precisa de cuentas a crear manualmente** en Nubox, con: código sugerido, descripción, bajo qué mayor va, atributos a marcar, y para qué ajuste sirve. Separar "crear ahora" de "crear solo si aplica NIIF 16". Esto es lo que el usuario ejecuta a mano.
