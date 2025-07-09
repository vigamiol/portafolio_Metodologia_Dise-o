# PayTrack - Sistema de Gestión de Pagos

Sistema para el registro, gestión y consulta de pagos realizados por clientes, implementado con arquitectura hexagonal.

## Características

- **Arquitectura Hexagonal**: Separación clara entre dominio, casos de uso y adaptadores
- **API REST**: Interfaz HTTP con FastAPI
- **Documentación automática**: Swagger UI y ReDoc
- **Validaciones de negocio**: Implementadas en el dominio
- **Repositorio en memoria**: Para demostración (fácilmente extensible a bases de datos)

## Requisitos Funcionales Implementados

### RF1. Registrar un Pago
- **Endpoint**: `POST /api/pagos/`
- **Entradas**: `nombre_cliente`, `monto`
- **Validaciones**: Monto > 0, nombre requerido
- **Respuesta**: HTTP 201 con datos del pago

### RF2. Listar todos los Pagos
- **Endpoint**: `GET /api/pagos/`
- **Respuesta**: HTTP 200 con lista de pagos

### RF3. Buscar Pagos por Cliente
- **Endpoint**: `GET /api/pagos/cliente/{nombre_cliente}`
- **Respuesta**: HTTP 200 con pagos del cliente

### RF4. Eliminar un Pago
- **Endpoint**: `DELETE /api/pagos/{id}`
- **Validación**: Solo si estado = "COMPLETADO"
- **Respuesta**: HTTP 204 si exitoso

## Instalación y Ejecución

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Ejecutar la aplicación

#### ⭐ Método recomendado (Windows):
```bash
# Abrir terminal en el directorio del proyecto y ejecutar:
cd app
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

#### Alternativa con script:
```bash
python start.py
```

### 3. Acceder a la aplicación
- **API**: http://localhost:8000
- **Frontend Web**: Abrir `frontend.html` en su navegador
- **Documentación Swagger**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

### 4. Usar la aplicación
1. Ejecute el servidor usando uno de los métodos anteriores
2. Abra `frontend.html` en su navegador web
3. Use la interfaz gráfica para probar todas las funcionalidades
4. O visite http://localhost:8000/docs para usar Swagger UI

### 5. Ejecutar tests
```bash
cd app
pytest test/
```

## Estructura del Proyecto

```
app/
├── core/                    # Núcleo del dominio
│   ├── entities/           # Entidades del dominio
│   └── ports/              # Interfaces (puertos)
├── usecases/               # Casos de uso (lógica de aplicación)
├── adapters/               # Adaptadores (implementaciones)
│   ├── repositories/       # Repositorios
│   ├── handlers/           # Controladores HTTP
│   ├── schemas/            # Esquemas de datos
│   └── dependency/         # Inyección de dependencias
main.py                     # Punto de entrada de la aplicación
```

## Ejemplos de Uso

### Registrar un pago
```bash
curl -X POST "http://localhost:8000/api/pagos/" \
     -H "Content-Type: application/json" \
     -d '{"nombre_cliente": "Juan Pérez", "monto": 150.00}'
```

### Listar todos los pagos
```bash
curl -X GET "http://localhost:8000/api/pagos/"
```

### Buscar pagos por cliente
```bash
curl -X GET "http://localhost:8000/api/pagos/cliente/Juan%20Pérez"
```

### Eliminar un pago
```bash
curl -X DELETE "http://localhost:8000/api/pagos/{id}"
```

## Arquitectura Hexagonal

### Dominio (Core)
- **Entidades**: `Pago` con reglas de negocio
- **Puertos**: Interfaces para repositorios

### Casos de Uso
- Lógica de aplicación independiente de tecnología
- Orquestación de entidades y repositorios

### Adaptadores
- **Repositorio**: Implementación en memoria
- **Handlers**: Controladores HTTP con FastAPI
- **Schemas**: Validación y serialización con Pydantic

## Extensibilidad

El diseño permite agregar fácilmente:
- Nuevas interfaces (CLI, gRPC, GraphQL)
- Diferentes repositorios (PostgreSQL, MongoDB)
- Nuevos casos de uso
- Middleware adicional
- Autenticación y autorización
