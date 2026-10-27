#  Copyright (c) 2022 Mira Geoscience Ltd.
#
#  This file is part of python-training.

import json
import os
from pathlib import Path
from shutil import copy


def update_forms():

    os.makedirs("training", exist_ok=True)

    for dirpath, dirnames, filenames in Path("../content").walk():
        if (
            "checkpoints" in str(dirpath)
            or "_build" in str(dirpath)
            or "__pycache__" in str(dirpath)
        ):
            continue

        for file in filenames:
            if not file.endswith("ipynb"):
                continue

            new_file = copy(dirpath / file, Path("../assets/training") / file)

            with open(new_file) as orig:
                notebook = json.load(orig)

                for elem in notebook["cells"]:
                    flag = elem.get("metadata", {}).get("tags", [])

                    if "clear-form" in flag:
                        elem["source"] = []

            with open(new_file, "w") as out:
                json.dump(notebook, out, indent=1)


if __name__ == "__main__":
    update_forms()

#  Copyright (c) 2026 Mira Geoscience Ltd.
