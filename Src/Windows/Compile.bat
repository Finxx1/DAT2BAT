@echo off
if "%1"=="" goto end

Compiler\aB2Econv.exe %1 %1.exe

:end