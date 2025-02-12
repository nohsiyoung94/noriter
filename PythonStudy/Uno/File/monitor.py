import psutil
import time
from tkinter import ttk, StringVar, Frame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SystemMonitor:
    def __init__(self, parent):
        self.parent = parent

        self.cpu_var = StringVar()
        self.ram_var = StringVar()
        self.own_memory_var = StringVar()
        self.network_var = StringVar()
        self.figure, self.ax = plt.subplots()

        self.previous_usages = []

        self.create_widgets()
        self.update_stats()

    def create_widgets(self):
        frame = Frame(self.parent)
        frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        ttk.Label(frame, text="System Monitoring Dashboard", font=("Arial", 14, "bold")).pack(pady=10)

        self.cpu_label = ttk.Label(frame, textvariable=self.cpu_var, font=("Arial", 12))
        self.cpu_label.pack(pady=5)

        self.ram_label = ttk.Label(frame, textvariable=self.ram_var, font=("Arial", 12))
        self.ram_label.pack(pady=5)

        self.own_memory_label = ttk.Label(frame, textvariable=self.own_memory_var, font=("Arial", 12))
        self.own_memory_label.pack(pady=5)

        self.network_label = ttk.Label(frame, textvariable=self.network_var, font=("Arial", 12))
        self.network_label.pack(pady=5)

        self.canvas = FigureCanvasTkAgg(self.figure, frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    def update_stats(self):
        self.cpu_var.set(f"CPU Usage: {psutil.cpu_percent()}%")
        self.ram_var.set(f"RAM Usage: {psutil.virtual_memory().percent:.3f}%")
        
        # 프로그램 메모리 사용량
        process = psutil.Process()
        own_memory_usage = process.memory_info().rss / (1024 * 1024)  # MB 단위로 변환
        total_memory = psutil.virtual_memory().total / (1024 * 1024)  # MB 단위로 변환
        memory_percentage = (own_memory_usage / total_memory) * 100
        self.own_memory_var.set(f"Program Memory Usage: {own_memory_usage:.3f}MB ({memory_percentage:.3f}%)")

        # 각 디스크 드라이브의 사용량 표시
        partitions = [partition.device for partition in psutil.disk_partitions() if partition.fstype]
        usages = [(psutil.disk_usage(partition.mountpoint).percent, psutil.disk_usage(partition.mountpoint).used / (1024 * 1024 * 1024)) for partition in psutil.disk_partitions() if partition.fstype]

        self.ax.clear()
        bars = self.ax.bar([partition for partition, _ in usages], [usage for usage, _ in usages], color='blue')
        self.ax.set_title("Drive Usage")
        self.ax.set_xlabel("Drive")
        self.ax.set_ylabel("Usage (%)")

        for bar, (percent, used) in zip(bars, usages):
            self.ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, f'{used:.3f}GB', ha='center', va='bottom')

        # 용량이 변한 경우 막대 색상을 변경
        if self.previous_usages:
            for bar, (current, previous) in zip(bars, self.previous_usages):
                if current != previous:
                    bar.set_color('red')
                else:
                    bar.set_color('blue')

        self.previous_usages = [usage for usage, _ in usages]

        self.canvas.draw()
        
        # 네트워크 속도 (예: 송수신 바이트 수를 이용하여 속도 계산)
        net_io = psutil.net_io_counters()
        self.network_var.set(f"Network - Sent: {net_io.bytes_sent // (2**20)}MB Received: {net_io.bytes_recv // (2**20)}MB")

        # 1초마다 업데이트
        self.parent.after(1000, self.update_stats)
