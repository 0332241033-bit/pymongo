# pymongo (FastAPI + MongoDB CRUD)

> API REST sencilla construida con **FastAPI** y **MongoDB (PyMongo)** que implementa operaciones **CRUD** sobre una colección de **usuarios**.


## Tabla de contenido

- [Resumen](#resumen)
- [Stack](#stack)
- [Arquitectura y estructura](#arquitectura-y-estructura)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Ejecución](#ejecución)
- [Endpoints (CRUD Usuarios)](#endpoints-crud-usuarios)
- [Modelo de datos](#modelo-de-datos)
- [Ejemplos rápidos (cURL)](#ejemplos-rápidos-curl)
- [Notas de seguridad](#notas-de-seguridad)
- [Mejoras recomendadas](#mejoras-recomendadas)
- [Licencia](#licencia)


## Resumen

Este repositorio contiene una API mínima para gestionar usuarios:

- Crear usuario
- Listar usuarios
- Obtener usuario por `id`
- Actualizar usuario
- Eliminar usuario

La aplicación expone rutas definidas con `APIRouter` y persiste datos en MongoDB usando `pymongo`.


## Stack

- **Python**
- **FastAPI** (API y documentación automática en Swagger/OpenAPI)
- **PyMongo** (cliente MongoDB)
- **Pydantic** (modelo de validación/entrada)


## Arquitectura y estructura

Estructura actual del proyecto:

```
.
├── index.py
├── config
│   └── db.py
├── models
│   └── user.py
├── routes
│   └── user.py
└── schemas
    └── user.py
```

### Flujo de ejecución

1. `index.py` crea la app de FastAPI e incluye el router de usuarios.
2. `config/db.py` crea la conexión a MongoDB vía `MongoClient`.
3. `routes/user.py` define los endpoints CRUD usando `conn.proyectodb.users`.
4. `models/user.py` define el esquema de entrada (Pydantic).
5. `schemas/user.py` convierte documentos MongoDB (incluyendo `ObjectId`) a JSON serializable.


## Requisitos

- Python 3.10+ (recomendado)
- MongoDB ejecutándose localmente o en un servidor accesible


## Instalación

> Nota: el repositorio no incluye `requirements.txt`/`pyproject.toml` por ahora. Abajo se muestran comandos sugeridos.

1) Crear y activar entorno virtual:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate
```

2) Instalar dependencias:

```bash
pip install fastapi uvicorn pymongo pydantic bson
```


## Configuración

La conexión a MongoDB está definida en `config/db.py`:

- URI: `mongodb://localhost:27017/`
- Base de datos: `proyectodb`
- Colección: `users`

Si quieres cambiar el host, puerto o usar credenciales, actualiza el URI en `config/db.py`.

### Variables de entorno (recomendado)

Para un entorno profesional, es recomendable mover el URI de conexión a una variable de entorno, por ejemplo:

- `MONGODB_URI=mongodb://localhost:27017/`


## Ejecución

Ejecuta el servidor con Uvicorn apuntando al objeto `app` dentro de `index.py`:

```bash
uvicorn index:app --reload
```

Luego abre:

- Documentación Swagger UI: `http://127.0.0.1:8000/docs`
- OpenAPI JSON: `http://127.0.0.1:8000/openapi.json`


## Endpoints (CRUD Usuarios)

Todas las rutas están definidas en `routes/user.py` y se montan en la raíz (`/`).

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/` | Listar todos los usuarios |
| GET | `/{id}` | Obtener un usuario por id (Mongo ObjectId) |
| POST | `/` | Crear un usuario |
| PUT | `/{id}` | Actualizar un usuario por id |
| DELETE | `/{id}` | Eliminar un usuario por id |


## Modelo de datos

El modelo Pydantic actual (`models/user.py`) espera:

```json
{
  "name": "string",
  "email": "string",
  "password": "string"
}
```

La API devuelve documentos con el `ObjectId` convertido a string en el campo `_id`/`id` según el serializador.


## Ejemplos rápidos (cURL)

### Crear usuario

```bash
curl -X POST http://127.0.0.1:8000/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Ada","email":"ada@example.com","password":"secret"}'
```

### Listar usuarios

```bash
curl http://127.0.0.1:8000/
```

### Obtener por id

```bash
curl http://127.0.0.1:8000/<object_id>
```

### Actualizar usuario

```bash
curl -X PUT http://127.0.0.1:8000/<object_id> \
  -H "Content-Type: application/json" \
  -d '{"name":"Ada Lovelace","email":"ada@example.com","password":"secret"}'
```

### Eliminar usuario

```bash
curl -X DELETE http://127.0.0.1:8000/<object_id>
```


## Notas de seguridad

Este proyecto es un ejemplo didáctico. En producción considera:

- **No almacenar contraseñas en texto plano**: usar hashing (p.ej. `bcrypt`).
- Validación y normalización de `email`.
- Manejo de errores (IDs inválidos, usuario no encontrado, etc.).
- Configurar CORS y rate limiting.
- Separar capas (routers, servicios, repositorios) y añadir pruebas.


## Mejoras recomendadas

Si quieres llevarlo a un nivel más profesional:

- Añadir `requirements.txt` o `pyproject.toml`
- Añadir `.env` + `python-dotenv` para configuración
- Añadir un prefijo de rutas (`/api/v1`)
- Respuestas con `response_model` y códigos HTTP apropiados
- Logging y manejo global de excepciones
- Docker (`Dockerfile` + `docker-compose.yml` con MongoDB)
- CI (GitHub Actions) y formateo (ruff/black)


## Licencia

Define una licencia (MIT/Apache-2.0) según tus necesidades.