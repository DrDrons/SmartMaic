import tkinter as tk

master = tk.Tk()

def my_mainloop():
    print("Hello World!")
    master.after(60000, my_mainloop)  # run again after 1000ms (1s)

master.after(60000, my_mainloop) # run first time after 1000ms (1s)

master.mainloop()