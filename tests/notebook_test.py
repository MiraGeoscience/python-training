#  Copyright (c) 2022-2026 Mira Geoscience Ltd.
#
#  This file is part of python-training.

import subprocess
from pathlib import Path


def test_notebooks():

    failures = []
    for directory, _, files in Path("..", "content").walk():
        if ".ipynb_checkpoints" in str(directory) or "_build" in str(directory):
            continue

        for file in files:
            if not file.endswith(".py"):
                continue

            process = subprocess.run(
                ["python", directory / file],
                capture_output=True,
                check=True,
            )

            if not process.returncode == 0:
                failures.append(process)

        if any(failures):
            raise RuntimeError(failures)
