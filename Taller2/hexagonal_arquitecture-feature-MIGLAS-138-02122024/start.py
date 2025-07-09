#!/usr/bin/env python3
"""
Script de inicio para PayTrack API
Ejecuta el servidor FastAPI con la configuración correcta
"""

import sys
import os
import subprocess

def main():
    # Obtener el directorio actual
    current_dir = os.path.dirname(os.path.abspath(__file__))
    app_dir = os.path.join(current_dir, 'app')
    
    # Verificar que existe la carpeta app
    if not os.path.exists(app_dir):
        print("❌ Error: No se encontró la carpeta 'app'")
        return 1
    
    # Cambiar al directorio app
    os.chdir(app_dir)
    
    print("🚀 Iniciando PayTrack API...")
    print("📍 Servidor disponible en: http://localhost:8000")
    print("📚 Documentación en: http://localhost:8000/docs")
    print("🌐 Frontend: Abra frontend.html en su navegador")
    print("-" * 50)
    
    try:
        # Ejecutar uvicorn directamente
        subprocess.run([
            sys.executable, "-m", "uvicorn", "main:app",
            "--host", "0.0.0.0",
            "--port", "8000",
            "--reload"
        ], check=True)
    except KeyboardInterrupt:
        print("\n👋 Servidor detenido por el usuario")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al ejecutar el servidor: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
