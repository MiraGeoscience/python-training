@echo off
setlocal EnableDelayedExpansion

call "%~dp0get_conda_exec.bat"
if !errorlevel! neq 0 (
  pause
  exit /B !errorlevel!
)

set PY_VER=3.9

set ENV_NAME=python-training
set MY_CONDA=!MY_CONDA_EXE:"=!
cd %~dp0
set PYTHONUTF8=1

:: try installing libmamba solver in base environment (fail silently)
call "!MY_CONDA!" install -n base --override-channels -c conda-forge conda-libmamba-solver -y > nul 2>&1 ^
  && set "CONDA_SOLVER=libmamba" ^
  || (call )


set MY_CONDA_ENV_FILE=environments\conda-py-%PY_VER%-win-64.lock.yml
if not exist !MY_CONDA_ENV_FILE! (
  echo "** ERROR: Could not find the conda environment specification file '!MY_CONDA_ENV_FILE!' **"
  pause
  exit /B 1
)

call "!MY_CONDA!" activate base ^
  && call conda env create --force -n %ENV_NAME% --file !MY_CONDA_ENV_FILE!

if !errorlevel! neq 0 (
  echo "** ERROR: Installation failed **"
  pause
  exit /B !errorlevel!
)

call "!MY_CONDA!" run -n %ENV_NAME% jupyter notebook training\index.ipynb

:: pause and open terminal for diagnostic in case it failed
pause
cmd /k "!MY_CONDA!" activate %ENV_NAME%
