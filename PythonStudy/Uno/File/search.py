import os

class SearchFiles:
    @staticmethod
    def search_files_with_string(folder, search_string):
        search_string = search_string.lower()  # 소문자로 변환
        matching_files = []
        for root, _, files in os.walk(folder):
            for file in files:
                if search_string in file.lower():  # 파일명도 소문자로 변환하여 비교
                    matching_files.append(os.path.join(root, file))
        return matching_files
