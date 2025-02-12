from tkinter import Tk
from app import FolderOrganizerApp

if __name__ == "__main__":
    root = Tk()
    root.geometry("1200x700")  # 창 크기를 확장합니다.
    app = FolderOrganizerApp(root)
    root.mainloop()
