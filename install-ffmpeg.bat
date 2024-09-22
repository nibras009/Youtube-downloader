@echo off
setlocal

REM Define the URL for the FFmpeg binary
set "FFMPEG_URL=https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip"
set "FFMPEG_ZIP=ffmpeg-latest-win64.zip"
set "FFMPEG_DIR=ffmpeg"
set "FFMPEG_BIN_DIR=%CD%\%FFMPEG_DIR%\bin"

REM Download FFmpeg
echo Downloading FFmpeg...
powershell -Command "Invoke-WebRequest -Uri %FFMPEG_URL% -OutFile %FFMPEG_ZIP%"

REM Check if download was successful
if not exist %FFMPEG_ZIP% (
    echo Failed to download FFmpeg. Exiting.
    pause
    exit /b 1
)

REM Create directory for FFmpeg
echo Creating directory for FFmpeg...
mkdir %FFMPEG_DIR%

REM Extract FFmpeg ZIP file
echo Extracting FFmpeg...
powershell -Command "Expand-Archive -Path %FFMPEG_ZIP% -DestinationPath %FFMPEG_DIR%"

REM Check if extraction was successful
if not exist %FFMPEG_BIN_DIR%\ffmpeg.exe (
    echo Failed to extract FFmpeg. Exiting.
    pause
    exit /b 1
)

REM Add FFmpeg to the system PATH
echo Adding FFmpeg to the system PATH...
setx PATH "%PATH%;%FFMPEG_BIN_DIR%"
if errorlevel 1 (
    echo Error adding FFmpeg to PATH. Exiting.
    pause
    exit /b 1
)

REM Clean up
echo Cleaning up...
del %FFMPEG_ZIP%

REM Verify FFmpeg installation
echo Verifying FFmpeg installation...
ffmpeg -version
if errorlevel 1 (
    echo Error verifying FFmpeg installation. Exiting.
    pause
    exit /b 1
)

echo Done. FFmpeg has been downloaded, extracted, and added to the PATH.
pause
@echo off
setlocal

REM Define the URL for the FFmpeg binary
set "FFMPEG_URL=https://github.com/BtbN/FFmpeg-Builds/releases/download/autobuilds/ffmpeg-n4.4.1-56-gce9d1fba60-win64-gpl-shared.zip"
set "FFMPEG_ZIP=ffmpeg-latest-win64.zip"
set "FFMPEG_DIR=ffmpeg"
set "FFMPEG_BIN_DIR=%CD%\%FFMPEG_DIR%\bin"

REM Download FFmpeg
echo Downloading FFmpeg...
powershell -Command "Invoke-WebRequest -Uri %FFMPEG_URL% -OutFile %FFMPEG_ZIP%"

REM Check if download was successful
if not exist %FFMPEG_ZIP% (
    echo Failed to download FFmpeg. Exiting.
    pause
    exit /b 1
)

REM Create directory for FFmpeg
echo Creating directory for FFmpeg...
mkdir %FFMPEG_DIR%

REM Extract FFmpeg ZIP file
echo Extracting FFmpeg...
powershell -Command "Expand-Archive -Path %FFMPEG_ZIP% -DestinationPath %FFMPEG_DIR%"

REM Check if extraction was successful
if not exist %FFMPEG_BIN_DIR%\ffmpeg.exe (
    echo Failed to extract FFmpeg. Exiting.
    pause
    exit /b 1
)

REM Add FFmpeg to the system PATH
echo Adding FFmpeg to the system PATH...
setx PATH "%PATH%;%FFMPEG_BIN_DIR%"
if errorlevel 1 (
    echo Error adding FFmpeg to PATH. Exiting.
    pause
    exit /b 1
)

REM Clean up
echo Cleaning up...
del %FFMPEG_ZIP%

REM Verify FFmpeg installation
echo Verifying FFmpeg installation...
ffmpeg -version
if errorlevel 1 (
    echo Error verifying FFmpeg installation. Exiting.
    pause
    exit /b 1
)

echo Done. FFmpeg has been downloaded, extracted, and added to the PATH.
pause
!!!