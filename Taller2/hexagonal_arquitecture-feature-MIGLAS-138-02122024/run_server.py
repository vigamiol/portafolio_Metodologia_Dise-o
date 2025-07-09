import sys
import os

# Agregar la carpeta app al path de Python
app_path = os.path.join(os.path.dirname(__file__), 'app')
sys.path.insert(0, app_path)

# Cambiar al directorio app
os.chdir(app_path)

# Importar y ejecutar la aplicación
from main import app
import uvicorn

if __name__ == "__main__":
    print("🚀 Iniciando PayTrack API...")
    print("📍 Servidor disponible en: http://localhost:8000")
    print("📚 Documentación en: http://localhost:8000/docs")
    print("🌐 Frontend: Abra frontend.html en su navegador")
    print("-" * 50)
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
