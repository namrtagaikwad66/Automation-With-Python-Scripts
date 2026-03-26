import os
import shutil

source_folder = r"C:\3 task"
destination_folder = r"C:\3 task\all_images"

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

files_moved = 0

# Walk through all folders and subfolders
for root, dirs, files in os.walk(source_folder):
    for file in files:
        if file.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
            # Avoid moving the script itself
            if file.endswith(".py"):
                continue
            source_path = os.path.join(root, file)
            destination_path = os.path.join(destination_folder, file)
            shutil.move(source_path, destination_path)
            print("Moved:", file)
            files_moved += 1

if files_moved == 0:
    print("No image files found.")
else:
    print(f"Total {files_moved} image files moved successfully!")