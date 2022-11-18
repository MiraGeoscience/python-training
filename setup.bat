@echo off
setlocal EnableDelayedExpansion

call "%~dp0get_conda_exec.bat"
if !errorlevel! neq 0 (
  exit /B !errorlevel!
)

set MY_CONDA=!MY_CONDA_EXE:"=!
cd %~dp0
set PYTHONUTF8=1
call "!MY_CONDA!" remove --name python-training --all --yes
call "!MY_CONDA!" env update -f environments\conda-py-3.9-win-64.lock.yml -n python-training
call "!MY_CONDA!" activate python-training && python -m pip install -e . --no-deps
pause
cmd /k
