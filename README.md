# 📝 ToDo List App (Django + Tailwind CSS)

¡Bienvenido al repositorio de tu aplicación de lista de tareas! Este proyecto está construido con **Django** para el *backend* y un *frontend* moderno utilizando **Tailwind CSS** y herramientas de desarrollo como **npm/Vite**.

---

## 🚀 Instalación y Puesta en Marcha

Para que la aplicación corra en tu máquina, debes levantar el **Backend** y el **Frontend** en terminales separadas.

### 1. ⚙️ Requisitos Previos

Asegúrate de tener instalado lo siguiente:

* **Python 3.x**
* **pip** (Administrador de paquetes de Python)
* **Node.js y npm** (Necesario para el *frontend*)

### 2. Instalación del Backend (Django)

Este proceso configura el entorno de Python y todas las dependencias de Django.

1.  **Navega a la carpeta raíz del proyecto** (`todolist_project`):

    ```bash
    cd todolist_project
    ```

2.  **Instala las dependencias de Python:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Ejecuta las migraciones de la base de datos:**

    ```bash
    python manage.py migrate
    ```

4.  **Inicia el servidor de desarrollo de Django:**

    ```bash
    python manage.py runserver
    ```
    El *backend* estará corriendo en `http://127.0.0.1:8000/`. Déjalo abierto en esta terminal.

---

## 3. Instalación y Ejecución del Frontend (Tailwind/npm)

El *frontend* maneja los estilos, la compilación de CSS y los scripts.

1.  **Abre una SEGUNDA terminal** y navega a la carpeta del *frontend*:

    ```bash
    cd frontend
    ```

2.  **Instala las dependencias de Node.js:**

    ```bash
    npm install
    ```

3.  **Inicia el modo de desarrollo (Vite):**
    
    Esto arrancará el servidor de *assets* y vigilará los cambios de Tailwind CSS y JavaScript.

    ```bash
    npm run dev
    ```
    
    **¡Listo!** El frontend ahora se comunicará con el backend de Django, y podrás acceder a la aplicación en `http://127.0.0.1:8000/`.

---

## 📝 Uso de la Aplicación

* **Crear Tarea:** Utiliza el botón "+ Añadir Nueva Tarea".
* **Marcar como Completada:** Usa el *checkbox* al inicio de cada tarjeta.
* **Edición Bloqueada:** Las tareas marcadas como Completadas **no se pueden editar**, asegurando la integridad de los datos. Si intentas editar una, verás una notificación de SweetAlert (Toast).

---

## 🛠 Estructura del Proyecto

* `todolist_project/`: Configuración principal de Django.
* `todos/`: Aplicación principal de Django que contiene los modelos, vistas y formularios.
* `frontend/`: Contiene todos los archivos de configuración y desarrollo de *assets* (Tailwind CSS, JavaScript).
    * `package.json`: Definiciones de npm y scripts.
    * `src/`: Archivos fuente de CSS/JS.
* `requirements.txt`: Dependencias de Python.
