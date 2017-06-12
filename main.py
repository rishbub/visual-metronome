import time
import tkinter

bpm = 140
beats = 3

background_color = "#222"
beat_color = "#eee"

canvas_width = 1000
canvas_height = 150

tk = tkinter.Tk()

canvas = tkinter.Canvas(tk, width=canvas_width, height=canvas_height)
canvas.pack()
tk.update()

while True:
    canvas.create_rectangle(0, 0, tk.winfo_width(), tk.winfo_height(), fill=background_color)
    for i in range(beats):
        canvas.config(width=tk.winfo_width()-2, height=tk.winfo_height()-2)
        canvas.create_rectangle((tk.winfo_width()/beats)*i+1, 0, (tk.winfo_width()/beats)*(i+1)-1, tk.winfo_height(), fill=beat_color)
        tk.update()
        time.sleep((bpm/60)**(-1))