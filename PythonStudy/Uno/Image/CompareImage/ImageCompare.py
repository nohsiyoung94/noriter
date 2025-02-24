import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import cv2
import imagehash
from skimage.metrics import structural_similarity as ssim

class ImageComparerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Similarity Comparison")
        self.root.geometry("1200x600")

        self.image_path = ""
        self.uploaded_image = None
        self.folder_path = ""
        self.images_to_compare = []

        # Left image display
        self.image_label = tk.Label(root)
        self.image_label.place(x=20, y=20, width=400, height=500)

        # Right image display (Comparison result)
        self.compare_image_label = tk.Label(root)
        self.compare_image_label.place(x=660, y=20, width=400, height=500)

        self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_button.place(x=440, y=20)

        self.folder_button = tk.Button(root, text="Select Folder", command=self.select_folder)
        self.folder_button.place(x=440, y=60)

        self.compare_button = tk.Button(root, text="Compare", command=self.compare_images)
        self.compare_button.place(x=440, y=100)

        self.filepath_label = tk.Label(root, text="No image uploaded", anchor="w")
        self.filepath_label.place(x=440, y=140, width=200)

        self.result_frame = tk.Frame(root)
        self.result_frame.place(x=440, y=200, width=200, height=350)

        self.rank_labels = {
            "1st": tk.Listbox(self.result_frame, height=5),
            "2nd": tk.Listbox(self.result_frame, height=5),
            "3rd": tk.Listbox(self.result_frame, height=5),
        }

        for idx, label in enumerate(self.rank_labels):
            tk.Label(self.result_frame, text=f"{label} Rank").grid(row=idx, column=0, pady=5)
            self.rank_labels[label].grid(row=idx, column=1)
            self.rank_labels[label].bind("<<ListboxSelect>>", self.display_selected_image)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image_path = file_path
            self.filepath_label.config(text=f"Uploaded: {os.path.basename(file_path)}")
            self.show_image(file_path, self.image_label)

    def show_image(self, file_path, label):
        image = Image.open(file_path)
        image.thumbnail((400, 500))
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.folder_path = folder_path
            self.images_to_compare = [os.path.join(folder_path, f)
                                      for f in os.listdir(folder_path)
                                      if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            messagebox.showinfo("Folder Selected", f"Loaded {len(self.images_to_compare)} images.")

    def compare_images(self):
        if not self.image_path or not self.folder_path:
            messagebox.showerror("Error", "Please upload an image and select a folder first.")
            return

        for label in self.rank_labels.values():
            label.delete(0, tk.END)

        first_rank, second_rank, third_rank = [], [], []

        uploaded_image = cv2.imread(self.image_path)
        uploaded_gray = cv2.cvtColor(uploaded_image, cv2.COLOR_BGR2GRAY)

        uploaded_hash = imagehash.phash(Image.open(self.image_path))
        orb = cv2.ORB_create()

        for image_path in self.images_to_compare:
            compare_image = cv2.imread(image_path)
            if compare_image is None:
                continue

            compare_gray = cv2.cvtColor(compare_image, cv2.COLOR_BGR2GRAY)
            compare_hash = imagehash.phash(Image.open(image_path))

            # Step 1: Hash comparison (for overall similarity)
            hash_diff = uploaded_hash - compare_hash

            # Step 2: ORB Keypoint Matching
            kp1, des1 = orb.detectAndCompute(uploaded_gray, None)
            kp2, des2 = orb.detectAndCompute(compare_gray, None)

            if des1 is not None and des2 is not None:
                bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
                matches = bf.match(des1, des2)
                orb_score = len(matches)

                if hash_diff < 10 or orb_score > 50:
                    first_rank.append(image_path)
                elif hash_diff < 20 or orb_score > 30:
                    second_rank.append(image_path)
                else:
                    third_rank.append(image_path)

        self.display_results(first_rank, second_rank, third_rank)

    def display_results(self, first, second, third):
        for label, rank in zip(["1st", "2nd", "3rd"], [first, second, third]):
            for image in rank:
                self.rank_labels[label].insert(tk.END, os.path.basename(image))

    def display_selected_image(self, event):
        selected = event.widget.curselection()
        if selected:
            index = selected[0]
            image_name = event.widget.get(index)
            for path in self.images_to_compare:
                if image_name in path:
                    self.show_image(path, self.compare_image_label)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageComparerApp(root)
    root.mainloop()