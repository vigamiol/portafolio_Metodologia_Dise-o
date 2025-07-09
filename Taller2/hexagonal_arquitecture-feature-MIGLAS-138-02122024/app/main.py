from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from adapters.handlers.pago_handlers import router as pago_router

# Crear la aplicación FastAPI
app = FastAPI(
    title="PayTrack API",
    description="Sistema de registro, gestión y consulta de pagos realizados por clientes",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS para permitir acceso desde el navegador
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar dominios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir las rutas de pagos
app.include_router(pago_router)

# Ruta de salud
@app.get("/", tags=["health"])
async def health_check():
    """Endpoint de verificación de salud"""
    return {
        "status": "ok",
        "message": "PayTrack API está funcionando correctamente",
        "version": "1.0.0"
    }

@app.get("/health", tags=["health"])
async def detailed_health():
    """Endpoint detallado de salud"""
    return {
        "status": "healthy",
        "service": "PayTrack",
        "version": "1.0.0",
        "description": "Sistema de gestión de pagos con arquitectura hexagonal"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
