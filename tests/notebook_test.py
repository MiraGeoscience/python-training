#  Copyright (c) 2022 Mira Geoscience Ltd.
#
#  This file is part of python-training.

import os
import subprocess

from nbconvert import ScriptExporter, export


def test_notebooks():
    os.makedirs("notebooks", exist_ok=True)
    failures = []

    for directory, sub_dir, files in os.walk(os.path.join("..", "training")):
        if ".ipynb_checkpoints" in directory or "_build" in directory:
            continue
        for file in files:
            if file.endswith(".ipynb"):
                file_name = os.path.join("notebooks", file[:-6] + ".py")
                with open(file_name, mode="w") as script:
                    content = export(ScriptExporter, os.path.join(directory, file))[0]
                    script.write(content)

                process = subprocess.run(["python", file_name], capture_output=True)

                if not process.returncode == 0:
                    failures.append(process)

        if any(failures):
            raise RuntimeError(failures)
