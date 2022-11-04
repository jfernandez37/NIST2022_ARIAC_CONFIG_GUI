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

def make_file(wind):
    file=filedialog.asksaveasfile(defaultextension=".yaml", filetypes=[("YAML file", ".yaml")])
    if file:
        fileNameVar.set(str(os.path.abspath(file.name)))
        file.close
        wind.destroy()
    

if __name__=="__main__":
    path=""
    fileNameStr=''
    root = tk.Tk()
    fileNameVar = tk.StringVar()
    save_and_exit = partial(make_file, root)
    save_file = tk.Button(root, text="Save a file", command=save_and_exit)
    save_file.pack()
    root.mainloop()
    print(fileNameVar.get())
    if platform.system()=="Windows":
        brokenPath=fileNameVar.get().split("\\")
        for i in brokenPath[:-1]:
            path+=i+"\\"
        fileNameStr=brokenPath[len(brokenPath)-1]
        print(path)
        print(fileNameStr)
        chdir(path)
        with open(fileNameStr,'a') as o:
            o.write("test")
