<div align="center">

# 🍃 PyMongo FastAPI CRUD

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-7.0%2B-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

**API REST completa con operaciones CRUD usando Python, FastAPI y MongoDB.**

[Características](#-características) · [Instalación](#-instalación) · [Uso](#-uso) · [API Reference](#-api-reference) · [Contribuir](#-contribuir)

</div>

---

## 📋 Tabla de Contenidos

- [Descripción](#-descripción)
- [Características](#-características)
- [Tecnologías](#-tecnologías)
- [Requisitos previos](#-requisitos-previos)
- [Instalación](#-instalación)
- [Configuración](#-configuración)
- [Uso](#-uso)
- [API Reference](#-api-reference)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Variables de entorno](#-variables-de-entorno)
- [Contribuir](#-contribuir)
- [Licencia](#-licencia)

---

## 📖 Descripción

**PyMongo FastAPI CRUD** es una API REST moderna y escalable que implementa las operaciones básicas de base de datos (**C**reate, **R**ead, **U**pdate, **D**elete) utilizando:

- 🐍 **Python** como lenguaje de programación principal
- ⚡ **FastAPI** como framework web de alto rendimiento
- 🍃 **MongoDB** como base de datos NoSQL
- 🔌 **PyMongo / Motor** como driver de conexión

---

## ✨ Características

| Característica | Descripción |
|----------------|-------------|
| ⚡ Alto rendimiento | FastAPI es uno de los frameworks más rápidos disponibles |
| 📝 Documentación automática | Swagger UI y ReDoc generados automáticamente |
| ✅ Validación de datos | Esquemas con Pydantic para validación robusta |
| 🔄 Operaciones CRUD | Create, Read, Update y Delete completos |
| 🌐 API REST | Endpoints siguiendo estándares REST |
| 🍃 MongoDB | Base de datos NoSQL flexible y escalable |
| 🔒 Manejo de errores | Respuestas HTTP consistentes y descriptivas |

---

## 🛠 Tecnologías

<div align="center">

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| [Python](https://www.python.org/) | 3.10+ | Lenguaje principal |
| [FastAPI](https://fastapi.tiangolo.com/) | 0.110+ | Framework web |
| [PyMongo](https://pymongo.readthedocs.io/) | 4.x | Driver MongoDB síncrono |
| [Motor](https://motor.readthedocs.io/) | 3.x | Driver MongoDB asíncrono |
| [Pydantic](https://docs.pydantic.dev/) | 2.x | Validación de datos |
| [Uvicorn](https://www.uvicorn.org/) | 0.29+ | Servidor ASGI |
| [MongoDB](https://www.mongodb.com/) | 7.0+ | Base de datos |

</div>

---

## 📦 Requisitos previos

Antes de comenzar, asegúrate de tener instalado:

- **Python** `>= 3.10` → [Descargar](https://www.python.org/downloads/)
- **MongoDB** `>= 7.0` → [Descargar](https://www.mongodb.com/try/download/community) o usar [MongoDB Atlas](https://www.mongodb.com/atlas)
- **pip** (incluido con Python)
- **Git** → [Descargar](https://git-scm.com/)

---

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/0332241033-bit/pymongo.git
cd pymongo
```

### 2. Crear y activar un entorno virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar en Linux / macOS
source venv/bin/activate

# Activar en Windows
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

> Si no existe `requirements.txt`, instala manualmente:
> ```bash
> pip install fastapi uvicorn pymongo motor pydantic python-dotenv
> ```

---

## ⚙️ Configuración

### Archivo `.env`

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

```env
# MongoDB
MONGO_URL=mongodb://localhost:27017
MONGO_DB_NAME=pymongo_db

# App
APP_HOST=0.0.0.0
APP_PORT=8000
APP_RELOAD=True
```

> **MongoDB Atlas:** Si usas MongoDB Atlas, reemplaza `MONGO_URL` con tu connection string:
> ```env
> MONGO_URL=mongodb+srv://<usuario>:<contraseña>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
> ```

---

## ▶️ Uso

### Iniciar el servidor de desarrollo

```bash
uvicorn main:app --reload
```

O con las variables del archivo `.env`:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Acceder a la documentación interactiva

Una vez iniciado el servidor, accede a:

| Interfaz | URL |
|----------|-----|
| 📚 **Swagger UI** | http://localhost:8000/docs |
| 📖 **ReDoc** | http://localhost:8000/redoc |
| 🔍 **OpenAPI JSON** | http://localhost:8000/openapi.json |

---

## 📡 API Reference

### Base URL

```
http://localhost:8000/api/v1
```

---

### 📌 Endpoints

#### ➕ Crear un documento — `POST /items`

Crea un nuevo documento en la base de datos.

**Request Body:**
```json
{
  "name": "Ejemplo",
  "description": "Descripción del item",
  "price": 29.99,
  "available": true
}
```

**Response `201 Created`:**
```json
{
  "id": "64f1a2b3c4d5e6f7a8b9c0d1",
  "name": "Ejemplo",
  "description": "Descripción del item",
  "price": 29.99,
  "available": true
}
```

---

#### 📋 Obtener todos los documentos — `GET /items`

Retorna la lista de todos los documentos.

**Query Parameters:**

| Parámetro | Tipo | Default | Descripción |
|-----------|------|---------|-------------|
| `skip` | `int` | `0` | Número de documentos a omitir |
| `limit` | `int` | `10` | Número máximo de documentos a retornar |

**Response `200 OK`:**
```json
[
  {
    "id": "64f1a2b3c4d5e6f7a8b9c0d1",
    "name": "Ejemplo",
    "description": "Descripción del item",
    "price": 29.99,
    "available": true
  }
]
```

---

#### 🔍 Obtener un documento por ID — `GET /items/{id}`

Retorna un documento específico por su `id`.

**Path Parameters:**

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `id` | `string` | ObjectId del documento en MongoDB |

**Response `200 OK`:**
```json
{
  "id": "64f1a2b3c4d5e6f7a8b9c0d1",
  "name": "Ejemplo",
  "description": "Descripción del item",
  "price": 29.99,
  "available": true
}
```

**Response `404 Not Found`:**
```json
{
  "detail": "Item no encontrado"
}
```

---

#### ✏️ Actualizar un documento — `PUT /items/{id}`

Actualiza un documento existente por su `id`.

**Path Parameters:**

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `id` | `string` | ObjectId del documento en MongoDB |

**Request Body:**
```json
{
  "name": "Ejemplo actualizado",
  "description": "Nueva descripción",
  "price": 49.99,
  "available": false
}
```

**Response `200 OK`:**
```json
{
  "id": "64f1a2b3c4d5e6f7a8b9c0d1",
  "name": "Ejemplo actualizado",
  "description": "Nueva descripción",
  "price": 49.99,
  "available": false
}
```

**Response `404 Not Found`:**
```json
{
  "detail": "Item no encontrado"
}
```

---

#### 🗑️ Eliminar un documento — `DELETE /items/{id}`

Elimina un documento de la base de datos por su `id`.

**Path Parameters:**

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `id` | `string` | ObjectId del documento en MongoDB |

**Response `200 OK`:**
```json
{
  "message": "Item eliminado correctamente"
}
```

**Response `404 Not Found`:**
```json
{
  "detail": "Item no encontrado"
}
```

---

### 📊 Códigos de respuesta HTTP

| Código | Significado |
|--------|-------------|
| `200` | ✅ OK — Operación exitosa |
| `201` | ✅ Created — Recurso creado |
| `400` | ❌ Bad Request — Solicitud inválida |
| `404` | ❌ Not Found — Recurso no encontrado |
| `422` | ❌ Unprocessable Entity — Error de validación |
| `500` | ❌ Internal Server Error — Error del servidor |

---

## 🗂 Estructura del proyecto

```
pymongo/
├── 📁 app/
│   ├── 📁 api/
│   │   ├── 📁 v1/
│   │   │   ├── endpoints/
│   │   │   │   └── items.py        # Endpoints CRUD
│   │   │   └── router.py           # Router principal v1
│   ├── 📁 core/
│   │   ├── config.py               # Configuración de la app
│   │   └── database.py             # Conexión a MongoDB
│   ├── 📁 models/
│   │   └── item.py                 # Modelos Pydantic
│   ├── 📁 schemas/
│   │   └── item.py                 # Esquemas de request/response
│   └── 📁 crud/
│       └── item.py                 # Lógica de acceso a datos
├── main.py                         # Punto de entrada de la app
├── requirements.txt                # Dependencias del proyecto
├── .env.example                    # Ejemplo de variables de entorno
├── .gitignore                      # Archivos ignorados por git
└── README.md                       # Documentación del proyecto
```

---

## 🔑 Variables de entorno

| Variable | Descripción | Valor por defecto |
|----------|-------------|-------------------|
| `MONGO_URL` | URL de conexión a MongoDB | `mongodb://localhost:27017` |
| `MONGO_DB_NAME` | Nombre de la base de datos | `pymongo_db` |
| `APP_HOST` | Host del servidor | `0.0.0.0` |
| `APP_PORT` | Puerto del servidor | `8000` |
| `APP_RELOAD` | Recarga automática en desarrollo | `True` |

---

## 🧪 Pruebas con curl

### Crear un item
```bash
curl -X POST "http://localhost:8000/api/v1/items" \
  -H "Content-Type: application/json" \
  -d '{"name": "Laptop", "description": "Laptop gaming", "price": 999.99, "available": true}'
```

### Obtener todos los items
```bash
curl -X GET "http://localhost:8000/api/v1/items"
```

### Obtener un item por ID
```bash
curl -X GET "http://localhost:8000/api/v1/items/64f1a2b3c4d5e6f7a8b9c0d1"
```

### Actualizar un item
```bash
curl -X PUT "http://localhost:8000/api/v1/items/64f1a2b3c4d5e6f7a8b9c0d1" \
  -H "Content-Type: application/json" \
  -d '{"name": "Laptop Pro", "description": "Laptop gaming actualizada", "price": 1199.99, "available": true}'
```

### Eliminar un item
```bash
curl -X DELETE "http://localhost:8000/api/v1/items/64f1a2b3c4d5e6f7a8b9c0d1"
```

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Sigue estos pasos:

1. **Fork** el repositorio
2. Crea una rama para tu feature:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Realiza tus cambios y haz **commit**:
   ```bash
   git commit -m "feat: agrega nueva funcionalidad"
   ```
4. Sube tus cambios:
   ```bash
   git push origin feature/nueva-funcionalidad
   ```
5. Abre un **Pull Request**

### Convenciones de commits

| Prefijo | Descripción |
|---------|-------------|
| `feat:` | Nueva característica |
| `fix:` | Corrección de bug |
| `docs:` | Cambios en documentación |
| `refactor:` | Refactorización de código |
| `test:` | Agregar o modificar tests |

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

<div align="center">

Hecho con ❤️ usando **Python**, **FastAPI** y **MongoDB**

⭐ ¡Dale una estrella al repositorio si te fue útil!

</div>
