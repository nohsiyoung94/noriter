import tkinter as tk
from tkinter import scrolledtext
import requests
import os
import shutil
import datetime

class QBittorrentClient:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.session = requests.Session()
        self.login(username, password)

    def login(self, username, password):
        headers = {'Referer': f'{self.base_url}'}
        login_data = {'username': username, 'password': password}
        response = self.session.post(f'{self.base_url}/api/v2/auth/login', data=login_data, headers=headers)
        if response.status_code == 200 and response.text == "Ok.":
            print("로그인 성공!")
        else:
            print("로그인 실패:", response.text)
            exit()

    def get_torrents(self):
        response = self.session.get(f"{self.base_url}/api/v2/torrents/info")
        if response.status_code == 200:
            try:
                torrents = response.json()
                print(f"Torrents: {torrents}")  # 디버깅을 위한 출력
                return torrents
            except requests.exceptions.JSONDecodeError:
                print(f"JSONDecodeError: {response.text}")
                return None
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

class FileManager:
    @staticmethod
    def move_file(source_path, destination_folder, filename):
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        source = os.path.join(source_path, filename)
        destination = os.path.join(destination_folder, filename)
        if os.path.isfile(source):
            shutil.move(source, destination)
            return True
        return False

class TorrentMonitorApp:
    def __init__(self, client, download_folder):
        self.client = client
        self.download_folder = download_folder
        self.destination_folder = self.create_destination_folder()

        self.root = tk.Tk()
        self.root.title("qBittorrent 상태 모니터링")
        self.root.geometry("800x600")

        self.first_connection_label = tk.Label(self.root, text="토렌트 연결 상태: 연결 중...")
        self.first_connection_label.pack()

        self.updated_connection_label = tk.Label(self.root, text="토렌트 연결 상태: 연결 중...")
        self.updated_connection_label.pack()

        self.dashboard_frame = tk.Frame(self.root)
        self.dashboard_frame.pack()

        self.waiting_label = tk.Label(self.dashboard_frame, text="대기중인 파일 개수: 0")
        self.waiting_label.grid(row=0, column=0)
        self.waiting_text = scrolledtext.ScrolledText(self.dashboard_frame, width=50, height=5)
        self.waiting_text.grid(row=1, column=0)

        self.downloading_label = tk.Label(self.dashboard_frame, text="다운로드중인 파일 개수: 0")
        self.downloading_label.grid(row=0, column=1)
        self.downloading_text = scrolledtext.ScrolledText(self.dashboard_frame, width=50, height=5)
        self.downloading_text.grid(row=1, column=1)

        self.completed_label = tk.Label(self.dashboard_frame, text="다운로드 완료된 파일 개수: 0")
        self.completed_label.grid(row=0, column=2)
        self.completed_text = scrolledtext.ScrolledText(self.dashboard_frame, width=50, height=5)
        self.completed_text.grid(row=1, column=2)

        self.update_status()
        self.first_connection_label.config(text=f"토렌트 연결이 완료되었습니다. 연결시간 : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.root.mainloop()

    def create_destination_folder(self):
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        destination_folder = os.path.join(self.download_folder, today)
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        return destination_folder

    def update_status(self):
        torrents = self.client.get_torrents()
        if torrents is None:
            self.first_connection_label.config(text="qBittorrent 웹 UI와 연결 실패. 설정을 확인하세요.")
            return

        waiting_files = []
        downloading_files = []
        completed_files = []

        for torrent in torrents:
            name = torrent['name']
            progress = torrent['progress'] * 100  # 진행률 (퍼센트)
            status = torrent['state']
            print(f"Name: {name}, Status: {status}, Progress: {progress:.2f}%")  # 디버깅을 위한 출력

            if status in ["uploading", "stalledUP", "pausedUP", "checkingUP"]:
                completed_files.append(name)
                if FileManager.move_file(self.download_folder, self.destination_folder, name):
                    print(f"{name} 파일을 {self.destination_folder}로 이동했습니다.")
            elif status in ["downloading", "stalledDL"]:
                downloading_files.append(f"{name} ({progress:.2f}%)")
            else:
                waiting_files.append(name)

        self.update_dashboard(waiting_files, downloading_files, completed_files)
        self.root.after(3000, self.update_status)

    def update_dashboard(self, waiting_files, downloading_files, completed_files):
        self.waiting_label.config(text=f"대기중인 파일 개수: {len(waiting_files)}")
        self.waiting_text.delete(1.0, tk.END)
        self.waiting_text.insert(tk.END, "\n".join(waiting_files))

        self.downloading_label.config(text=f"다운로드중인 파일 개수: {len(downloading_files)}")
        self.downloading_text.delete(1.0, tk.END)
        self.downloading_text.insert(tk.END, "\n".join(downloading_files))

        self.completed_label.config(text=f"다운로드 완료된 파일 개수: {len(completed_files)}")
        self.completed_text.delete(1.0, tk.END)
        self.completed_text.insert(tk.END, "\n".join(completed_files))

        self.updated_connection_label.config(text=f"새로고침 시간 : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    client = QBittorrentClient('http://localhost:8090', 'admin', 'admin')
    app = TorrentMonitorApp(client, 'D:\\희안')
