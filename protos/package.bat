@echo off
setlocal enabledelayedexpansion

:: Get the current Git SHA
for /f %%A in ('git rev-parse --short HEAD') do set "git_sha=%%A"

:: If the git SHA contains only numbers, use the long SHA
set "only_numbers=true"
for /f "delims=0123456789" %%i in ("%git_sha%") do (
    if not "%%i"=="" set "only_numbers=false"
)
if "%only_numbers%"=="true" (
    for /f %%A in ('git rev-parse HEAD') do set "git_sha=%%A"
)

:: Get the current date and time
set version_date=%date:~10,4%.%date:~4,2%.%date:~7,2%

:: Run the dotnet pack command with the updated Version parameter
REM dotnet clean 
REM dotnet build
dotnet pack -c Release -p:Version=!version_date!-!git_sha! -o c:\DTS\Source\api-client\ApiClient\Libs\

endlocal