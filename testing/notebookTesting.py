import tkinter as tk
from tkinter import ttk
from functools import partial
options=["1","2","3"]
def timeTest(timeFrame, timeVar, timeVal):
    timeVar.set(timeVal)
    timeEntry=tk.Entry(timeFrame, textvariable=timeVar)
    timeEntry.pack()

def removeFrame(frameFlag, mainWind):
    frameFlag.set('1')
    mainWind.destroy()

def switchPartMenu(partEntry, partOptionMenu,partFlag, partOption):
    if partFlag.get()=="0":
        partOption.set(options[0])
        partEntry.pack_forget()
        partOptionMenu.pack()
        partFlag.set('1')
    else:
        partOption.set('')
        partEntry.pack()
        partOptionMenu.pack_forget()
        partFlag.set('0')

def showAndHideButton(switchPartMenuButton, saveButton, partOption, partOptionFlag,a,b,c):
    print("test")
    if partOption.get()=="":
        switchPartMenuButton.pack()
        saveButton.pack_forget()
        partOptionFlag.set('0')
    elif partOptionFlag.get()=="0":
        saveButton.pack()
        switchPartMenuButton.pack_forget()
        partOptionFlag.set('1')
        

def savePartOption(partEntry, partOptionMenu, partFlag, partOption, chosenOptions):
    chosenOptions.append(partOption.get())
    switchPartMenu(partEntry, partOptionMenu,partFlag, partOption)
    print(chosenOptions)

def runMainWind(timeVal, frameFlag):
    chosenOptions=[]
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
    partFlag=tk.StringVar()
    partFlag.set('0')
    partOptionFlag=tk.StringVar()
    partOptionFlag.set('0')
    partVal=tk.StringVar()
    partVal.set('')
    partEntry=tk.Entry(frame2, textvariable=partVal)
    partEntry.pack()
    partOption=tk.StringVar()
    partOption.set('')
    partOptionMenu=tk.OptionMenu(frame2, partOption, *options)
    partOptionMenu.pack_forget()
    show_option_menu=partial(switchPartMenu, partEntry, partOptionMenu,partFlag, partOption)
    switchPartMenuButton=tk.Button(frame2, text="Switch Window", command=show_option_menu)
    switchPartMenuButton.pack()
    save_option=partial(savePartOption, partEntry, partOptionMenu, partFlag, partOption, chosenOptions)
    saveOptionButton=tk.Button(frame2, text="Save option", command=save_option)
    saveOptionButton.pack_forget()
    switch_buttons=partial(showAndHideButton,switchPartMenuButton, saveOptionButton, partOption, partOptionFlag)
    partOption.trace('w',switch_buttons)
    mainWind.mainloop()

if __name__=="__main__":
    timeVal=['0']
    root=tk.Tk()
    frameFlag=tk.StringVar()
    frameFlag.set('0')
    exitButton=tk.Button(root, text="exit", command=root.destroy)
    exitButton.pack()
    root.mainloop()
    runMainWind(timeVal,frameFlag)