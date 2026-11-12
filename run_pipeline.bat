@echo off
REM NYC Taxi Capstone Pipeline Launcher

cd /d "%~dp0"

echo ================================================
echo   NYC Taxi Capstone - Starting ETL Pipeline
echo ================================================

if exist "myenv\Scripts\activate.bat" (
    call "myenv\Scripts\activate.bat"
)

python -m pipeline.pipeline

echo.
echo ================================================
echo   Pipeline finished. Check logs\ for details.
echo ================================================
pause