import tkinter as tk
from tkinter import ttk
from functools import partial
def timeTest(timeFrame, timeVar, timeVal):
    timeVar.set(timeVal)
    timeEntry=tk.Entry(timeFrame, textvariable=timeVar)
    timeEntry.pack()

def removeFrame(frameFlag, mainWind):
    frameFlag.set('1')
    mainWind.destroy()

def runMainWind(timeVal, frameFlag):
    mainWind=tk.Tk()
    mainWind.geometry('400x500')
    mainWind.title('notebook testing')

    notebook=ttk.Notebook(mainWind)
    notebook.pack(pady=10, expand=True)

    frame1 = ttk.Frame(notebook, width=400, height=280)
    

    frame1.pack(fill='both', expand=True)
    

    timeLabel=tk.Label(frame1, text="This is a time label test")
    timeLabel.pack()

    timeVar=tk.StringVar()
    timeTest(frame1, timeVar, timeVal[0])
    # add frames to notebook

    notebook.add(frame1, text='Time')
    if frameFlag.get()=="0":
        frame2 = ttk.Frame(notebook, width=400, height=280)
        frame2.pack(fill='both', expand=True)
        notebook.add(frame2, text='Parts')

    delete_part_frame=partial(removeFrame, frameFlag, mainWind)
    mainWindDeletePartsButton=tk.Button(mainWind, text="remove parts frame", command=delete_part_frame)
    mainWindDeletePartsButton.pack()

    mainWind.mainloop()
    timeVal.clear()
    timeVal.append(timeVar.get())

if __name__=="__main__":
    timeVal=['0']
    root=tk.Tk()
    frameFlag=tk.StringVar()
    frameFlag.set('0')
    exitButton=tk.Button(root, text="exit", command=root.destroy)
    exitButton.pack()
    root.mainloop()
    while(True):
        runMainWind(timeVal,frameFlag)