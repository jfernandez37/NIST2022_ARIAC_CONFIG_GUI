import tkinter as tk
from tkinter import filedialog
import tkinter.ttk as ttk
import math
import platform
import os.path
from os import chdir, path
import os
from pathlib import Path
from functools import partial
from turtle import update
from PIL import Image, ImageTk  # needed for images in gui

def toplevel():
    testWind = tk.Toplevel()
    testWind.geometry("500x600")
    left_label = tk.Label(testWind, text="This is a test left")
    left_label.grid(column=0, sticky=tk.W)
    left_label2 = tk.Label(testWind, text="This is a 2nd test left")
    left_label2.grid(column=0, sticky=tk.W)
    right_label = tk.Label(testWind, text="This is a test right")
    right_label.grid(row=0, column=1, sticky=tk.W)
    testWind.mainloop()

if __name__=="__main__":
    root=tk.Tk()
    root.geometry('500x600')
    openTopLevel = tk.Button(root, text="Open toplevel", command=toplevel)
    openTopLevel.pack()
    root.mainloop()
