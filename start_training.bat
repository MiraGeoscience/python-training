@echo off
setlocal EnableDelayedExpansion

set MY_MICROMAMBA="%~dp0..\micromamba.exe"
if exist !MY_MICROMAMBA! (
  if exist "%~dp0..\_micromamba" (
    set MAMBA_ROOT_PREFIX=%~dp0..\_micromamba
    echo Using micromamba: !MY_MICROMAMBA! (root: !MAMBA_ROOT_PREFIX!)
    set MY_CONDA_RUNNER=!MY_MICROMAMBA:"=!
	goto conda_is_set
  )

call "%~dp0get_conda_exec.bat"
if !errorlevel! neq 0 (
  pause
  exit /B !errorlevel!
)
  
set MY_CONDA_RUNNER=!MY_CONDA_EXE:"=!

:conda_is_set

set ENV_NAME=python-training

cd %~dp0
set PYTHONUTF8=1

call "!MY_CONDA_RUNNER!" run -n %ENV_NAME% jupyter notebook training\index.ipynb

if !errorlevel! neq 0 (
  echo "** ERROR: Failed starting the notebook **"
)

:: pause and open terminal for diagnostic in case it failed
pause
cmd /k
