from tkinter import Tk, filedialog, messagebox, ttk, Canvas, Entry, Label, StringVar, Text, Scrollbar, VERTICAL, RIGHT, Y, LEFT, BOTH
from PIL import Image, ImageTk

class GUI:
    def __init__(self, parent, root):
        self.parent = parent
        self.root = root
        self.status_label = None
        self.fireworks_canvas = None
        self.search_string_var = StringVar()
        self.results_text = None
        self.selected_folder = None  # 검색할 폴더를 저장하기 위한 변수
        self.search_delay = None  # 검색 지연 타이머 변수

    def setup_gui(self, process_folder_callback, search_files_callback, select_folder_callback):
        self.root.title("Folder and File Organizer")
        self.root.geometry("600x700")

        try:
            header_image = Image.open("header.png")
            header_image = header_image.resize((600, 100), Image.ANTIALIAS)
            header_photo = ImageTk.PhotoImage(header_image)
            header_label = ttk.Label(self.root, image=header_photo)
            header_label.image = header_photo
            header_label.pack()
        except Exception:
            header_label = ttk.Label(self.root, text="Folder Organizer", font=("Arial", 20, "bold"))
            header_label.pack()

        frame = ttk.Frame(self.root)
        frame.pack(pady=20)

        select_folder_button = ttk.Button(frame, text="Select Folder and Start", command=process_folder_callback)
        select_folder_button.pack(pady=10)

        self.status_label = ttk.Label(frame, text="Status: Waiting", font=("Arial", 12))
        self.status_label.pack(pady=10)

        self.fireworks_canvas = Canvas(self.root, width=600, height=150, bg="black")
        self.fireworks_canvas.pack()

        search_frame = ttk.Frame(self.root)
        search_frame.pack(pady=20)

        search_entry_label = Label(search_frame, text="Enter Search String:", font=("Arial", 12))
        search_entry_label.grid(row=0, column=0, padx=5, pady=5)
        search_entry = Entry(search_frame, textvariable=self.search_string_var, width=30)
        search_entry.grid(row=0, column=1, padx=5, pady=5)
        search_entry.bind('<KeyRelease>', lambda event: self.delayed_search(search_files_callback))  # 검색 지연 이벤트 추가

        folder_search_button = ttk.Button(search_frame, text="Select Search Folder", command=select_folder_callback)
        folder_search_button.grid(row=1, column=0, columnspan=2, pady=10)

        search_folder_button = ttk.Button(search_frame, text="Search in Folder", command=search_files_callback)
        search_folder_button.grid(row=2, column=0, columnspan=2, pady=10)

        results_frame = ttk.Frame(self.root)
        results_frame.pack(pady=10, fill=BOTH, expand=True)

        self.results_text = Text(results_frame, height=10, width=70, wrap='word')
        self.results_text.pack(side=LEFT, fill=BOTH, expand=True)

        scrollbar = Scrollbar(results_frame, orient=VERTICAL, command=self.results_text.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.results_text.config(yscrollcommand=scrollbar.set)

    def delayed_search(self, search_files_callback):
        if self.search_delay:
            self.root.after_cancel(self.search_delay)
        self.search_delay = self.root.after(1000, search_files_callback)  # 1초 지연 후 검색 실행

    def update_status(self, text):
        self.status_label.config(text=text)
        self.root.update_idletasks()

    def get_search_string(self):
        return self.search_string_var.get().strip()

    def select_folder(self):
        return filedialog.askdirectory(title="Select Folder")

    def set_selected_folder(self):
        self.selected_folder = self.select_folder()
        self.update_status(f"Selected Folder: {self.selected_folder}")

    def get_selected_folder(self):
        return self.selected_folder

    def display_search_results(self, folder, matching_files):
        self.results_text.delete(1.0, 'end')
        self.results_text.insert('end', f"Search Folder: {folder}\n\n")
        self.results_text.insert('end', "Search Results:\n")
        if matching_files:
            for file in matching_files:
                self.results_text.insert('end', f"{file}\n")
        else:
            self.results_text.insert('end', "No files found.\n")
