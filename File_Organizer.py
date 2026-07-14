import os
import shutil

FOLDERS = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".mp4": "Videos",
    ".mp3": "Audio",
}

def organize(directory):
    for file in os.listdir(directory):
        path = os.path.join(directory, file)

        if os.path.isfile(path):
            ext = os.path.splitext(file)[1].lower()

            if ext in FOLDERS:
                folder = os.path.join(directory, FOLDERS[ext])
                os.makedirs(folder, exist_ok=True)
                shutil.move(path, os.path.join(folder, file))

if name == "main":
    organize(".")
    print("Files organized successfully!")
