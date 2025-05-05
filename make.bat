@echo off
set version=0.1.0
set dist=op

if /i "%1" == "build" (
goto :build
)
if /i "%1" == "publish" (
goto :publish
) else (
echo escolha build ou publish
goto :eof
)

:build
set readme=readme.md
set license=LICENSE
set buildpath=build\
set distpath=dist\pyinstaller\%dist%-%version%\
set fzip=%dist%-%version%.zip
pyinstaller --distpath dist/pyinstaller -y op.spec
copy %readme% %distpath%%readme%
copy %license% %distpath%%license%
cd %distpath%
call zip -r %fzip% *.*
move %fzip% ..\%fzip%
cd ..\..\..
rd /s /q %distpath%
goto :eof

:publish
set distpath="C:\Users\Administrador\cli\op\dist\pyinstaller"
set drive="G:\Meu Drive"
set mtcliws="C:\Users\Administrador\cli\mtcli-ws\mtcli-ws\BIN"
copy %distpath%\%dist%-%version%.zip %mtcliws%\%dist%.zip
copy %distpath%\%dist%-%version%.zip %drive%\%dist%.zip
copy %distpath%\%dist%-%version%.zip %drive%\%dist%-%version%.zip
goto :eof
