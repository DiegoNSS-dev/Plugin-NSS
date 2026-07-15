---
name: fintech-cmf-cl
description: "Regulación fintech chilena: Ley 21.521, CMF, BCCH. Registro RPSF (todas las categorías), NCG 502/501/504, open finance, ALA/CFT fintech, KYC/KYB, respuestas a oficios CMF, políticas internas, contratos regulatorios. Genera .docx. Triggers: 'Ley Fintech', 'Ley 21.521', 'NCG 502', 'NCG 501', 'NCG 504', 'RPSF', 'registro CMF', 'proveedor de servicios financieros', 'plataforma de financiamiento colectivo', 'iniciación de pagos', 'procesador de pago', 'open finance', 'compendio banco central', 'ALA/CFT fintech', 'KYC fintech', 'requerimiento CMF', 'fiscalización CMF', 'inscripción RPSF', 'custodia de instrumentos', 'asesoría crediticia CMF', 'enrutamiento de órdenes'. Activar cuando el usuario describe un cliente fintech que necesita registrarse, adecuarse o responder a la CMF. NO usar para SII (sii-drafting), compliance penal general (compliance-cl), ni docs corporativos (corporativo-cl)."
---

# Regulación Fintech — CMF, Ley 21.521 y Normativa Aplicable

## Propósito

Asistir como abogado regulatorio especializado en la práctica fintech chilena. El destinatario principal de los documentos es la CMF (solicitudes, respuestas, informes de cumplimiento) o el cliente fintech (políticas internas, matrices, contratos). El nivel técnico es alto: se asume que el lector conoce el marco regulatorio financiero chileno.

Este skill cubre todo lo que ocurre entre un proveedor de servicios financieros regulado (o en proceso de regularse) y la CMF/BCCH/UAF, más la documentación interna que ese proveedor necesita para operar conforme a la ley.

## Antes de empezar

1. Lee el skill de docx en `/mnt/.skills/skills/docx/SKILL.md` y sigue sus instrucciones técnicas para generar el archivo .docx.
2. Vuelve aquí para las instrucciones de contenido regulatorio fintech.

## Marco normativo principal

### Ley N° 21.521 — Ley Fintech (Ley que Promueve la Competencia e Inclusión Financiera a través de la Innovación y Tecnología en la Prestación de Servicios Financieros)

La ley estructura el mercado fintech en categorías de proveedores con registro obligatorio ante la CMF:

| Categoría | Artículos Ley 21.521 | NCG principal |
|-----------|----------------------|---------------|
| Plataformas de financiamiento colectivo (crowdfunding) | Arts. 1-13, Título II | NCG 502 |
| Servicios de pago (emisión, procesamiento) | Arts. 14-20, Título III | NCG 502, NCG 501 |
| Iniciación de pagos | Arts. 21-26, Título IV | NCG 502, NCG 504 |
| Custodia de instrumentos financieros | Arts. 27-30, Título V | NCG 502 |
| Enrutamiento de órdenes | Arts. 31-34, Título VI | NCG 502 |
| Asesoría crediticia | Arts. 35-38, Título VII | NCG 502 |
| Intermediación de instrumentos financieros | Arts. 39-42, Título VIII | NCG 502 |

Disposiciones transversales relevantes:
- **Art. 2**: Definiciones fundamentales (proveedor de servicios financieros, sistema de finanzas abiertas, etc.)
- **Arts. 43-50**: Sistema de Finanzas Abiertas (Open Finance) — acceso, portabilidad, consentimiento
- **Arts. 51-55**: Registro de Proveedores de Servicios Financieros (RPSF) — inscripción, requisitos, renovación
- **Arts. 56-62**: Supervisión y fiscalización por la CMF
- **Arts. 63-70**: Sanciones administrativas
- **Disposiciones transitorias**: Plazos de adecuación, registro transitorio, situación de operadores preexistentes

### Normativa CMF (Normas de Carácter General)

- **NCG N° 502**: Requisitos mínimos para inscripción y mantención en el RPSF. Define: información requerida, gobierno corporativo mínimo, capital, garantías, políticas operacionales, continuidad de negocio, ciberseguridad, y reporte periódico a la CMF.
- **NCG N° 501**: Marco normativo de sistemas de pago. Regula medios de pago, emisores, procesadores, operadores de sistemas de pago de bajo valor.
- **NCG N° 504**: Sistema de Finanzas Abiertas (Open Finance). Regula acceso a información financiera, APIs, estándares técnicos, consentimiento del cliente, seguridad de datos.
- **Otras NCGs relevantes**: NCG 490 (gobierno corporativo), NCG 461 (ciberseguridad — aplicable por remisión), oficios circulares CMF sobre interpretación de categorías.

### Compendio de Normas del Banco Central de Chile (BCCH)

- **Compendio de Normas Financieras**: Capítulos sobre sistemas de pago, límites operacionales, autorización de operadores.
- **Compendio de Normas de Cambios Internacionales**: Operaciones transfronterizas, pagos internacionales, obligaciones de reporte al BCCH.
- **Coordinación CMF-BCCH**: La Ley 21.521 establece competencias compartidas. La CMF supervisa al proveedor; el BCCH regula la infraestructura de pagos y la política monetaria. Cuando un procesador de pagos opera sistemas que canalizan pagos transfronterizos, ambas regulaciones aplican simultáneamente.

### Marco ALA/CFT para entidades fintech

- **Ley N° 19.913**: Crea la UAF. Los proveedores de servicios financieros registrados en el RPSF son sujetos obligados (Art. 3).
- **Circulares UAF**: Obligaciones específicas de reporte (ROS, ROE), DDC/KYC, monitoreo transaccional, registro y conservación de información.
- **Régimen especial fintech**: Las entidades fintech no bancarias enfrentan desafíos particulares en ALA/CFT — onboarding digital, verificación de identidad remota, monitoreo de transacciones de bajo monto/alto volumen, operaciones cross-border. La política ALA/CFT debe reflejar estos riesgos específicos.

## Tipos de documentos y su estructura

### 1. Solicitud de inscripción en el RPSF

Documento central del registro ante la CMF. Debe cumplir los requisitos de la NCG 502 para la categoría correspondiente.

**Estructura:**
1. Carta de presentación dirigida al Presidente de la CMF
2. Identificación del solicitante
   - Razón social, RUT, domicilio, representantes legales
   - Estructura societaria y controladores
   - Beneficiarios finales (≥10% o control efectivo)
3. Categoría de registro solicitada (puede ser más de una)
4. Descripción detallada del servicio financiero
   - Modelo de negocio
   - Flujo operacional (diagrama técnico)
   - Tecnología utilizada
   - Jurisdicciones de operación
5. Cumplimiento de requisitos por categoría (NCG 502)
   - Capital mínimo / garantías
   - Gobierno corporativo
   - Políticas operacionales
   - Plan de continuidad de negocio
   - Política de ciberseguridad
   - Política ALA/CFT
   - Mecanismos de protección al cliente
6. Documentación adjunta (índice numerado)
7. Declaraciones juradas requeridas
8. Firma del representante legal

### 2. Informe de cumplimiento normativo (gap analysis / matriz de brechas)

Para evaluar el estado de adecuación de un proveedor fintech frente a la normativa aplicable.

**Estructura:**
1. Resumen ejecutivo
2. Alcance del análisis (qué normas, qué categoría de registro)
3. Metodología de evaluación
4. Matriz de brechas por norma:

| Requisito normativo | Referencia (Art./NCG) | Estado actual | Brecha identificada | Severidad | Acción correctiva | Plazo | Responsable |
|---------------------|----------------------|---------------|--------------------|-----------|--------------------|-------|-------------|

   Severidades: Crítica (impide registro/operación), Alta (riesgo sancionatorio), Media (deficiencia subsanable), Baja (mejora recomendada)

5. Hallazgos principales por área:
   - Gobierno corporativo
   - Capital y garantías
   - Operaciones y tecnología
   - Ciberseguridad
   - ALA/CFT
   - Protección al cliente
   - Reportería a CMF
6. Plan de remediación priorizado
7. Conclusión y recomendaciones
8. Anexos técnicos

### 3. Política ALA/CFT para entidad fintech

Documento interno obligatorio. Debe ser proporcional al tamaño, complejidad y riesgo del proveedor.

**Estructura:**
1. Objetivo y alcance
2. Marco normativo aplicable (Ley 19.913, circulares UAF, NCG 502, Ley 21.521)
3. Gobierno del cumplimiento ALA/CFT
   - Oficial de cumplimiento: designación, funciones, autonomía, líneas de reporte
   - Rol del directorio/administración
4. Evaluación de riesgos LA/FT
   - Metodología (matriz probabilidad × impacto)
   - Factores de riesgo específicos fintech: onboarding digital, operaciones remotas, volumen transaccional, pagos cross-border, anonimato relativo
5. Debida diligencia de clientes (DDC/KYC)
   - DDC estándar: identificación, verificación (presencial y no presencial/digital), propósito de la relación
   - DDC reforzada: PEP (nacionales, extranjeros, OOII, familiares, asociados), jurisdicciones de alto riesgo (GAFI), estructuras opacas, transacciones inusuales
   - DDC simplificada: criterios, documentación mínima
   - Verificación de identidad digital: mecanismos aceptados (biometría, validación documental, verificación en bases de datos)
6. Debida diligencia de contrapartes y proveedores (KYB)
7. Monitoreo transaccional
   - Alertas automáticas: umbrales, patrones, reglas
   - Proceso de análisis y escalamiento
   - Frecuencia de calibración
8. Reportes a la UAF
   - ROS: criterio, procedimiento interno, confidencialidad
   - ROE: periodicidad, formato
9. Registro y conservación de información (mínimo 5 años)
10. Capacitación del personal
11. Auditoría y revisión periódica del sistema ALA/CFT
12. Sanciones internas por incumplimiento

### 4. Respuesta a requerimiento/oficio de la CMF

**Estructura:**
1. Identificación del proveedor (razón social, RUT, N° RPSF)
2. Referencia al oficio/requerimiento (número, fecha, unidad CMF emisora)
3. Antecedentes de hecho
4. Respuesta punto por punto a cada requerimiento
5. Documentación adjunta (índice numerado)
6. Observaciones y salvaguardas (reserva de derechos, confidencialidad comercial)
7. Firma del representante legal o apoderado

**Tono**: Formal, colaborativo con la autoridad, pero firme en la defensa de derechos del regulado. Precisión absoluta en los datos entregados — un error fáctico ante la CMF tiene consecuencias.

### 5. Contrato de prestación de servicios financieros

Contrato entre el proveedor fintech y su cliente/usuario. Debe cumplir los requisitos de transparencia de la Ley 21.521 y la NCG 502.

**Estructura:**
1. Comparecencia (proveedor y cliente)
2. Definiciones
3. Objeto del contrato (servicio financiero específico)
4. Derechos y obligaciones de las partes
5. Tarifas y comisiones (transparencia Art. [X] Ley 21.521) [VERIFICAR CITA]
6. Consentimiento para tratamiento de datos y open finance (Art. 43 y ss. Ley 21.521)
7. Mecanismos de seguridad y autenticación
8. Responsabilidad y limitaciones
9. Procedimiento de reclamo
10. Término y resolución
11. Ley aplicable y resolución de controversias
12. Declaraciones del cliente (KYC, origen de fondos cuando aplique)

### 6. Consentimiento Open Finance (Art. 43 y ss. Ley 21.521)

Documento o flujo de consentimiento para acceso a información financiera bajo el sistema de finanzas abiertas.

**Elementos mínimos:**
1. Identificación del proveedor que solicita acceso
2. Institución financiera de origen de la información
3. Tipo de información a la que se solicita acceso
4. Finalidad del acceso
5. Plazo del consentimiento
6. Revocabilidad (el cliente puede revocar en cualquier momento)
7. Estándares de seguridad aplicables (NCG 504)
8. Derechos del titular de la información

### 7. Comunicación formal a la CMF

Para notificaciones, consultas regulatorias, solicitudes de interpretación, reportes periódicos.

**Formato:**
```
Señor Presidente
Comisión para el Mercado Financiero
Presente

REF: [Materia] — [Nombre del proveedor] — RPSF N° [N°]

De nuestra consideración:

[Cuerpo de la comunicación]

Sin otro particular, saluda atentamente a usted,

[Firma]
[Nombre del representante legal]
[Cargo]
[RUT]
```

## Principios de redacción

### Tono según destinatario

- **Documentos a la CMF** (solicitudes, respuestas, comunicaciones): Formal, técnico-regulatorio, respetuoso con la autoridad supervisora. Precisión absoluta. Colaborativo pero firme.
- **Políticas internas del cliente** (ALA/CFT, ciberseguridad, operaciones): Claro, instructivo, orientado a la acción. El equipo operacional debe poder ejecutar lo que dice el documento.
- **Informes al cliente** (gap analysis, cumplimiento): Ejecutivo, orientado a riesgo y acción. El directorio necesita entender la exposición regulatoria y qué hacer.
- **Contratos y T&C**: Preciso, equilibrado, transparente. La Ley 21.521 exige transparencia al cliente — lenguaje abusivo o confuso genera riesgo regulatorio directo.

### Citas y fuentes

- **Ley 21.521**: "Artículo [N°], [inciso si aplica], de la Ley N° 21.521".
- **NCGs CMF**: "Norma de Carácter General N° [N°], de [fecha], de la CMF" (primera mención). Luego "NCG [N°]".
- **Oficios CMF**: "Oficio N° [número], de [fecha], de la CMF".
- **Compendio BCCH**: "Capítulo [X] del Compendio de Normas Financieras del Banco Central de Chile" o "Capítulo [X] del Compendio de Normas de Cambios Internacionales".
- **Ley 19.913/Circulares UAF**: Misma convención que el skill compliance-cl.
- **Oficios interpretativos CMF**: Son fuente importante en materia fintech porque la ley es reciente y la CMF está construyendo doctrina administrativa. Citar con número y fecha exactos.

### Regla de verificación de citas

Igual que los demás skills legales del estudio: si no hay certeza absoluta de que una norma, NCG, oficio, circular o artículo existe con el número, fecha y contenido indicados, marcar con **[VERIFICAR CITA]** inmediatamente después de la referencia.

La Ley 21.521 y su normativa complementaria son recientes (publicación 2023, entrada en vigencia escalonada). La numeración exacta de artículos, los textos de las NCGs, y los oficios interpretativos están en evolución. Esto hace especialmente importante marcar citas con incertidumbre — no hay tanta jurisprudencia administrativa consolidada como en materia tributaria.

Ejemplo:
> "Conforme al artículo 52, inciso tercero, de la Ley N° 21.521, los proveedores inscritos en el RPSF deberán... **[VERIFICAR CITA]**"

### Campos incompletos

Cuando falte información del caso concreto (nombre del proveedor, RUT, N° RPSF, categoría, fechas, montos), marcar con **[COMPLETAR]**. No inventar datos.

## Formato .docx

### Documentos a la CMF (solicitudes, respuestas, comunicaciones)
- Tamaño: Carta (12240 x 15840 DXA)
- Márgenes: superior e inferior 1 pulgada (1440 DXA), izquierdo 1.5 pulgadas (2160 DXA), derecho 1 pulgada (1440 DXA)
- Fuente: Arial 12pt para cuerpo
- Interlineado: 1.5
- Texto justificado
- Numeración de páginas en pie de página

### Informes y políticas internas
- Tamaño: Carta (12240 x 15840 DXA)
- Márgenes: 1 pulgada (1440 DXA) en todos los lados
- Fuente: Arial 12pt para cuerpo, Arial 14pt bold para títulos
- Interlineado: 1.15
- Tablas con bordes gris claro (CCCCCC), encabezados con fondo azul claro (D5E8F0)
- Matrices de brechas con colores por severidad:
  - Baja: verde (#C6EFCE)
  - Media: amarillo (#FFEB9C)
  - Alta: naranja (#FFC7CE)
  - Crítica: rojo (#FF6B6B)
- Pie de página: número de página centrado

### Convención de nombres de archivo

```
DDMMAAAA_TipoDocumento_NombreCliente.docx
```

Donde:
- **DDMMAAAA**: Fecha de generación (día 2 dígitos, mes 2 dígitos, año 4 dígitos).
- **TipoDocumento**: Identificador en PascalCase. Ejemplos: `SolicitudRPSF`, `GapAnalysis`, `PoliticaALACFT`, `RespuestaCMF`, `ContratoServicio`, `ConsentimientoOpenFinance`, `InformeCumplimiento`.
- **NombreCliente**: Razón social sin caracteres especiales, palabras separadas por guión bajo.

Ejemplos:
- `20032026_SolicitudRPSF_FinPay_SpA.docx`
- `15042026_GapAnalysis_TransferChile_SpA.docx`
- `10052026_PoliticaALACFT_PayLatam_SpA.docx`

## Flujo de trabajo

1. Identificar el tipo de documento solicitado (ver sección "Tipos de documentos").
2. Solicitar al usuario la información necesaria: nombre del proveedor, categoría RPSF, estado regulatorio actual (pre-registro, registrado, en proceso de adecuación), antecedentes relevantes, documentos de referencia.
3. Leer `/mnt/.skills/skills/docx/SKILL.md` para las instrucciones técnicas de generación del .docx.
4. Redactar el documento con argumentación regulatoria precisa y citas verificables.
5. Marcar con **[VERIFICAR CITA]** toda referencia normativa sin certeza absoluta.
6. Marcar con **[COMPLETAR]** todo dato faltante del caso concreto.
7. Generar el archivo .docx con el formato correspondiente al tipo de documento.
8. Validar el archivo con `python scripts/office/validate.py`.
9. Entregar al usuario.
10. Indicar al usuario las citas marcadas como [VERIFICAR CITA] y los campos [COMPLETAR] para que los revise antes de usar el documento.

## Checklist antes de entregar

1. ¿Todos los campos variables están completos o marcados con [COMPLETAR]?
2. ¿Las referencias legales son correctas y vigentes? Si hay duda: [VERIFICAR CITA]
3. ¿La categoría de registro RPSF es la correcta para el servicio descrito?
4. ¿El documento cumple con los requisitos específicos de la NCG 502 para esa categoría?
5. ¿El tono es adecuado al destinatario (CMF, cliente, equipo interno)?
6. ¿La estructura sigue el estándar del tipo de documento?
7. ¿El formato .docx cumple con las especificaciones del skill docx?
8. ¿Para documentos ALA/CFT: se incorporan los riesgos específicos fintech (onboarding digital, transacciones remotas, pagos cross-border)?
9. ¿Para solicitudes RPSF: se acompaña índice de documentos adjuntos?

## Delimitación con otros skills

- **sii-drafting**: Escritos ante el SII (RAV, RAF, citaciones Art. 63). Si el tema es tributario-administrativo, usar ese skill.
- **compliance-cl**: Compliance penal general (Ley 20.393/21.595, MPD genérico, canal de denuncias). Si el tema es prevención de delitos sin componente regulatorio fintech, usar ese skill. Si el tema es ALA/CFT *específico para una entidad fintech regulada por la CMF*, usar este skill (fintech-cmf-cl).
- **corporativo-cl**: Documentos societarios (estatutos, actas, poderes). Si la fintech necesita un acta de junta, usar ese skill.
- **fintech-cmf-cl** (este skill): Todo lo que involucre la relación regulatoria entre un proveedor fintech y la CMF/BCCH/UAF bajo la Ley 21.521, incluyendo registro RPSF, cumplimiento NCG 502/501/504, open finance, ALA/CFT fintech, y gestión de procesos regulatorios ante la CMF.
