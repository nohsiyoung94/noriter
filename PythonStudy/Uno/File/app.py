from tkinter import messagebox, Frame
from file_operations import FileOperations
from fireworks import Fireworks
from gui import GUI
from search import SearchFiles
from monitor import SystemMonitor

class FolderOrganizerApp:
    def __init__(self, root):
        self.root = root
        left_frame = Frame(root)
        left_frame.pack(side="left", fill="both", expand=True)

        right_frame = Frame(root)
        right_frame.pack(side="right", fill="both", expand=True)

        self.gui = GUI(left_frame, root)  # root를 추가로 전달합니다.
        self.gui.setup_gui(self.process_folder, self.search_files, self.select_folder)

        self.system_monitor = SystemMonitor(right_frame)

    def process_folder(self):
        folder = self.gui.select_folder()
        if not folder:
            return

        self.gui.update_status("Processing... Please wait a moment.")

        files_moved, renamed_files = FileOperations.process_folder(folder)

        self.gui.update_status(f"Renamed files: {renamed_files}, Moved videos: {files_moved}")

        self.show_fireworks()

        if messagebox.askyesno("Completed", "Do you want to delete empty folders?"):
            FileOperations.delete_empty_folders(folder)
            self.gui.update_status("Completed: Empty folders deleted.")
        else:
            self.gui.update_status("Completed: Empty folders retained.")

    def show_fireworks(self):
        self.gui.fireworks_canvas.delete("all")
        Fireworks.create_fireworks(self.gui.fireworks_canvas)

    def search_files(self):
        folder = self.gui.get_selected_folder()
        if not folder:
            self.gui.update_status("Folder selection required: Please select a folder to search.")
            return

        search_string = self.gui.get_search_string()
        if not search_string:
            self.gui.update_status("Input required: Please enter a search string.")
            return

        matching_files = SearchFiles.search_files_with_string(folder, search_string)

        self.gui.display_search_results(folder, matching_files)

    def select_folder(self):
        self.gui.set_selected_folder()
