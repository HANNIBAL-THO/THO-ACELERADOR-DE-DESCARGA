@echo off
REM 

REM 
if not exist assets mkdir assets

REM 
if not exist assets\logo.ico (
    echo Descargando icono...
    powershell -Command "Invoke-WebRequest -Uri 'https://github.com/yeuritho/assets/raw/main/logo.ico' -OutFile 'assets/logo.ico'"
    if not exist assets\logo.ico (
        echo No se pudo descargar logo.ico. Por favor, agrega un icono manualmente en assets\logo.ico
        pause
        exit /b
    )
)

REM 
if not exist assets\matrix.gif (
    echo Descargando GIF...
    powershell -Command "Invoke-WebRequest -Uri 'https://github.com/yeuritho/assets/raw/main/matrix.gif' -OutFile 'assets/matrix.gif'"
    if not exist assets\matrix.gif (
        echo No se pudo descargar matrix.gif. Por favor, agrega un GIF manualmente en assets\matrix.gif
        pause
        exit /b
    )
)

REM 
rmdir /s /q dist
rmdir /s /q build
del /q *.spec

REM 
pip install -r requeriments.txt

REM 
pyinstaller --noconfirm --onefile --windowed ^
  --icon=assets\logo.ico ^
  --add-data "assets;assets" ^
  --add-data "fondo_animado.py;." ^
  main.py

REM 
echo.
echo Compilación finalizada. El ejecutable está en la carpeta dist.
pause
