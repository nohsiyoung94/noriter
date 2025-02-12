import os
import shutil

class FileOperations:
    @staticmethod
    def move_videos_outside(folder):
        video_extensions = ['.mp4', '.avi', '.mkv', '.mov']
        files_moved = 0
        for root, dirs, files in os.walk(folder):
            for file in files:
                if any(file.lower().endswith(ext) for ext in video_extensions):
                    full_path = os.path.join(root, file)
                    if root != folder:
                        shutil.move(full_path, folder)
                        files_moved += 1
        return files_moved

    @staticmethod
    def rename_files(folder):
        renamed_files = 0
        for root, _, files in os.walk(folder):
            for file in files:
                if '@' in file:
                    new_name = file.split('@', 1)[-1]
                    old_path = os.path.join(root, file)
                    new_path = os.path.join(root, new_name)
                    os.rename(old_path, new_path)
                    renamed_files += 1
        return renamed_files

    @staticmethod
    def delete_empty_folders(folder):
        for root, dirs, _ in os.walk(folder, topdown=False):
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                if not os.listdir(dir_path):
                    os.rmdir(dir_path)

    @classmethod
    def process_folder(cls, folder):
        files_moved = cls.move_videos_outside(folder)
        renamed_files = cls.rename_files(folder)
        return files_moved, renamed_files
