import tkinter as tk
from tkinter import ttk
from functools import partial
agvList=["agv1", "agv2", "agv3", "agv4"]
partTypes=["sensor", "pump", "regulator", "battery"]
partColors=['green', 'red', 'purple','blue','orange']
def switchPartMenu(agv1Quadrants,partVals, partWidgets, partFlag, agvTrayWidgetsArr, agvTrayValsArr):
    if partFlag.get()=="0":
        partVals[0].set(agvList[0])
        partVals[1].set(partTypes[0])
        partVals[2].set(partColors[0])
        partVals[3].set(agv1Quadrants[0])
        partVals[4].set('0')
        for widget in partWidgets:
            widget.pack()
        for widget in agvTrayWidgetsArr:
            widget.pack_forget()
        partFlag.set('1')
    else:
        for val in partVals:
            val.set('')
        for widget in partWidgets:
            widget.pack_forget()
        for widget in agvTrayWidgetsArr:
            widget.pack()
        partFlag.set('0')

def showAndHideButton(switchPartMenuButton, saveButton, val, partOptionFlag,a,b,c):
    if val.get()=="":
        switchPartMenuButton.pack(side = tk.BOTTOM)
        saveButton.pack_forget()
        partOptionFlag.set('0')
    elif partOptionFlag.get()=="0":
        saveButton.pack(side = tk.BOTTOM)
        switchPartMenuButton.pack_forget()
        partOptionFlag.set('1')
        

def savePartOption(agvSelection,partWidgets, partFlag, partVals, chosenOptions, currentQuadrant, agv1Quadrants, agv2Quadrants, agv3Quadrants, agv4Quadrants, agvTrayWidgetsArr, agvTrayValsArr):
    for val in partVals:
        chosenOptions.append(val.get())
    if agvSelection.get()=='agv1':
        agv1Quadrants.remove(currentQuadrant.get())
    elif agvSelection.get()=='agv2':
        agv2Quadrants.remove(currentQuadrant.get())
    elif agvSelection.get()=='agv3':
        agv3Quadrants.remove(currentQuadrant.get())
    else:
        agv4Quadrants.remove(currentQuadrant.get())
    switchPartMenu(agv1Quadrants,partVals, partWidgets, partFlag, agvTrayWidgetsArr, agvTrayValsArr)
    print(chosenOptions)

def partsWidgets(partsFrame, partFlag, agv1Quadrants,agv2Quadrants,agv3Quadrants,agv4Quadrants,agvTrayWidgetsArr, agvTrayValsArr, chosenOptions):
    partOptionFlag=tk.StringVar()
    partOptionFlag.set('0')
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
    #quadrants
    partQuadrant=tk.StringVar()
    partQuadrant.set(agv1Quadrants[0])
    partQuadrantSelectLabel=tk.Label(partsFrame, text="Select the quadrant of the tray for the part")
    partQuadrantSelectLabel.pack_forget()
    partQuadrantSelectMenu=tk.OptionMenu(partsFrame, partQuadrant, *agv1Quadrants)
    partQuadrantSelectMenu.pack_forget()
    partVals.append(partQuadrant)
    partWidgets.append(partQuadrantSelectLabel)
    partWidgets.append(partQuadrantSelectMenu)
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
    show_option_menu=partial(switchPartMenu,agv1Quadrants,partVals, partWidgets, partFlag, agvTrayWidgetsArr, agvTrayValsArr)
    switchPartMenuButton=tk.Button(partsFrame, text="Add Part", command=show_option_menu)
    switchPartMenuButton.pack(side = tk.BOTTOM)
    save_option=partial(savePartOption, agvSelection,partWidgets, partFlag, partVals, chosenOptions, partQuadrant, agv1Quadrants, agv2Quadrants, agv3Quadrants, agv4Quadrants, agvTrayWidgetsArr, agvTrayValsArr)
    saveOptionButton=tk.Button(partsFrame, text="Save Part", command=save_option)
    saveOptionButton.pack_forget()
    switch_buttons=partial(showAndHideButton,switchPartMenuButton, saveOptionButton, partVals[0], partOptionFlag)
    agv_update_menu=partial(updateAgvQudrants,agvSelection, partQuadrantSelectMenu, partQuadrant, agv1Quadrants,agv2Quadrants,agv3Quadrants,agv4Quadrants)
    agvSelection.trace('w', agv_update_menu)
    partVals[0].trace('w',switch_buttons)

def updateAgvQudrants(agvSelection, quadrantMenu, currentQuadrant, agv1Quadrants,agv2Quadrants,agv3Quadrants,agv4Quadrants,a,b,c):
    '''Updates the available quadrants for each agv'''
    menu=quadrantMenu['menu']
    menu.delete(0,'end')
    if agvSelection.get()=='agv1':
        currentQuadrant.set(agv1Quadrants[0])
        for quadrant in agv1Quadrants:
            menu.add_command(label=quadrant, command=lambda quadrant=quadrant: currentQuadrant.set(quadrant))
    elif agvSelection.get()=='agv2':
        currentQuadrant.set(agv2Quadrants[0])
        for quadrant in agv2Quadrants:
            menu.add_command(label=quadrant, command=lambda quadrant=quadrant: currentQuadrant.set(quadrant))
    elif agvSelection.get()=='agv3':
        currentQuadrant.set(agv3Quadrants[0])
        for quadrant in agv3Quadrants:
            menu.add_command(label=quadrant, command=lambda quadrant=quadrant: currentQuadrant.set(quadrant))
    else:
        currentQuadrant.set(agv4Quadrants[0])
        for quadrant in agv4Quadrants:
            menu.add_command(label=quadrant, command=lambda quadrant=quadrant: currentQuadrant.set(quadrant))