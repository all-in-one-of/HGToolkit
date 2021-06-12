@echo off

echo ---------------------------------------------------------------------------------
echo ------------------------- HGT Installer 1.0 -------------------------------------
echo ---------------------------------------------------------------------------------
echo.
echo Installing the Houdini Games Toolkit for all installed version of Houdini.

REM Set the base variables
set "CLONEPATH=%~dp0"
set "CLONEPATH=%CLONEPATH:\=/%"

for /f "tokens=*" %%G in ('dir /b /a:d "%UserProfile%\Documents\houdini*"') do ^
powershell -Command "(gc 'config\HGToolkit.template') -replace 'xxx', '%CLONEPATH%' | Out-File -Encoding ASCII  '%UserProfile%\Documents\%%G\packages\HGToolkit.json'"

echo.
echo Sucessfully installed for all found Versions of Houdini...
echo ---------------------------------------------------------------------------------
pause


