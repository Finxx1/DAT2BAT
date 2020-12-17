cd Src\Windows\
pyinstaller -F b2c.py
pyinstaller -F bARC.py
py b2c.py c2bin.bat
..\Tcc\win32\tcc -o c2bin.exe c2bin.bat.c
copy c2bin.exe ..\..\Bin\
copy dist\* ..\..\Bin\
del __pycache__\* -y
rmdir __pycache__
del build\b2c\* -y
del build\bARC\* -y
rmdir build\b2c
rmdir build\bARC
rmdir build
del dist\* -y
rmdir dist
del *.spec -y
del *.c -y
del *.exe -y