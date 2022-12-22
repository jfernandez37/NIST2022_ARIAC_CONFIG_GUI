from tkinter import filedialog
import platform
import os

if platform.system()=="Windows": #allows paths as inputs for linux
    invalidFileChar = " /~`,;\"\'\\!@#$%^&*()+=[]"  # characters not allowed in file names for windows
else:
    invalidFileChar = " `,;\"\'\\!@#$%^&*()+=[]"  # characters not allowed in file names for linux

def make_file(wind, fileNameVar):
    """Used for making a file for the user"""
    file=filedialog.asksaveasfile(defaultextension=".yaml", filetypes=[("YAML file", ".yaml")])
    if file:
        if str(os.path.abspath(file.name))!='':
            fileNameVar.set(str(os.path.abspath(file.name)))
            file.close
            wind.destroy()


def correct_file_name(tempFileName, a, b , c):  # deletes any invalid characters in file name
    """This function removes any characters which can not be used in the file name. It does so as the user is typing. Not needed anymore"""
    tempStr = tempFileName.get()
    for char in invalidFileChar:
        if char in tempStr:
            tempStr = tempStr.replace(char, '')
    tempFileName.set(tempStr)