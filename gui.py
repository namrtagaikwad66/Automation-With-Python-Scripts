import tkinter as tk
from tkinter import filedialog, messagebox
import os
from utils import create_folder, move_images

DEST_FOLDER = os.path.join(os.getcwd(), "data", "organized")

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        source_entry.delete(0, tk.END)
        source_entry.insert(0, folder)

def organize_images():
    source = source_entry.get()
    if not source or not os.path.exists(source):
        messagebox.showerror("Error", "Please select a valid folder")
        return
    create_folder(DEST_FOLDER)
    moved_count = move_images(source, DEST_FOLDER)
    messagebox.showinfo("Done", f"{moved_count} images moved successfully!")

root = tk.Tk()
root.title("GUI Image Organizer")
root.geometry("450x150")

tk.Label(root, text="Select Source Folder:").pack()
source_entry = tk.Entry(root, width=50)
source_entry.pack(padx=10)

tk.Button(root, text="Browse", command=browse_folder).pack(pady=5)
tk.Button(root, text="Organize Images", command=organize_images).pack(pady=5)

root.mainloop()