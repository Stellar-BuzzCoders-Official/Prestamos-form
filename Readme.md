# Flask Loan Request Application

## Descripción

Este proyecto es una aplicación web simple construida con Flask que permite a los usuarios enviar solicitudes de préstamos y adelantos. La aplicación maneja solicitudes `GET` y `POST` para mostrar un formulario y procesar la información enviada.

## Estructura del Proyecto

El proyecto está estructurado de la siguiente manera:

```bash
  loan_app/
  │
  ├── app.py
  ├── templates/
  │   └── form.html
  ├── static/
  │   └── style.css
  └── __init__.py
```

- **`/templates`**: Contiene los archivos HTML para las plantillas.
  - **`form.html`**: Plantilla para el formulario de solicitud de préstamos y adelantos.
  - **`future_form.html`**: Plantilla para futuros formularios o funcionalidades.

- **`/static`**: Contiene archivos estáticos como CSS.
  - **`style.css`**: Archivo CSS para los estilos de la aplicación.

- **`app.py`**: Archivo principal de la aplicación Flask que maneja las rutas y la lógica del servidor.

- **`README.md`**: Este archivo.

## Instalación
### Crea un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
```

### Activa el entorno virtual:

#### En Windows
```bash
venv\Scripts\activate
```

#### En macOS/Linux
```bash
source venv/bin/activate
```
Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución
Inicia la aplicación Flask:

```bash
python app.py
```

Abre un navegador web y visita:

`http://127.0.0.1:5000/`
