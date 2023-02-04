import tkinter as tk
from tkinter import ttk
from functools import partial
options=["1","2","3"]
agvList=["agv1", "agv2", "agv3", "agv4"]
partTypes=["sensor", "pump", "regulator", "battery"]
partColors=['green', 'red', 'purple','blue','orange']
def timeTest(timeFrame, timeVar, timeVal):
    timeVar.set(timeVal)
    timeEntry=tk.Entry(timeFrame, textvariable=timeVar)
    timeEntry.pack()

def removeFrame(frameFlag, mainWind):
    frameFlag.set('1')
    mainWind.destroy()

def switchPartMenu(partEntry, partVals, partWidgets, partFlag):
    if partFlag.get()=="0":
        partVals[0].set(agvList[0])
        partVals[1].set(partTypes[0])
        partVals[2].set(partColors[0])
        partVals[3].set('0')
        for widget in partWidgets:
            widget.pack()
        partEntry.pack_forget()
        partFlag.set('1')
    else:
        for val in partVals:
            val.set('')
        for widget in partWidgets:
            widget.pack_forget()
        partEntry.pack()
        partFlag.set('0')

def showAndHideButton(switchPartMenuButton, saveButton, val, partOptionFlag,a,b,c):
    if val.get()=="":
        switchPartMenuButton.pack()
        saveButton.pack_forget()
        partOptionFlag.set('0')
    elif partOptionFlag.get()=="0":
        saveButton.pack()
        switchPartMenuButton.pack_forget()
        partOptionFlag.set('1')
        

def savePartOption(partEntry, partWidgets, partFlag, partVals, chosenOptions):
    for val in partVals:
        chosenOptions.append(val.get())
    switchPartMenu(partEntry, partVals, partWidgets, partFlag)
    print(chosenOptions)

def partsWidgets(partsFrame, partFlag):
    partOptionFlag=tk.StringVar()
    partOptionFlag.set('0')
    partVal=tk.StringVar()
    partVal.set('')
    partEntry=tk.Entry(partsFrame, textvariable=partVal)
    partEntry.pack()
    partVals=[]
    partWidgets=[]
    #agv selection
    agvSelection=tk.StringVar()
    agvSelection.set(agvList[0])
    agvSelectLabel=tk.Label(partsFrame, text="Select the agv for the part")
    agvSelectLabel.pack_forget()
    agvSelectMenu=tk.OptionMenu(partsFrame, agvSelection, *agvList)
    agvSelectMenu.pack_forget()
    partVals.append(agvSelection)
    partWidgets.append(agvSelectLabel)
    partWidgets.append(agvSelectMenu)
    #part type selection
    partType=tk.StringVar()
    partType.set(partTypes[0])
    partTypeSelectLabel=tk.Label(partsFrame, text="Select the type of part")
    partTypeSelectLabel.pack_forget()
    partTypeSelectMenu=tk.OptionMenu(partsFrame, partType, *partTypes)
    partTypeSelectMenu.pack_forget()
    partVals.append(partType)
    partWidgets.append(partTypeSelectLabel)
    partWidgets.append(partTypeSelectMenu)
    #part color selection
    partColor=tk.StringVar()
    partColor.set(partColors[0])
    partColorSelectLabel=tk.Label(partsFrame, text="Select the color of the part")
    partColorSelectLabel.pack_forget()
    partColorSelectMenu=tk.OptionMenu(partsFrame, partColor, *partColors)
    partColorSelectMenu.pack_forget()
    partVals.append(partColor)
    partWidgets.append(partColorSelectLabel)
    partWidgets.append(partColorSelectMenu)
    #rotation entry
    partRotation=tk.StringVar()
    partRotation.set('0')
    partRotationLabel=tk.Label(partsFrame, text="Enter the rotation of the part")
    partRotationLabel.pack_forget()
    partRotationEntry=tk.Entry(partsFrame, textvariable=partRotation)
    partRotationEntry.pack_forget()
    partVals.append(partRotation)
    partWidgets.append(partRotationLabel)
    partWidgets.append(partRotationEntry)
    show_option_menu=partial(switchPartMenu, partEntry, partVals, partWidgets, partFlag)
    switchPartMenuButton=tk.Button(partsFrame, text="Switch Window", command=show_option_menu)
    switchPartMenuButton.pack()
    save_option=partial(savePartOption, partEntry, partWidgets, partFlag, partVals, chosenOptions)
    saveOptionButton=tk.Button(partsFrame, text="Save option", command=save_option)
    saveOptionButton.pack_forget()
    switch_buttons=partial(showAndHideButton,switchPartMenuButton, saveOptionButton, partVals[0], partOptionFlag)
    partVals[0].trace('w',switch_buttons)

def printBlank():
    print("")

def chooseChallenge(challengeFrame):
    newRobotMalfunctionButton=tk.Button(challengeFrame, text="Add new robot malfunction")
    newRobotMalfunctionButton.grid(column=1)
    newFaultyPartButton=tk.Button(challengeFrame, text="Add new faulty part")
    newFaultyPartButton.grid(column=1)
    newDroppedPartButton=tk.Button(challengeFrame, text="Add new dropped part")
    newDroppedPartButton.grid(column=1)
    newSensorBlackoutButton=tk.Button(challengeFrame, text="Add new sensor blackout")
    newSensorBlackoutButton.grid(column=1)

def runMainWind(chosenOptions,timeVal):
    mainWind=tk.Tk()
    mainWind.geometry('400x500')
    mainWind.title('notebook testing')

    notebook=ttk.Notebook(mainWind)
    notebook.pack(pady=10, expand=True)

    timeFrame = ttk.Frame(notebook, width=400, height=280)
    

    timeFrame.pack(fill='both', expand=True)
    

    timeLabel=tk.Label(timeFrame, text="This is a time label test")
    timeLabel.pack()

    timeVar=tk.StringVar()
    timeTest(timeFrame, timeVar, timeVal[0])
    # add frames to notebook

    notebook.add(timeFrame, text='Time')
    partsFrame = ttk.Frame(notebook, width=400, height=280)
    partsFrame.pack(fill='both', expand=True)
    notebook.add(partsFrame, text='Parts')

    challengesFrame=ttk.Frame(notebook, width=400, height=280)
    challengesFrame.pack(fill='both', expand=True)
    notebook.add(challengesFrame, text="Challenges")

    #Parts frame
    partFlag=tk.StringVar()
    partFlag.set('0')
    partsWidgets(partsFrame, partFlag)

    #Challenges frame
    chooseChallenge(challengesFrame)

    mainWind.mainloop()

if __name__=="__main__":
    chosenOptions=[]
    timeVal=['0']
    runMainWind(chosenOptions, timeVal)