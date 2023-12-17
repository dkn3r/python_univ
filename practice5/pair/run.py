from tkinter import *

import time
from Ball import Ball
from Paddle import Paddle
from EventHandler import EventHandler


def start_game(event=None):
    global paddle, ball

    canvas.delete(start_text)
    canvas.itemconfig(end_text, state="hidden")
    canvas.itemconfig(continue_text, state="hidden")
    paddle = Paddle(canvas, 'blue')
    ball = Ball(canvas, paddle, 'red')
    animate()


def animate():
    tk.bind_all('<Button-1>', restart_game)
    if not event_handler.is_active:
        return
    if not ball.hit_bottom:
        ball.draw()
        paddle.draw()
        tk.after(10, animate)

    else:
        canvas.itemconfig(end_text, state="normal")
        canvas.itemconfig(continue_text, state="normal")



def restart_game(event):
    global paddle, ball
    canvas.itemconfig(end_text, state="hidden")
    canvas.itemconfig(continue_text, state="hidden")

    paddle.delete_paddle()
    ball.delete_ball()
    ball.start_score()
    paddle = Paddle(canvas, 'blue')
    ball = Ball(canvas, paddle, 'red')



    animate()


def on_escape(event=None):
    tk.destroy()
    print("Гра завершена!")


tk = Tk()
tk.title("Гра JUMP!")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()

start_text = canvas.create_text(250, 200, text="Click to start", font=("Arial", 20, 'bold'), fill='green')

end_text = canvas.create_text(250, 200, text="The end!\n\n", font=("Arial", 20, 'bold'), fill="red")
continue_text = canvas.create_text(250, 200, text="Click to try again or press 'escape' to leave", font=("Arial", 10),
                                   fill="blue")
canvas.itemconfig(end_text, state="hidden")
canvas.itemconfig(continue_text, state="hidden")

paddle = None
ball = None
event_handler = EventHandler(tk)

tk.bind_all('<Button-1>', start_game)
tk.bind_all('<Escape>', on_escape)


tk.mainloop()
