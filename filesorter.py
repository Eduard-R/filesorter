import os
from pathlib import Path
import shutil
import sys

def file_sort(path):
    path = Path(path)
    for file in path.iterdir():
        suffix = file.suffix.lower().strip(".")
        if not suffix:
            suffix = "rest"
        
        destination = path / suffix
        destination.mkdir(exist_ok=True)

        shutil.move(str(file), destination / file.name)

file_sort(Path(sys.executable).parent)