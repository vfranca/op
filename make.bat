@echo off
set version=0.1.0
set dist=op
set distpath=dist\pyinstaller

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
set fzip=%dist%-%version%.zip
pyinstaller --distpath %distpath% -y %dist%.spec
copy %readme% %distpath%\%dist%-%version%\%readme%
copy %license% %distpath%\%dist%-%version%\%license%
cd %distpath%\%dist%-%version%
call zip -r %fzip% *.*
move %fzip% ..\%fzip%
cd ..\..\..
rd /s /q %distpath%\%dist%-%version%
goto :eof

:publish
set drive="G:\Meu Drive"
set mtcliws="C:\Users\Administrador\cli\mtcli-ws\mtcli-ws\BIN"
copy %distpath%\%dist%-%version%.zip %mtcliws%\%dist%.zip
copy %distpath%\%dist%-%version%.zip %drive%\%dist%.zip
copy %distpath%\%dist%-%version%.zip %drive%\%dist%-%version%.zip
goto :eof
