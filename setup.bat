@echo off
setlocal EnableDelayedExpansion

call "%~dp0get_conda_exec.bat"
if !errorlevel! neq 0 (
  pause
  exit /B !errorlevel!
)

set PY_VER=3.9

set MY_CONDA=!MY_CONDA_EXE:"=!
cd %~dp0
set PYTHONUTF8=1
call "!MY_CONDA!" activate
call conda remove --name python-training --all --yes
call conda env create -f environments\conda-py-%PY_VER%-win-64.lock.yml -n python-training
call conda activate python-training

pause
cmd /k
