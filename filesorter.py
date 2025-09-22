from pathlib import Path
import shutil
import sys

def file_sort(path):
    path = Path(path)

    # aktuelle .exe-Datei merken (falls es eine gibt)
    current_exe = Path(sys.argv[0]).resolve()

    for file in path.iterdir():
        # nur Dateien bearbeiten
        if not file.is_file():
            continue

        # die eigene exe-Datei überspringen
        if file.resolve() == current_exe:
            continue

        # Dateiendung bestimmen
        suffix = file.suffix.lower().strip(".")
        if not suffix:
            suffix = "rest"

        # Zielordner bestimmen und ggf. einmalig anlegen
        destination = path / suffix
        destination.mkdir(exist_ok=True)

        # Datei verschieben
        target = destination / file.name
        if not target.exists():  
            shutil.move(str(file), target)
        else:
            # Wenn Datei schon existiert → z. B. mit Zähler umbenennen
            counter = 1
            new_name = f"{file.stem}_{counter}{file.suffix}"
            while (destination / new_name).exists():
                counter += 1
                new_name = f"{file.stem}_{counter}{file.suffix}"
            shutil.move(str(file), destination / new_name)


if __name__ == "__main__":
    # aktuelles Arbeitsverzeichnis verwenden
    file_sort(Path.cwd())
