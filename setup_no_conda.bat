:: assumes micromamba.exe is present in the parent folder
:: and creates the micromamba root folder there as _micromambaroot

@echo off
setlocal EnableDelayedExpansion

set MY_MICROMAMBA="%~dp0..\micromamba.exe"

if not exist !MY_MICROMAMBA! (
  echo INFO: Not finding !MY_MICROMAMBA!. Downloading...
  powershell.exe -command "& Invoke-RestMethod -URI https://micro.mamba.pm/api/micromamba/win-64/latest -OutFile \"%~dp0..\micromamba.tar.bz2\""
  tar x -O -f "%~dp0..\micromamba.tar.bz2" Library/bin/micromamba.exe > !MY_MICROMAMBA!
)

!MY_MICROMAMBA! --version > nul 2>&1
if !ERRORLEVEL! neq 0 (
  echo ERROR: Failed executing micromamba: !MY_MICROMAMBA! 1>&2
  pause
  exit /B !ERRORLEVEL!
)

set MAMBA_ROOT_PREFIX=%~dp0..\_micromamba
  
set PY_VER=3.9

set ENV_NAME=python-training
cd %~dp0
set PYTHONUTF8=1

set MY_CONDA_ENV_FILE=environments\conda-py-%PY_VER%-win-64.lock.yml
if not exist !MY_CONDA_ENV_FILE! (
  echo "** ERROR: Could not find the conda environment specification file '!MY_CONDA_ENV_FILE!' **"
  pause
  exit /B 1
)

!MY_MICROMAMBA! create --yes -n %ENV_NAME% --file !MY_CONDA_ENV_FILE!

if !errorlevel! neq 0 (
  echo "** ERROR: Installation failed **"
  pause
  exit /B !errorlevel!
)

!MY_MICROMAMBA! run -n %ENV_NAME% jupyter notebook training\index.ipynb

:: pause and open terminal for diagnostic in case it failed
pause
cmd /k !MY_MICROMAMBA! -n %ENV_NAME% run cmd
