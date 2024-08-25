@echo off
setlocal

set "FFMPEG_URL=https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z"
set "FFMPEG_ZIP=%TEMP%\ffmpeg-release-full.7z"
set "FFMPEG_EXTRACT_DIR=%TEMP%\ffmpeg"
set "FFMPEG_BIN_DIR=%FFMPEG_EXTRACT_DIR%\ffmpeg-*\bin"

echo Downloading FFmpeg...
powershell -Command "Invoke-WebRequest -Uri '%FFMPEG_URL%' -OutFile '%FFMPEG_ZIP%'"

if not exist "%FFMPEG_EXTRACT_DIR%" mkdir "%FFMPEG_EXTRACT_DIR%"

echo Extracting FFmpeg...
"C:\Program Files\7-Zip\7z.exe" x "%FFMPEG_ZIP%" -o"%FFMPEG_EXTRACT_DIR%" -y

rem Find the actual bin directory
for /d %%D in ("%FFMPEG_BIN_DIR%") do set "FFMPEG_BIN_PATH=%%D"

if not defined FFMPEG_BIN_PATH (
    echo Failed to find FFmpeg bin directory.
    exit /b 1
)

rem Add FFmpeg to PATH
set "PATH=%PATH%;%FFMPEG_BIN_PATH%"

rem Clean up
del "%FFMPEG_ZIP%"

echo FFmpeg installation completed. Please restart your Command Prompt or PowerShell to use FFmpeg.

endlocal
pause
