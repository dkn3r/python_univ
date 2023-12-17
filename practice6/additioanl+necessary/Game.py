import tkinter as tk
from tkinter import Canvas, PhotoImage, Label, Button
import time


class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("The man run to the exit")
        self.root.resizable(0, 0)
        self.root.wm_attributes("-topmost", 1)

        self.canvas = Canvas(self.root, width=500, height=500, highlightthickness=0)
        self.canvas.pack()
        self.canvas_height = 500
        self.canvas_width = 500

        self.bg = PhotoImage(file="img/background.png")
        self.canvas.create_image(0, 0, image=self.bg, anchor='nw')

        self.sprites = []
        self.running = True
        self.game_over = False

        self.start_time = None
        self.timer_label = Label(self.root, text="Timer: 0 s", font=('Arial', 12),highlightthickness=0, justify='right')
        self.timer_label.pack(side="top",anchor='ne')

    def start_timer(self):
        if not self.start_time:
            self.start_time = time.time()
            self.update_timer()

    def update_timer(self):
        if self.start_time and not self.game_over:
            elapsed_time = int(time.time() - self.start_time)
            self.timer_label.config(text=f"Timer: {elapsed_time} s")
        if not self.game_over:
            self.root.after(1000, self.update_timer)

    def stop_timer(self):
        if self.start_time:
            self.start_time = None  # Зупиняємо таймер
            self.timer_label.config(text="Timer: 0 s")

    def stop(self):
        self.running = False

    def mainloop(self):
        while self.running and not self.game_over:
            for sprite in self.sprites:
                sprite.move()

            self.root.update_idletasks()
            self.update_timer()
            self.root.update()
            time.sleep(0.01)
