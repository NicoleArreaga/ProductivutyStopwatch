#Julia & Nicole's stopwatch timer
import tkinter as tk #we used tkinter instead of kivy because tkinter is used a toolkit that is able to construct wdigets, stopwatch,etc
import tkinter.font as TkFont
from datetime import datetime

def run():
    current_time = datetime.now()
    diff = current_time - start_time
    txt_var.set(' %d.%02d' % (diff.seconds,diff.microseconds//10000)) #converting seconds

    if running: #for timelapse
        root.after(20, run) #to reschedule after 20ms, refersh display

def start():
    global running
    global start_time

    if not running:
        running = True
        start_time = datetime.now()

        root.after(10, run)

def stop():
    global running

    running = False

def reset():
    global start_time
    start_time = datetime.now()

    if not running:
        txt_var.set(' 0:00 ')

running = False
start_time = None

root = tk.Tk()
root.geometry("600x300") #width x height of the stopwatch
root.title("Stopwatch")

txt_var = tk.StringVar()
txt_var.set(' 0:00 ')

fontstyle = TkFont.Font(size = 50) #to make the '0:00' bigger
tk.Label(root, textvariable=txt_var, font=fontstyle) .pack()

tk.Button(root, text="Start", command=start) .pack(fill = 'x') #start button
tk.Button(root, text='Stop', command=stop) .pack(fill='x') #stop button
tk.Button(root, text='Reset', command=reset) .pack(fill='x') #reset button
tk.Button(root, text='Timelapse', command=run) .pack(fill='x') #timelapse button
root.mainloop() #for looping purposes (multiple times)