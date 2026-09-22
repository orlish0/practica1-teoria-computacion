# Ejercicio 1. Entorno de trabajo: control de versiones y contenedores

## Parte A. Investigación

### 1. Sistema de Control de Versiones (VCS)
Un sistema de control de versiones (VCS, por sus siglas en inglés) es una herramienta de software diseñada para registrar los cambios realizados sobre un conjunto de archivos a lo largo del tiempo, permitiendo recuperar versiones específicas en el futuro, auditar modificaciones y coordinar el trabajo colaborativo.

En el trabajo en equipo, resuelve los problemas clásicos de concurrencia:
- **Sobrescritura accidental:** Evita que un miembro del equipo borre el trabajo de otro al guardar simultáneamente el mismo archivo.
- **Pérdida de trazabilidad:** Identifica con precisión qué usuario introdujo una línea de código, en qué fecha y bajo qué justificación.
- **Desincronización de versiones:** Elimina la necesidad de intercambiar archivos comprimidos o copias duplicadas (por ejemplo, `proyecto_final_v2_modificado.zip`), centralizando el historial en un flujo ordenado y verificable.

---

### 2. Diferencia entre Git y GitHub
- **Git:** Es el software local y motor de control de versiones distribuido. Se ejecuta directamente en la máquina del desarrollador a través de la terminal o interfaz local; gestiona el historial, las ramas y los registros criptográficos (hashes SHA) sin necesidad obligatoria de conexión a Internet.
- **GitHub:** Es una plataforma en la nube (servicio de alojamiento remoto) que utiliza Git como base. Ofrece herramientas de colaboración en red, como almacenamiento remoto de repositorios, gestión de ramas protegidas, interfaces para Pull Requests, revisión de código en equipo, seguimiento de incidencias (Issues) y automatización de flujos de trabajo (CI/CD).

En resumen: Git es la herramienta que gestiona los cambios localmente; GitHub es el servicio remoto que facilita compartir y colaborar sobre esos cambios.

---

### 3. Conceptos fundamentales de Git
- **Repositorio (Repository):** Espacio digital donde se almacenan todos los archivos de un proyecto junto con su historial completo de modificaciones organizadas cronológicamente.
  - *Ejemplo:* La carpeta `practica1-tc/` que contiene el directorio oculto `.git/`.
- **Confirmación (Commit):** Una instantánea inmutable del estado del proyecto en un momento dado, acompañada de un mensaje explicativo y un identificador único (hash).
  - *Ejemplo:* Confirmar un avance con `git commit -m "feat: implementar funciones de prefijos"`.
- **Rama (Branch):** Una línea de desarrollo independiente que permite trabajar en nuevas funcionalidades, correcciones o pruebas sin alterar la línea principal (`main`).
  - *Ejemplo:* Crear la rama `feature/entorno-docs` para redactar la documentación sin interferir con el código estable.
- **Fusión (Merge):** La acción de integrar el historial y los cambios de una rama secundaria dentro de otra rama de destino.
  - *Ejemplo:* Incorporar los cambios de `feature/entorno-docs` dentro de `main`.
- **Conflicto de fusión (Merge Conflict):** Ocurre cuando dos ramas modifican las mismas líneas de un archivo de manera incompatible y Git no puede resolver automáticamente cuál versión conservar, requiriendo intervención manual.
  - *Ejemplo:* Si dos desarrolladores cambian de forma distinta el título en la línea 1 de `README.md` simultáneamente.
- **Pull Request (PR):** Una solicitud formal en una plataforma como GitHub para que las confirmaciones realizadas en una rama sean revisadas y fusionadas en otra, sirviendo como filtro de calidad y revisión por pares.
  - *Ejemplo:* Abrir un PR en GitHub para fusionar la rama de pruebas hacia la rama principal tras validar los resultados.
- **Archivo `.gitignore`:** Archivo de texto plano que especifica patrones de nombres de archivos y directorios que Git debe omitir deliberadamente del seguimiento de versiones.
  - *Ejemplo:* Incluir `venv/` y `__pycache__/` para evitar subir entornos locales o archivos compilados.
- **Archivo `README`:** Documento de entrada (comúnmente en formato Markdown) que describe el propósito del proyecto, instrucciones de instalación, dependencias y datos de autoría.
  - *Ejemplo:* El archivo `README.md` en la raíz con la carátula de la práctica y los datos del estudiante.

---

### 4. Contenedores vs. Máquinas Virtuales
Un contenedor es una unidad de software estandarizada que empaqueta el código y todas sus dependencias para que la aplicación se ejecute de manera rápida y confiable en cualquier entorno.

| Criterio | Máquina Virtual (VM) | Contenedor (Docker/Podman) |
| :--- | :--- | :--- |
| **Aislamiento** | Aislamiento completo por hardware. Cada VM incluye un sistema operativo huésped completo sobre un hipervisor. | Aislamiento a nivel de sistema operativo (espacios de nombres y cgroups del kernel del host). |
| **Arranque** | Lento; requiere varios segundos o minutos para inicializar el kernel huésped y servicios del SO. | Casi instantáneo (fracciones de segundo o pocos segundos); solo inicializa el proceso aislado. |
| **Tamaño** | Pesado; requiere varios gigabytes por imagen de disco debido al sistema operativo completo. | Ligero; las imágenes base optimizadas (como Alpine o Debian slim) ocupan desde unas decenas hasta pocos cientos de megabytes. |

---

### 5. Términos de Contenedores
- **Imagen:** Una plantilla de solo lectura que contiene las instrucciones, el sistema base, las dependencias y el código necesario para ejecutar una aplicación.
- **Contenedor:** Una instancia en ejecución de una imagen. Es el entorno aislado donde los procesos se ejecutan efectivamente.
- **Volumen:** Mecanismo de almacenamiento persistente administrado por el motor de contenedores que permite compartir o preservar datos entre el sistema anfitrión y el contenedor, o entre distintos contenedores, independientemente del ciclo de vida del contenedor.
- **Puerto publicado (Published Port):** Mapeo de red que vincula un puerto del equipo anfitrión (host) con un puerto interno del contenedor, permitiendo el tráfico entrante desde el exterior (por ejemplo, `8550:8550`).

---

### 6. Entornos Virtuales de Python
Un entorno virtual de Python (creado típicamente con `python -m venv`) es un directorio autónomo que contiene enlaces simbólicos al intérprete del sistema y un conjunto independiente de bibliotecas y paquetes instalados con `pip`.

**¿Por qué un entorno virtual no modifica la versión del intérprete?**
Porque el entorno virtual no instala un compilador o un núcleo de Python nuevo; únicamente crea una estructura de directorios con scripts de activación y un enlace simbólico (o copia superficial del ejecutable) que apunta directamente al intérprete de Python que se utilizó para crearlo. Por ende, la versión del motor de ejecución subyacente sigue siendo exactamente la misma que la del sistema anfitrión o contenedor base.

---

### 7. Fijación de Versión en Imágenes Base (`python:3.12-slim` vs. `python:latest`)
Conviene fijar la versión (`python:3.12-slim`) en lugar de emplear `python:latest` por las siguientes razones técnicas:
1. **Reproducibilidad y determinismo:** La etiqueta `latest` es mutable y cambia dinámicamente con el tiempo. Si se construye la imagen semanas o meses después, `latest` podría apuntar a una versión mayor posterior con cambios incompatibles (*breaking changes*) o bibliotecas deprecadas.
2. **Estabilidad del entorno:** Al fijar `3.12-slim`, se garantiza que todos los miembros del equipo, los entornos de prueba y los contenedores de producción ejecuten exactamente el mismo intérprete y dependencias de sistema.
3. **Eficiencia de recursos (`-slim`):** Las variantes `slim` contienen únicamente los paquetes indispensables para ejecutar Python sobre una base Debian mínima, reduciendo drásticamente la superficie de ataque y el peso de la imagen en comparación con las imágenes completas por defecto.
