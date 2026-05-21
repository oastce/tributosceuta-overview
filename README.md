# 🚀 Ceuta Hub Tecnológico - Ventajas Fiscales para Inversores

Este proyecto transforma una presentación ejecutiva tradicional en una página web interactiva, moderna y de alto impacto visual, diseñada específicamente para captar la atención de inversores nacionales e internacionales interesados en el ecosistema tecnológico de Ceuta.

---

## 📁 Estructura Actualizada del Proyecto

El proyecto está organizado de forma óptima para su rápido renderizado y despliegue en plataformas como **GitHub Pages**:

*   📄 **`index.html`**: Archivo principal unificado que contiene la estructura HTML5 de las 13 diapositivas interactivas, los estilos CSS premium (efectos de glassmorphism, tipografías y transiciones) y la lógica JavaScript de control e interactividad. **Tamaño optimizado: ~226 KB**.
*   📁 **`images/`**: Carpeta que contiene las imágenes de fondo de las diapositivas de forma independiente para optimizar la descarga y permitir el almacenamiento en caché del navegador.
    *   `1&13.jpg`: Fondo para diapositivas de Inicio y Contacto.
    *   `2.jpg` a `11.jpg`, `12.webp`: Fondos para cada sección temática específica.
*   📄 **`index.html.bak`**: Copia de seguridad del archivo original con las imágenes incrustadas en base64 (~7.1 MB) para fines de depuración o archivo.

---

## ⚡ Optimización del Rendimiento (Web Performance)

Inicialmente, el archivo `index.html` pesaba **7.1 MB** debido a que contenía las 12 imágenes del fondo codificadas en Base64 en el propio código fuente. Se ha realizado una optimización estructural importante:
1. **Extracción a Binario:** Se extrajeron los datos en base64 de vuelta a sus formatos originales (`.jpg`, `.jpeg`, `.webp`) y se colocaron en el directorio `/images`.
2. **Referenciación Externa:** Se cambiaron los estilos CSS del archivo HTML para cargar las imágenes mediante rutas relativas (`url('images/...')`).
3. **Resultado:**
   *   El peso del HTML disminuyó de **7.12 MB a 226 KB** (un **96.8% de reducción**).
   *   El navegador ahora descarga el HTML instantáneamente y carga las imágenes en paralelo.
   *   Se aprovecha al máximo la caché del navegador para visitas sucesivas y la distribución a través de la CDN de **GitHub Pages**.

---

## 🌟 Características Destacadas y Elementos Interactivos

### 1. Modos de Visualización Dual
*   **Modo Presentación (Deck View):** Navegación fluida tipo diapositivas a pantalla completa con efectos de transición premium, barra de progreso y navegación mediante teclado.
*   **Modo Documento (Scroll View):** Transforma la presentación en una landing page continua de lectura vertical, ideal para lecturas rápidas o impresión.

### 2. Navegación Avanzada
*   **Controles de teclado:** Permite avanzar o retroceder con las flechas del teclado (`←` / `→` / `↑` / `↓`), la tecla `Espacio` o `Re Pág` / `Av Pág`.
*   **Navegación lateral por puntos (Dots):** Panel interactivo flotante a la derecha con Tooltips informativos de cada diapositiva.
*   **Controlador inferior:** Indicador numérico de progreso (`1 / 13`) y barra de progreso fluida.

### 3. Calculadora Fiscal Interactiva (Diapositiva 7)
Un simulador dinámico que permite a los inversores ingresar su facturación anual y elegir el tipo de IPSI tecnológico (0.5% o 4.0%) para ver en tiempo real el ahorro fiscal neto comparado con el 21% de IVA de la península, acompañado de gráficos visuales del ahorro porcentual.

### 4. Gráfico de Comparación Salarial (Diapositiva 8)
Visualización interactiva que demuestra gráficamente el beneficio de la deducción del 60% en el IRPF en Ceuta, comparando el salario neto final de un trabajador en Ceuta frente al de la Península.

### 5. Diagrama de Conectividad (Diapositiva 4)
Visualización interactiva de rutas y tiempos medios de tránsito en Helicóptero y Ferry entre Málaga, Algeciras y Ceuta.

---

## 💻 Cómo Ejecutar Localmente

Al no tener dependencias de backend complejos, puedes visualizar la página directamente de dos maneras:

### Opción 1: Servidor Local (Recomendado)
Para evitar problemas con políticas de CORS del navegador al cargar ciertos recursos, inicia un servidor estático rápido:

**Con Python:**
```bash
python3 -m http.server 8000
```
Luego abre en tu navegador: **[http://localhost:8000](http://localhost:8000)**

**Con Node.js (npx):**
```bash
npx serve
```

### Opción 2: Apertura Directa
Simplemente haz doble clic sobre el archivo **`index.html`** para abrirlo en tu navegador predeterminado de manera local.

---

## 🌐 Despliegue en GitHub Pages

Este repositorio está configurado para desplegarse de manera automática en **GitHub Pages**. Para subir cambios, utiliza:

```bash
git add .
git commit -m "Optimización de carga y actualización de README"
git push
```

El sitio estará disponible públicamente en la URL de GitHub Pages asociada a la organización/usuario (por ejemplo, `https://adminSTC.github.io/ceuta-overview/`).
