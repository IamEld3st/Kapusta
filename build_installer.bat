@echo off
powershell -Command "Invoke-WebRequest https://github.com/tangalbert919/ungoogled-chromium-binaries/releases/download/87.0.4280.141-1/ungoogled-chromium_87.0.4280.141-1.1_windows-x64.zip -OutFile chrome_win.zip"
powershell -Command "Expand-Archive -Force chrome_win.zip ."
cd src
pyinstaller -n Kapusta --add-data kapusta_gui;kapusta_gui --hidden-import eel --collect-submodules kapusta_math --distpath ..\dist --icon=..\icon.ico --noconsole main.py
cd ..
move ungoogled-* dist\Kapusta\chromium
copy icon.ico dist\icon.ico
"C:\Program Files (x86)\NSIS\Bin\makensis.exe" /X"SetCompressor /FINAL lzma" installer.nsi
rd /S /Q dist
rd /S /Q src\build
del /Q src\Kapusta.spec
del /Q chrome_win.zip
pause
