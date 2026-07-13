---
name: estandar-docx-nss
description: "Genera documentos Word (.docx) para NSS (firma legal, tributaria y contable chilena) aplicando el estándar de formato canónico de NSS — Arial 11pt negro, interlineado 1.5, justificado, tamaño carta, márgenes de 1 pulgada, logo NSS en el encabezado, numeración de página y la convención de nombres YYYYMMDD_tipo_identificacion. Usa esta skill SIEMPRE que el usuario quiera crear, redactar, generar o dar formato a CUALQUIER documento Word de NSS — contratos, estatutos, actas de directorio o junta, escrituras, poderes, propuestas o cotizaciones a clientes, cartas, e informes contables, tributarios o de auditoría — aunque no diga explícitamente formato ni .docx. Si el entregable es un documento Word de parte de NSS, esta skill aplica."
---

# Estándar de documentos .docx — NSS

Cuando generes cualquier documento Word para NSS, debe verse como si saliera de la misma firma, sin importar quién lo pidió ni para qué área es. La coherencia de formato es parte de cómo NSS comunica que es una firma seria y moderna, así que trata estas especificaciones como el estilo de la casa, no como sugerencias.

Genera el documento con **docx-js** (la librería `docx` de Node.js): instálala localmente en una carpeta temporal, arma el archivo con un script y entrega el `.docx` resultante.

## Cómo generar

```bash
npm init -y && npm install docx
```

Instala **local, nunca global**. Para el andamiaje de código con los valores NSS ya configurados (márgenes, fuente, encabezado con logo, pie con número de página, tablas), lee `references/plantilla-docx-js.md` y adáptalo al documento que te pidan.

## Especificaciones generales (canónicas)

| Parámetro | Valor |
|-----------|-------|
| Motor | docx-js (Node.js). Instalar local: `npm init -y && npm install docx` |
| Tamaño de página | Carta / US Letter — 12240 x 15840 DXA |
| Márgenes | 1 pulgada (1440 DXA) en los 4 lados |
| Margen izquierdo (solo demandas judiciales) | 1.5 pulgadas (2160 DXA) |
| Fuente | Arial 11pt en TODO el documento (cuerpo, tablas, viñetas, firmas, encabezados de sección) |
| Tamaño en docx-js | `size: 22` (half-points = 11pt) |
| Interlineado | 1.5 → `spacing: { line: 360 }` |
| Color de texto | Negro (#000000) sin excepciones. Sin texto de color, sin destacados decorativos |
| Alineación cuerpo | Justificado (`AlignmentType.JUSTIFIED`) |

## Jerarquía visual

| Elemento | Formato |
|----------|---------|
| Título del documento | Arial 11pt, negrita, subrayado, centrado |
| Nombre sociedad / identificación | Arial 11pt, negrita, centrado |
| Secciones / encabezados | Arial 11pt, negrita o subrayado, justificado |
| Cláusulas / acuerdos numerados | "PRIMERO:", "SEGUNDA:", etc. — negrita, justificado |
| Cuerpo de texto | Arial 11pt, normal, justificado |
| Firmas | Línea "___" + nombre + RUT, todo en negrita, justificado |
| Pie de página | Número de página centrado |

## Encabezado y pie

- **Header con logo**: usa `assets/nss-logo.png` de esta skill. Respeta el aspect ratio nativo del PNG, nunca hardcodees dimensiones que lo deformen.
  - Logo actual: 1000 x 259 px (ratio ≈ 3.86).
  - Render estándar compacto: `transformation: { width: 110, height: 28 }`.
  - Si se requiere un logo mayor: `height = round(width / 3.87)`.
  - **Si `assets/nss-logo.png` no existe**, pídele el archivo al usuario (o genera un encabezado de solo texto y avísale), en vez de inventar dimensiones o rutas.
- **Header limpio (propuestas / cartas a cliente)**: solo el logo, alineado a la izquierda. Sin dirección ni contactos.
- **Header completo (informes formales)**: logo + dirección + contactos.
- **Footer**: número de página. Centrado por defecto; en propuestas va a la derecha en Arial 9pt (única excepción al 11pt).
- **Espaciado del título principal**: `spacing: { before: 800 }` para separarlo del logo; subtítulo `spacing: { after: 400 }`. Meta visual: 2–3 líneas en blanco entre logo y título.

## Numeración de cláusulas

- Estatutos: "ARTÍCULO PRIMERO:", "ARTÍCULO SEGUNDO:", ...
- Estatutos notariales / escritura pública: "PRIMERO:", "SEGUNDO:", ...
- Acuerdos dentro de acta: "Primero:", "Segundo:", "Tercero:"
- Actas — materias de tabla: 1), 2), 3) o descripciones
- Resto de documentos: numeración arábiga

## Color en tablas (única excepción al negro)

Los colores solo se permiten en **fondos de celda**, nunca en texto. Ejemplo de columna de severidad:

- Rojo `#FF4444`, texto blanco → ALTO
- Amarillo `#FFD700`, texto negro → MEDIO
- Verde `#4CAF50`, texto blanco → BAJO

## Notas técnicas docx-js

- Fondos de celda: usar `ShadingType.CLEAR` (no `.SOLID`).
- Tablas: definir `width` tanto en `TableCell` como en `Table`.
- Viñetas: `LevelFormat.BULLET` en la config de `numbering`.
- Instalar local, no global.

## Convención de nombres de archivo

Formato general: `[YYYYMMDD]_[tipo]_[identificacion].docx`. Usa siempre `YYYYMMDD` (no DDMMAAAA) para que los archivos ordenen cronológicamente.

Ejemplos:
- `20260321_propuesta_aumento-capital_autonomation.docx`
- `20260321_informe_revision_eeff_inversiones-xy.docx`
- `20260321_EstudioTitulos_Lote4_Vitacura.docx`

## Checklist antes de entregar

1. ¿Campos variables completos o marcados `[COMPLETAR]`?
2. ¿Referencias legales correctas y vigentes? Si hay duda: `[VERIFICAR CITA]`.
3. ¿Comprensible para un cliente no-abogado?
4. ¿Formato cumple este estándar (Arial 11pt, negro, 1.5, justificado, carta, márgenes 1")?
5. ¿Logo con aspect ratio correcto?

## Nota de consistencia

El estándar canónico de NSS es **11pt / interlineado 1.5**. La skill antigua `legal-docs-cl` usaba 12pt cuerpo / 14pt títulos e interlineado 1.15 — **no** sigas eso: usa 11pt / 1.5 en todos los documentos NSS.
