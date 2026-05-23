# FODMAP Scanner 🌿

App móvil (PWA) para escanear códigos de barras y detectar FODMAPs en ingredientes.

## Cómo publicarla en GitHub Pages (gratis)

### Paso 1 — Crear cuenta en GitHub
1. Entrá a [github.com](https://github.com) y creá una cuenta si no tenés.

### Paso 2 — Crear un repositorio nuevo
1. Click en el botón verde **"New"** (o el ícono `+` arriba a la derecha → "New repository")
2. Nombre del repositorio: `fodmap-scanner`
3. Dejalo en **Public**
4. Click en **"Create repository"**

### Paso 3 — Subir los archivos
En la página del repositorio vacío vas a ver una sección que dice "uploading an existing file".
1. Click en **"uploading an existing file"**
2. Arrastrá o seleccioná **todos** estos archivos:
   - `index.html`
   - `manifest.json`
   - `sw.js`
   - La carpeta `icons/` con los dos PNG adentro
3. Click en **"Commit changes"**

### Paso 4 — Activar GitHub Pages
1. En tu repositorio, click en **Settings** (arriba a la derecha)
2. En el menú izquierdo, click en **Pages**
3. En "Source" seleccioná **"Deploy from a branch"**
4. En "Branch" seleccioná **main** y carpeta **/ (root)**
5. Click en **Save**

### Paso 5 — Esperar 2 minutos y abrir la app
- Tu app va a estar en: `https://TU-USUARIO.github.io/fodmap-scanner`
- Abrila desde el celu en Chrome (Android) o Safari (iPhone)

---

## Instalar en el celu como app

### Android (Chrome)
1. Abrí la URL en Chrome
2. Tocá el menú (⋮) → "Agregar a pantalla de inicio"
3. ¡Listo! Aparece como app nativa.

### iPhone (Safari)
1. Abrí la URL en Safari
2. Tocá el ícono de compartir (□↑) → "Agregar a inicio"
3. ¡Listo!

---

## Estructura de archivos

```
fodmap-scanner/
├── index.html       ← Toda la app (HTML + CSS + JS)
├── manifest.json    ← Configuración de la PWA
├── sw.js            ← Service worker (modo offline)
└── icons/
    ├── icon-192.png
    └── icon-512.png
```

## Personalizar el diseño

Todo el CSS está en el bloque `<style>` dentro de `index.html`.
Las variables principales están al principio:

```css
:root {
  --bg:      #0f1a12;   /* fondo principal */
  --accent:  #6dde8a;   /* verde principal */
  --danger:  #ff6b5b;   /* rojo (alto FODMAP) */
  --warn:    #f5c542;   /* amarillo (FODMAP moderado) */
  --safe:    #6dde8a;   /* verde (sin FODMAP) */
  --serif:   'DM Serif Display'; /* fuente títulos */
  --sans:    'DM Sans';          /* fuente general */
}
```

Cambiando esas variables podés cambiar toda la paleta de colores de la app.

---

## Cómo funciona

1. **Escaneo**: Usa la API `BarcodeDetector` del navegador (Chrome en Android, Edge)
2. **Búsqueda**: Consulta [Open Food Facts](https://world.openfoodfacts.org) — base de datos abierta con millones de productos incluyendo argentinos
3. **Fallback**: Si el producto no está, consulta a Claude via API
4. **Análisis**: Detecta FODMAPs en los ingredientes localmente (sin internet necesario)
