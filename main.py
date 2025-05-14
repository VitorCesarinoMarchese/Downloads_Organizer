import os
import shutil
import sys
import json

with open('config.json', 'r') as f:
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
                    target_folder = os.path.join(folder_path, folder)

                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)

                    shutil.move(file_path, os.path.join(
                        target_folder, filename))
                    print(f"Moved {filename} -> {folder}/")
                    break


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python main.py <folder_path>")
    else:
        folder = sys.argv[1]
        organize_folder(folder)
