#  Copyright (c) 2022 Mira Geoscience Ltd.
#
#  This file is part of python-training.

import os
import shutil
import subprocess


def test_notebooks(tmp_path):
    os.makedirs("notebooks", exist_ok=True)
    failures = []

    for directory, _, files in os.walk(os.path.join("..", "training")):
        if ".ipynb_checkpoints" in directory or "_build" in directory:
            continue

        for file in files:

            if not file.endswith(".py"):
                continue

            shutil.copy(os.path.join(directory, file), tmp_path / file)
            process = subprocess.run(
                ["python", tmp_path / file], capture_output=True, check=True
            )

            if not process.returncode == 0:
                failures.append(process)

        if any(failures):
            raise RuntimeError(failures)
