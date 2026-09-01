@echo off
TITLE Lanzador Dashboard SLA - Mesa de Ayuda
COLOR 0A

:: 1. Posicionarse en el directorio actual donde reside el script
cd /d "%~dp0"

echo [INICIO] Verificando entorno de ejecucion...

:: 2. Verificar si el entorno virtual ya existe
IF NOT EXIST "venv\Scripts\activate.bat" (
    echo [INFO] Primera ejecucion detectada. Construyendo entorno virtual local...
    python -m venv venv
    IF %ERRORLEVEL% NEQ 0 (
        echo [ERROR] Fallo al crear venv. Asegurate de que Python esta instalado y en el PATH.
        pause
        exit /b %ERRORLEVEL%
    )
    
    echo [INFO] Entorno virtual creado.
    echo [INFO] Instalando dependencias desde requirements.txt. Esto tomara unos minutos...
    call venv\Scripts\activate.bat
    pip install --upgrade pip -q
    pip install -r requirements.txt -q
    echo [INFO] Dependencias instaladas correctamente.
) ELSE (
    echo [INFO] Entorno virtual detectado. Activando...
    call venv\Scripts\activate.bat
)

:: 3. Levantar el servidor de Streamlit de forma local
echo [INFO] Iniciando motor ETL y servidor web...
streamlit run app.py

pause