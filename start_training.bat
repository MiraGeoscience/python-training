@echo off
setlocal EnableDelayedExpansion

call "%~dp0get_conda_exec.bat"
if !errorlevel! neq 0 (
  pause
  exit /B !errorlevel!
)

set ENV_NAME=python-training

set MY_CONDA=!MY_CONDA_EXE:"=!
cd %~dp0
set PYTHONUTF8=1

call "!MY_CONDA!" run -n %ENV_NAME% jupyter notebook training\index.ipynb

if !errorlevel! neq 0 (
  echo "** ERROR: Failed starting the notebook **"
  pause
  exit /B !errorlevel!
)

pause
cmd /k "!MY_CONDA! activate %ENV_NAME%"
