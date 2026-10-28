@echo off
setlocal EnableDelayedExpansion

call "%~dp0get_conda_exec.bat"
if !errorlevel! neq 0 (
  pause
  exit /B !errorlevel!
)

set PY_VER=3.12

set ENV_NAME=python-training
set MY_CONDA=!MY_CONDA_EXE:"=!
cd %~dp0
set PYTHONUTF8=1
set CONDA_CHANNEL_PRIORITY=strict
set CONDA_CHANNEL_ALIAS=https://repo.prefix.dev

set MY_CONDA_ENV_FILE=environments\py-%PY_VER%-win-64.conda.lock.yml
if not exist !MY_CONDA_ENV_FILE! (
  echo "** ERROR: Could not find the conda environment specification file '!MY_CONDA_ENV_FILE!' **"
  pause
  exit /B 1
)

call "!MY_CONDA!" activate base ^
  && call "!MY_CONDA!" env create --yes -n %ENV_NAME% --file !MY_CONDA_ENV_FILE!

if !errorlevel! neq 0 (
  echo "** ERROR: Installation failed **"
  pause
  exit /B !errorlevel!
)

call "!MY_CONDA!" run -n %ENV_NAME% jupyter notebook assets\training

pause
