#  Copyright (c) 2022 Mira Geoscience Ltd.
#
#  This file is part of python-training.

import os
import sys

CONVERT = {"ipynb": "py", "py": "ipynb"}
LOCATION = {"ipynb": os.path.join("content"), "py": os.path.join("content")}


def update_files(ext):
    for directory, _, files in os.walk(os.path.join(LOCATION[CONVERT[ext]])):
        if (
            ".ipynb_checkpoints" in directory
            or "_build" in directory
            or "__pycache__" in directory
        ):
            continue

        for file in files:
            head, tail = file.split(".")
            if not file.endswith(CONVERT[ext]) or "__init__" in file:
                continue

            outfile = f"{head}.{ext}"
            os.system(
                f"jupytext --output {os.path.join(directory, outfile)} {os.path.join(directory, file)}"
            )


def update_forms():

    os.makedirs("training", exist_ok=True)

    for directory, _, files in os.walk(os.path.join(LOCATION["py"])):
        if (
            ".ipynb_checkpoints" in directory
            or "_build" in directory
            or "__pycache__" in directory
        ):
            continue

        for file in files:

            if not file.endswith("py") or "__init__" in file:
                continue

            head, tail = file.split(".")
            new_file = os.path.join("training", f"{head}.py")

            with open(os.path.join(directory, file)) as orig:
                lines = list(orig)
                skip = False
                with open(new_file, mode="w+") as new:
                    for line in lines:
                        if "clear-form" in line:
                            skip = True

                        # if line[0] in ["#", "\n"]:
                        if "# -" in line and skip:
                            skip = False
                            new.write("\n")
                            continue

                        if not skip:
                            new.write(line)

            outfile = f"{head}.ipynb"
            os.system(
                f"jupytext --output {os.path.join('training', outfile)} {new_file}"
            )
            os.remove(new_file)


if __name__ == "__main__":

    if len(sys.argv) == 1 or sys.argv[1] not in ["py", "ipynb", "forms"]:
        raise UserWarning("Input argument should be one of 'py', 'ipynb' or 'forms'.")

    ext = sys.argv[1]

    if ext == "forms":
        update_forms()
    else:
        update_files(ext)

#  Copyright (c) 2022 Mira Geoscience Ltd.
