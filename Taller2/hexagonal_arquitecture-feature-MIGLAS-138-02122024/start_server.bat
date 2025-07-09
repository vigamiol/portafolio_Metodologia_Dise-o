@echo off
echo 🚀 Iniciando PayTrack API...
echo 📍 Servidor disponible en: http://localhost:8000
echo 📚 Documentación en: http://localhost:8000/docs
echo 🌐 Frontend: Abra frontend.html en su navegador
echo --------------------------------------------------
cd app
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
pause
