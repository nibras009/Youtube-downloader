@echo off
setlocal

:: Define the URL for the latest FFmpeg release
set "FFMPEG_URL=https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z"
set "FFMPEG_ZIP=%TEMP%\ffmpeg-release-full.7z"
set "FFMPEG_EXTRACT_DIR=%ProgramFiles%\ffmpeg"

:: Download the FFmpeg archive
echo Downloading FFmpeg...
powershell -Command "Invoke-WebRequest -Uri '%FFMPEG_URL%' -OutFile '%FFMPEG_ZIP%'"

:: Create the directory for FFmpeg
if not exist "%FFMPEG_EXTRACT_DIR%" mkdir "%FFMPEG_EXTRACT_DIR%"

:: Extract the downloaded archive
echo Extracting FFmpeg...
"C:\Program Files\7-Zip\7z.exe" x "%FFMPEG_ZIP%" -o"%FFMPEG_EXTRACT_DIR%" -y

:: Add FFmpeg to the system PATH
set "FFMPEG_BIN_PATH=%FFMPEG_EXTRACT_DIR%\ffmpeg-*\bin"
set "PATH=%PATH%;%FFMPEG_BIN_PATH%"

:: Clean up the downloaded file
del "%FFMPEG_ZIP%"

echo FFmpeg installation completed. Please restart your Command Prompt or PowerShell to use FFmpeg.

endlocal
pause
