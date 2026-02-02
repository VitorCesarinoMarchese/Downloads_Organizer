from pathlib import Path
import os
import shutil
import sys
import json

BASE_DIR = Path(__file__).resolve().parent
CONFIG_PATH = BASE_DIR / "config.json"

with open(CONFIG_PATH, 'r') as f:
    FILE_TYPES = json.load(f)


def organize_folder(folder_path):
    if not os.path.isdir(folder_path):
        print("Invalid folder path")
        return
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()

            for folder, extensions in FILE_TYPES.items():
                if file_extension in extensions:
                    match folder:
                        case "Images":
                            target_folder = os.path.expanduser("~/Pictures/")
                        case "Documents":
                            target_folder = os.path.expanduser("~/Documents/")
                        case "Videos":
                            target_folder = os.path.expanduser("~/obs/")
                        case _:
                            target_folder = os.path.join(folder_path, folder)

                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)

                    try:
                        shutil.move(file_path,
                                    target_folder)
                        print(f"Moved {filename} -> {target_folder}/")
                    except Exception as e:
                        print(f"Error moving {filename}: {e}")

                    break


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python main.py <folder_path>")
    else:
        folder = sys.argv[1]
        organize_folder(folder)
