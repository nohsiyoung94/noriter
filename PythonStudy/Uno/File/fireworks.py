import random
from tkinter import Canvas

class Fireworks:
    @staticmethod
    def create_fireworks(canvas: Canvas):
        colors = ["red", "blue", "yellow", "green", "orange", "purple", "pink"]
        for _ in range(50):
            x = random.randint(50, 550)
            y = random.randint(10, 140)
            color = random.choice(colors)
            size = random.randint(5, 15)
            canvas.create_oval(x, y, x + size, y + size, fill=color, outline="")
