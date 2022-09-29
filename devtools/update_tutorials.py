#  Copyright (c) 2022 Mira Geoscience Ltd.
#
#  This file is part of python-training.

import os
import sys

CONVERT = {"ipynb": "py", "py": "ipynb"}


def update_files(ext):
    for directory, _, files in os.walk(os.path.join("..", "content")):
        if ".ipynb_checkpoints" in directory or "_build" in directory:
            continue

        for file in files:

            if not file.endswith(CONVERT[ext]):
                continue

            os.system(f"jupytext --to {ext} {os.path.join(directory, file)}")


def update_forms(ext):

    os.makedirs("../training", exist_ok=True)

    for directory, _, files in os.walk(os.path.join("..", "content")):
        if ".ipynb_checkpoints" in directory or "_build" in directory:
            continue

        for file in files:

            if not file.endswith(ext):
                continue

            new_file = os.path.join("../training", file)

            with open(os.path.join(directory, file)) as orig:
                lines = list(orig)
                skip = False
                with open(new_file, mode="w+") as new:
                    for line in lines:
                        if "# +" in line:
                            skip = True

                        if line[0] in ["#", "\n"]:
                            if "# -" in line and skip:
                                skip = False
                                new.write("\n")
                            new.write(line)

            os.system(f"jupytext --to {CONVERT[ext]} {new_file}")
            os.remove(new_file)


if __name__ == "__main__":
    ext = sys.argv[1]

    if ext == "forms":
        update_forms("py")
    else:
        update_files(ext)

#  Copyright (c) 2022 Mira Geoscience Ltd.
