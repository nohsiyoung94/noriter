import os
import shutil
from tkinter import Tk, filedialog, messagebox, ttk, Canvas
from PIL import Image, ImageTk
import random

# Functions for operations
def move_videos_outside(folder):
    video_extensions = ['.mp4', '.avi', '.mkv', '.mov']  # Modify extensions as needed
    files_moved = 0
    for root, dirs, files in os.walk(folder):
        for file in files:
            if any(file.lower().endswith(ext) for ext in video_extensions):
                full_path = os.path.join(root, file)
                if root != folder:  # Skip if already in the top-level folder
                    shutil.move(full_path, folder)
                    files_moved += 1
    return files_moved

def rename_files(folder):
    renamed_files = 0
    for root, _, files in os.walk(folder):
        for file in files:
            if '@' in file:
                new_name = file.split('@', 1)[-1]  # Keep only the part after '@'
                old_path = os.path.join(root, file)
                new_path = os.path.join(root, new_name)
                os.rename(old_path, new_path)
                renamed_files += 1
    return renamed_files

def delete_empty_folders(folder):
    for root, dirs, _ in os.walk(folder, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):  # Check if the folder is empty
                os.rmdir(dir_path)

def create_fireworks(canvas):
    colors = ["red", "blue", "yellow", "green", "orange", "purple", "pink"]
    for _ in range(50):
        x = random.randint(50, 550)
        y = random.randint(10, 140)
        color = random.choice(colors)
        size = random.randint(5, 15)
        canvas.create_oval(x, y, x + size, y + size, fill=color, outline="")

def process_folder():
    folder = filedialog.askdirectory(title="Select a Folder")
    if not folder:
        return

    # Update GUI status
    status_label.config(text="Processing... Please wait.")
    root.update_idletasks()

    files_moved = move_videos_outside(folder)
    renamed_files = rename_files(folder)

    # Display results
    status_label.config(text=f"Files Renamed: {renamed_files}, Videos Moved: {files_moved}")

    # Fireworks effect
    fireworks_canvas.delete("all")
    create_fireworks(fireworks_canvas)

    # Prompt to delete empty folders
    if messagebox.askyesno("Completed", "Do you want to delete empty folders?"):
        delete_empty_folders(folder)
        status_label.config(text="Completed: Empty folders deleted.")
    else:
        status_label.config(text="Completed: Empty folders retained.")

# GUI setup
root = Tk()
root.title("Folder and File Organizer")
root.geometry("600x400")

# Header image
try:
    header_image = Image.open("header.png")  # Provide the path to your header image
    header_image = header_image.resize((600, 100), Image.ANTIALIAS)
    header_photo = ImageTk.PhotoImage(header_image)
    header_label = ttk.Label(root, image=header_photo)
    header_label.pack()
except Exception as e:
    header_label = ttk.Label(root, text="Folder Organizer", font=("Arial", 20, "bold"))
    header_label.pack()

# Style and widget placement
frame = ttk.Frame(root)
frame.pack(pady=20)

select_folder_button = ttk.Button(frame, text="Select Folder and Start", command=process_folder)
select_folder_button.pack(pady=10)

status_label = ttk.Label(frame, text="Status: Waiting", font=("Arial", 12))
status_label.pack(pady=10)

fireworks_canvas = Canvas(root, width=600, height=150, bg="black")
fireworks_canvas.pack()

root.mainloop()
