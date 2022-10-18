import os
import subprocess


def test_notebooks():

    failures = []
    for directory, _, files in os.walk(os.path.join("..", "content")):
        if ".ipynb_checkpoints" in directory or "_build" in directory:
            continue

        for file in files:

            if not file.endswith(".py"):
                continue

            process = subprocess.run(
                ["python", os.path.join(directory, file)],
                capture_output=True,
                check=True,
            )

            if not process.returncode == 0:
                failures.append(process)

        if any(failures):
            raise RuntimeError(failures)


#  Copyright (c) 2022 Mira Geoscience Ltd.
