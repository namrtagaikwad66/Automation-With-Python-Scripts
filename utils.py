import os
import shutil

IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".gif")

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def get_unique_filename(destination, filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    new_name = filename
    while os.path.exists(os.path.join(destination, new_name)):
        new_name = f"{base}_{counter}{ext}"
        counter += 1
    return new_name

def move_images(source, destination):
    files_moved = 0
    for root, _, files in os.walk(source):
        for file in files:
            if file.lower().endswith(IMAGE_EXTENSIONS):
                if os.path.abspath(root) == os.path.abspath(destination):
                    continue
                safe_name = get_unique_filename(destination, file)
                shutil.move(os.path.join(root, file), os.path.join(destination, safe_name))
                files_moved += 1
    return files_moved