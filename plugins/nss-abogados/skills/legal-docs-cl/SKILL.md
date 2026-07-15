---
name: legal-docs-cl
description: "Genera documentos legales corporativos y tributarios bajo derecho chileno en formato .docx profesional. Usa este skill cuando el usuario pida crear, redactar o modificar: estatutos de sociedades (SpA, SRL, SA), actas de juntas de accionistas o socios, poderes, contratos, informes tributarios, memorándums legales, cartas a clientes, propuestas comerciales de servicios legales, o cualquier documento legal dirigido a clientes. También se activa cuando el usuario mencione 'estatutos', 'junta de accionistas', 'acta', 'poder', 'informe tributario', 'memorándum', 'propuesta', 'contrato', o cualquier documento corporativo o tributario chileno destinado a lectura por clientes. NO usar para escritos ante el SII, tribunales o recursos administrativos — para esos existe el skill legal-briefs-cl."
---

# Documentos Legales Corporativos y Tributarios — Derecho Chileno

## Propósito

Crear documentos legales de alta calidad profesional destinados a clientes: estatutos societarios, actas de juntas, informes, memorándums, contratos y propuestas. El lenguaje debe ser jurídicamente preciso pero accesible para el cliente.

## Antes de empezar

1. Lee el skill de docx en `/mnt/skills/public/docx/SKILL.md` y sigue sus instrucciones técnicas para generar el archivo .docx.
2. Luego vuelve aquí para las instrucciones de contenido legal.

## Principios de redacción

### Tono y lenguaje
- Lenguaje jurídico correcto, pero que un cliente empresario pueda entender sin ser abogado.
- Evitar latinismos innecesarios. Cuando se use un término técnico, explicarlo brevemente entre paréntesis si el contexto lo amerita.
- Frases directas, párrafos cortos. No sacrificar precisión por simplicidad, pero tampoco oscurecer por pedantería.
- Voz activa cuando sea posible. Pasiva solo cuando la estructura legal lo exija.

### Estructura de documentos

Cada tipo de documento tiene su estructura estándar. Respetarla siempre:

**Estatutos de sociedad (SpA, SRL, SA):**
1. Comparecencia (individualización de socios/accionistas)
2. Constitución y denominación social
3. Objeto social
4. Domicilio
5. Capital social y forma de pago
6. Administración
7. Juntas de accionistas/socios (si aplica)
8. Distribución de utilidades
9. Duración
10. Disolución y liquidación
11. Arbitraje / resolución de conflictos
12. Cláusulas transitorias (primer directorio, poderes, etc.)

**Actas de juntas de accionistas/socios:**
1. Encabezado (tipo de junta, fecha, hora, lugar)
2. Asistentes y representados (nombre, RUT, acciones/participación)
3. Quórum
4. Tabla/orden del día
5. Desarrollo de cada punto de tabla
6. Acuerdos adoptados (redactados como resoluciones numeradas)
7. Cierre y firma

**Informes tributarios / Memorándums:**
1. Destinatario, fecha, referencia
2. Resumen ejecutivo (máximo 3-4 líneas)
3. Antecedentes del caso
4. Análisis (con referencias normativas)
5. Conclusión y recomendación
6. Firma

**Propuestas de servicios legales:**
1. Identificación del cliente
2. Materia / contexto
3. Alcance del trabajo
4. Equipo a cargo
5. Honorarios y forma de pago
6. Plazo estimado
7. Condiciones generales

### Legislación aplicable — Fuentes válidas

Citar siempre con artículo, inciso y/o número cuando corresponda:

- Código de Comercio
- Ley N° 18.046 sobre Sociedades Anónimas
- Ley N° 3.918 sobre Sociedades de Responsabilidad Limitada
- Ley N° 20.190 (SpA — Título VII del Código de Comercio, arts. 424 y ss.)
- Código Civil (personas, obligaciones, contratos)
- Código Tributario (DL 830)
- Ley sobre Impuesto a la Renta (DL 824)
- Ley sobre Impuesto a las Ventas y Servicios (DL 825)
- Oficios del SII (citar número, fecha y materia)
- Circulares del SII (citar número y fecha)
- Resoluciones del SII (citar número y fecha)
- Convenios para Evitar la Doble Tributación (indicar país contraparte y artículo)

### Reglas de citación

- En documentos dirigidos a clientes (informes, memorándums), incluir referencias normativas en el cuerpo del texto de forma natural: "Conforme al artículo 14 de la Ley sobre Impuesto a la Renta..."
- En estatutos y actas, las referencias legales van implícitas en la estructura; no es necesario citar artículo por artículo salvo que sea relevante.
- Si no se tiene certeza de la vigencia o existencia exacta de una norma, circular, oficio o resolución: marcar con **[VERIFICAR CITA]** en el texto. Nunca inventar un número de oficio o circular.

### Formato .docx

**Reglas de formato OBLIGATORIAS para todos los documentos:**

- Tamaño carta (Letter: 12240 x 15840 DXA)
- Márgenes: 1 pulgada (1440 DXA) en todos los lados.
- **Fuente: Arial 11 pt (size: 22 en docx-js) para TODO el documento.**
- **Color de fuente: negro (`000000`) en todo el texto, incluidos títulos.** No usar colores en el cuerpo ni en los encabezados de sección.
- **Interlineado: 1,5 líneas (en docx-js: `spacing: { line: 360, lineRule: "auto" }`).**
- Títulos: Arial, en **negrita**, color negro. Pueden ir a mayor tamaño para jerarquía, pero la fuente siempre es Arial y el color siempre negro.
- Numeración de cláusulas: Usar estilo "PRIMERA:", "SEGUNDA:", etc. para estatutos. Numeración arábiga para el resto.
- **Logo institucional: incluir SIEMPRE el logo de NSS en la esquina superior izquierda**, dentro del encabezado (header), respetando los márgenes de la página y en tamaño pequeño (ver más abajo).
- Pie de página: Número de página centrado.

#### Logo NSS en el encabezado (obligatorio)

El logo se encuentra en `assets/logo-nss-black.png` (dentro de este skill). Debe ir en la **esquina superior izquierda**, dentro del header, alineado al margen izquierdo (no invade el margen) y en **tamaño pequeño** (ancho ≈ 132 px, alto ≈ 34 px; mantiene la proporción original 520×134).

```javascript
const fs = require("fs");
const path = require("path");
const { Header, Paragraph, ImageRun, AlignmentType } = require("docx");

// Ruta al asset del skill
const LOGO = fs.readFileSync(path.join(__dirname, "assets", "logo-nss-black.png"));

const nssHeader = new Header({
  children: [
    new Paragraph({
      alignment: AlignmentType.LEFT, // esquina superior izquierda
      children: [
        new ImageRun({
          type: "png",
          data: LOGO,
          transformation: { width: 132, height: 34 }, // pequeño, proporción 520:134
          altText: { title: "NSS", description: "Logo NSS", name: "LogoNSS" },
        }),
      ],
    }),
  ],
});

// ...luego, en la sección:
sections: [{
  properties: {
    page: {
      size: { width: 12240, height: 15840 },
      margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }, // respeta márgenes
    },
  },
  headers: { default: nssHeader },
  children: [ /* contenido */ ],
}]
```

**Estilos base en docx-js (Arial 11, negro, interlineado 1,5):**

```javascript
const doc = new Document({
  styles: {
    default: {
      document: {
        run: { font: "Arial", size: 22, color: "000000" }, // Arial 11pt negro
        paragraph: { spacing: { line: 360, lineRule: "auto" } }, // interlineado 1,5
      },
    },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { font: "Arial", size: 28, bold: true, color: "000000" },
        paragraph: { spacing: { before: 240, after: 160, line: 360, lineRule: "auto" }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { font: "Arial", size: 24, bold: true, color: "000000" },
        paragraph: { spacing: { before: 200, after: 120, line: 360, lineRule: "auto" }, outlineLevel: 1 } },
    ],
  },
  // ...
});
```

- Encabezado: el logo NSS es obligatorio; puede acompañarse del nombre de la firma si el usuario lo proporciona, pero el logo nunca se omite.

### Checklist antes de entregar

Antes de guardar el archivo final, verificar mentalmente:

1. ¿Todos los campos variables están completos o marcados con [COMPLETAR]?
2. ¿Las referencias legales son correctas y vigentes? Si hay duda: [VERIFICAR CITA]
3. ¿El documento es comprensible para un cliente no-abogado?
4. ¿La estructura sigue el estándar del tipo de documento?
5. ¿El formato .docx cumple las reglas obligatorias: **Arial 11, color negro, interlineado 1,5 y logo NSS en la esquina superior izquierda respetando márgenes**?
6. ¿El formato .docx cumple con las especificaciones del skill docx?

## Ejemplo de uso

**Prompt del usuario:** "Necesito crear los estatutos de una SpA con dos accionistas, capital de 10 millones, administrada por un directorio de 3 miembros."

**Proceso:**
1. Leer el skill docx (`/mnt/skills/public/docx/SKILL.md`)
2. Generar el .docx siguiendo la estructura de estatutos SpA, con Arial 11 negro, interlineado 1,5 y el logo NSS en la esquina superior izquierda
3. Usar lenguaje jurídico accesible
4. Citar arts. 424 y ss. del Código de Comercio donde corresponda
5. Marcar datos faltantes con [COMPLETAR] (ej: nombres, RUT, domicilio)
6. Validar con `python scripts/office/validate.py`
7. Copiar a `/mnt/user-data/outputs/`
