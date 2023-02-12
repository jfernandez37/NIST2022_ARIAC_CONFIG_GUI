import tkinter as tk
from tkinter import ttk
from functools import partial
options=["1","2","3"]
agvList=["agv1", "agv2", "agv3", "agv4"]
partTypes=["sensor", "pump", "regulator", "battery"]
partColors=['green', 'red', 'purple','blue','orange']
trays=["Tray 0","Tray 1","Tray 2","Tray 3","Tray 4","Tray 5","Tray 6","Tray 7","Tray 8","Tray 9"]
slots=["Slot 1", "Slot 2", "Slot 3", "Slot 4", "Slot 5", "Slot 6"]
agvOptions=["1","2","3","4"]
allPartTypes=["sensor", "pump", "regulator", "battery"]
allPartColors=['green', 'red', 'purple','blue','orange']
robotTypes=["ceiling_robot","floor_robot"]
destinations=["warehouse", "as1", "as2","as3","as4","kitting"]
stations=["as1","as2","as3","as4"]
sensBOCategories=["time-based","during kitting", "during assembly","after kitting", "after assembly"]
conditionTypes=['','time','partPlace','submission']
usedIds=["ABCDFGHI"] #Temporary for testing
LEFTCOLUMN=1
MIDDLECOLUMN=2
RIGHTCOLUMN=3
agv1Quadrants=["1","2","3","4"] # available quadrants for agv1
agv2Quadrants=["1","2","3","4"] # available quadrants for agv2
agv3Quadrants=["1","2","3","4"] # available quadrants for agv3
agv4Quadrants=["1","2","3","4"] # available quadrants for agv4
agvTrayIds=["0","1","2","3","4","5","6"] # all options for tray ids for agvs
def addNewKTray(topLabel, tray1, slot1, tray1Menu, slot1Menu,tray2, slot2, tray2Menu, slot2Menu,tray3, slot3, tray3Menu, slot3Menu,tray4, slot4, tray4Menu, slot4Menu,tray5, slot5, tray5Menu, slot5Menu,tray6, slot6, tray6Menu, slot6Menu, counter, availableTrays, availableSlots):
    if len(counter)==0:
        tray1.set(availableTrays[0])
        slot1.set(availableSlots[0])
        availableTrays.remove(tray1.get())
        availableSlots.remove(slot1.get())
        tray1Menu.grid(column=LEFTCOLUMN, row=2)
        slot1Menu.grid(column=RIGHTCOLUMN, row=2)
    elif len(counter)==1:
        tray2.set(availableTrays[0])
        slot2.set(availableSlots[0])
        availableTrays.remove(tray2.get())
        availableSlots.remove(slot2.get())
        tray2Menu.grid(column=LEFTCOLUMN, row=3)
        slot2Menu.grid(column=RIGHTCOLUMN, row=3)
    elif len(counter)==2:
        tray3.set(availableTrays[0])
        slot3.set(availableSlots[0])
        availableTrays.remove(tray3.get())
        availableSlots.remove(slot3.get())
        tray3Menu.grid(column=LEFTCOLUMN, row=4)
        slot3Menu.grid(column=RIGHTCOLUMN, row=4)
    elif len(counter)==3:
        tray4.set(availableTrays[0])
        slot4.set(availableSlots[0])
        availableTrays.remove(tray4.get())
        availableSlots.remove(slot4.get())
        tray4Menu.grid(column=LEFTCOLUMN, row=5)
        slot4Menu.grid(column=RIGHTCOLUMN, row=5)
    elif len(counter)==4:
        tray5.set(availableTrays[0])
        slot5.set(availableSlots[0])
        availableTrays.remove(tray5.get())
        availableSlots.remove(slot5.get())
        tray5Menu.grid(column=LEFTCOLUMN, row=6)
        slot5Menu.grid(column=RIGHTCOLUMN, row=6)
    elif len(counter)==5:
        tray6.set(availableTrays[0])
        slot6.set(availableSlots[0])
        availableTrays.remove(tray6.get())
        availableSlots.remove(slot6.get())
        tray6Menu.grid(column=LEFTCOLUMN, row=7)
        slot6Menu.grid(column=RIGHTCOLUMN, row=7)
    counter.append(0)

def removeKTray(tray1, slot1, tray1Menu, slot1Menu,tray2, slot2, tray2Menu, slot2Menu,tray3, slot3, tray3Menu, slot3Menu,tray4, slot4, tray4Menu, slot4Menu,tray5, slot5, tray5Menu, slot5Menu,tray6, slot6, tray6Menu, slot6Menu, counter, availableTrays, availableSlots):
    if len(counter)==1:
        availableTrays.append(tray1.get())
        availableSlots.append(slot1.get())
        tray1.set("")
        slot1.set("")
        tray1Menu.grid_forget()
        slot1Menu.grid_forget()
    elif len(counter)==2:
        availableTrays.append(tray2.get())
        availableSlots.append(slot2.get())
        tray2.set("")
        slot2.set("")
        tray2Menu.grid_forget()
        slot2Menu.grid_forget()
    elif len(counter)==3:
        availableTrays.append(tray3.get())
        availableSlots.append(slot3.get())
        tray3.set("")
        slot3.set("")
        tray3Menu.grid_forget()
        slot3Menu.grid_forget()
    elif len(counter)==4:
        availableTrays.append(tray4.get())
        availableSlots.append(slot4.get())
        tray4.set("")
        slot4.set("")
        tray4Menu.grid_forget()
        slot4Menu.grid_forget()
    elif len(counter)==5:
        availableTrays.append(tray5.get())
        availableSlots.append(slot5.get())
        tray5.set("")
        slot5.set("")
        tray5Menu.grid_forget()
        slot5Menu.grid_forget()
    elif len(counter)==6:
        availableTrays.append(tray6.get())
        availableSlots.append(slot6.get())
        tray6.set("")
        slot6.set("")
        tray6Menu.grid_forget()
        slot6Menu.grid_forget()
    availableSlots.sort()
    counter.remove(0)

def updateKTrayMenus(tray1, tray1Menu, tray2, tray2Menu, tray3, tray3Menu, tray4, tray4Menu, tray5, tray5Menu, tray6, tray6Menu,counter,removeButton, addButton, a,b,c):
    '''Updates the available trays for kitting trays'''
    menu1=tray1Menu['menu']
    menu1.delete(0, 'end')
    menu2=tray2Menu['menu']
    menu2.delete(0, 'end')
    menu3=tray3Menu['menu']
    menu3.delete(0, 'end')
    menu4=tray4Menu['menu']
    menu4.delete(0, 'end')
    menu5=tray5Menu['menu']
    menu5.delete(0, 'end')
    menu6=tray6Menu['menu']
    menu6.delete(0, 'end')
    currentTrayVals=[tray1.get(), tray2.get(), tray3.get(), tray4.get(), tray5.get(), tray6.get()]
    for tray in trays:
        if (tray not in currentTrayVals) or tray==tray1.get():
            menu1.add_command(label=tray, command=lambda tray=tray: tray1.set(tray))
        if (tray not in currentTrayVals) or tray==tray2.get():
            menu2.add_command(label=tray, command=lambda tray=tray: tray2.set(tray))
        if (tray not in currentTrayVals) or tray==tray3.get():
            menu3.add_command(label=tray, command=lambda tray=tray: tray3.set(tray))
        if (tray not in currentTrayVals) or tray==tray4.get():
            menu4.add_command(label=tray, command=lambda tray=tray: tray4.set(tray))
        if (tray not in currentTrayVals) or tray==tray5.get():
            menu5.add_command(label=tray, command=lambda tray=tray: tray5.set(tray))
        if (tray not in currentTrayVals) or tray==tray6.get():
            menu6.add_command(label=tray, command=lambda tray=tray: tray6.set(tray))
    if tray6.get()!="":
        addButton.grid_forget()
    else:
        addButton.grid_forget()
        addButton.grid(column=MIDDLECOLUMN, row=8)
    if tray1.get()=="":
        removeButton.grid_forget()
    else:
        removeButton.grid_forget()
        removeButton.grid(column=MIDDLECOLUMN, row=9)
    

def updateKSlotMenus(slot1, slot1Menu, slot2, slot2Menu, slot3, slot3Menu, slot4, slot4Menu, slot5, slot5Menu, slot6, slot6Menu,a,b,c):
    '''Updates the available slots for kitting slots'''
    menu1=slot1Menu['menu']
    menu1.delete(0, 'end')
    menu2=slot2Menu['menu']
    menu2.delete(0, 'end')
    menu3=slot3Menu['menu']
    menu3.delete(0, 'end')
    menu4=slot4Menu['menu']
    menu4.delete(0, 'end')
    menu5=slot5Menu['menu']
    menu5.delete(0, 'end')
    menu6=slot6Menu['menu']
    menu6.delete(0, 'end')
    currentSlotVals=[slot1.get(), slot2.get(), slot3.get(), slot4.get(), slot5.get(), slot6.get()]
    for slot in slots:
        if (slot not in currentSlotVals) or slot==slot1.get():
            menu1.add_command(label=slot, command=lambda slot=slot: slot1.set(slot))
        if (slot not in currentSlotVals) or slot==slot2.get():
            menu2.add_command(label=slot, command=lambda slot=slot: slot2.set(slot))
        if (slot not in currentSlotVals) or slot==slot3.get():
            menu3.add_command(label=slot, command=lambda slot=slot: slot3.set(slot))
        if (slot not in currentSlotVals) or slot==slot4.get():
            menu4.add_command(label=slot, command=lambda slot=slot: slot4.set(slot))
        if (slot not in currentSlotVals) or slot==slot5.get():
            menu5.add_command(label=slot, command=lambda slot=slot: slot5.set(slot))
        if (slot not in currentSlotVals) or slot==slot6.get():
            menu6.add_command(label=slot, command=lambda slot=slot: slot6.set(slot))

def kittingTrayWidgets(setupFrame, kittingTrayCounter, availableSlots, availableTrays, trayVals, slotVals):
    kittingTrayLabel=tk.Label(setupFrame, text="Kitting Trays")
    kittingTrayLabel.grid(column=2, row=2)
    #variables and menus for the trays and slots
    tray1=tk.StringVar()
    tray2=tk.StringVar()
    tray3=tk.StringVar()
    tray4=tk.StringVar()
    tray5=tk.StringVar()
    tray6=tk.StringVar()
    slot1=tk.StringVar()
    slot2=tk.StringVar()
    slot3=tk.StringVar()
    slot4=tk.StringVar()
    slot5=tk.StringVar()
    slot6=tk.StringVar()
    tray1Menu=tk.OptionMenu(setupFrame, tray1, *availableTrays)
    tray2Menu=tk.OptionMenu(setupFrame, tray2, *availableTrays)
    tray3Menu=tk.OptionMenu(setupFrame, tray3, *availableTrays)
    tray4Menu=tk.OptionMenu(setupFrame, tray4, *availableTrays)
    tray5Menu=tk.OptionMenu(setupFrame, tray5, *availableTrays)
    tray6Menu=tk.OptionMenu(setupFrame, tray6, *availableTrays)
    slot1Menu=tk.OptionMenu(setupFrame, slot1, *availableSlots)
    slot2Menu=tk.OptionMenu(setupFrame, slot2, *availableSlots)
    slot3Menu=tk.OptionMenu(setupFrame, slot3, *availableSlots)
    slot4Menu=tk.OptionMenu(setupFrame, slot4, *availableSlots)
    slot5Menu=tk.OptionMenu(setupFrame, slot5, *availableSlots)
    slot6Menu=tk.OptionMenu(setupFrame, slot6, *availableSlots)
    if trayVals[0]!="":
        tray1.set(trayVals[0])
        slot1.set(slotVals[0])
        tray1Menu.grid(column=LEFTCOLUMN, row=3)
        slot1Menu.grid(column=RIGHTCOLUMN, row=3)
    if trayVals[1]!="":
        tray2.set(trayVals[1])
        slot2.set(slotVals[1])
        tray2Menu.grid(column=LEFTCOLUMN, row=4)
        slot2Menu.grid(column=RIGHTCOLUMN, row=4)
    if trayVals[2]!="":
        tray3.set(trayVals[2])
        slot3.set(slotVals[2])
        tray3Menu.grid(column=LEFTCOLUMN, row=5)
        slot3Menu.grid(column=RIGHTCOLUMN, row=5)
    if trayVals[3]!="":
        tray4.set(trayVals[3])
        slot4.set(slotVals[3])
        tray4Menu.grid(column=LEFTCOLUMN, row=6)
        slot4Menu.grid(column=RIGHTCOLUMN, row=6)
    if trayVals[4]!="":
        tray5.set(trayVals[4])
        slot5.set(slotVals[4])
        tray5Menu.grid(column=LEFTCOLUMN, row=7)
        slot5Menu.grid(column=RIGHTCOLUMN, row=7)
    if trayVals[5]!="":
        tray6.set(trayVals[5])
        slot6.set(slotVals[5])
        tray6Menu.grid(column=LEFTCOLUMN, row=8)
        slot6Menu.grid(column=RIGHTCOLUMN, row=8)
    #add new and remove buttons
    if len(kittingTrayCounter)==0:
        addNewKTray(kittingTrayLabel, tray1, slot1, tray1Menu, slot1Menu,tray2, slot2, tray2Menu, slot2Menu,tray3, slot3, tray3Menu, slot3Menu,tray4, slot4, tray4Menu, slot4Menu,tray5, slot5, tray5Menu, slot5Menu,tray6, slot6, tray6Menu, slot6Menu, kittingTrayCounter, availableTrays, availableSlots)
    add_new_tray=partial(addNewKTray,kittingTrayLabel, tray1, slot1, tray1Menu, slot1Menu,tray2, slot2, tray2Menu, slot2Menu,tray3, slot3, tray3Menu, slot3Menu,tray4, slot4, tray4Menu, slot4Menu,tray5, slot5, tray5Menu, slot5Menu,tray6, slot6, tray6Menu, slot6Menu, kittingTrayCounter, availableTrays, availableSlots)
    addTrayButton=tk.Button(setupFrame, text="Add New Tray", command=add_new_tray)
    addTrayButton.grid(column=MIDDLECOLUMN, row=8)
    remove_tray=partial(removeKTray,tray1, slot1, tray1Menu, slot1Menu,tray2, slot2, tray2Menu, slot2Menu,tray3, slot3, tray3Menu, slot3Menu,tray4, slot4, tray4Menu, slot4Menu,tray5, slot5, tray5Menu, slot5Menu,tray6, slot6, tray6Menu, slot6Menu, kittingTrayCounter, availableTrays, availableSlots)
    removeTrayButton=tk.Button(setupFrame, text="Remove Tray", command=remove_tray)
    removeTrayButton.grid(column=MIDDLECOLUMN, row=9)
    update_all_tray_menus=partial(updateKTrayMenus,tray1, tray1Menu, tray2, tray2Menu, tray3, tray3Menu, tray4, tray4Menu, tray5, tray5Menu, tray6, tray6Menu,kittingTrayCounter,removeTrayButton, addTrayButton)
    update_all_slot_menus=partial(updateKSlotMenus, slot1, slot1Menu, slot2, slot2Menu, slot3, slot3Menu, slot4, slot4Menu, slot5, slot5Menu, slot6, slot6Menu)
    tray1.trace('w', update_all_tray_menus)
    tray2.trace('w', update_all_tray_menus)
    tray3.trace('w', update_all_tray_menus)
    tray4.trace('w', update_all_tray_menus)
    tray5.trace('w', update_all_tray_menus)
    tray6.trace('w', update_all_tray_menus)
    slot1.trace('w', update_all_slot_menus)
    slot2.trace('w', update_all_slot_menus)
    slot3.trace('w', update_all_slot_menus)
    slot4.trace('w', update_all_slot_menus)
    slot5.trace('w', update_all_slot_menus)
    slot6.trace('w', update_all_slot_menus)
    trayVals.clear()
    slotVals.clear()
    trayVals.append(tray1.get())
    trayVals.append(tray2.get())
    trayVals.append(tray3.get())
    trayVals.append(tray4.get())
    trayVals.append(tray5.get())
    trayVals.append(tray6.get())
    slotVals.append(slot1.get())
    slotVals.append(slot2.get())
    slotVals.append(slot3.get())
    slotVals.append(slot4.get())
    slotVals.append(slot5.get())
    slotVals.append(slot6.get())

def timeEntry(timeFrame, timeVar, timeVal):
    timeVar.set(timeVal)
    timeLabel=tk.Label(timeFrame, text="This is a time label test")
    timeLabel.grid(column=MIDDLECOLUMN)
    timeEntry=tk.Entry(timeFrame, textvariable=timeVar)
    timeEntry.grid(column=MIDDLECOLUMN)


def removeFrame(frameFlag, mainWind):
    frameFlag.set('1')
    mainWind.destroy()

def switchPartMenu(partVals, partWidgets, partFlag, agvTrayWidgetsArr, agvTrayValsArr):
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
    switchPartMenu(partVals, partWidgets, partFlag, agvTrayWidgetsArr, agvTrayValsArr)
    print(chosenOptions)

def partsWidgets(partsFrame, partFlag, agv1Quadrants,agv2Quadrants,agv3Quadrants,agv4Quadrants,agvTrayWidgetsArr, agvTrayValsArr):
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
    show_option_menu=partial(switchPartMenu,partVals, partWidgets, partFlag, agvTrayWidgetsArr, agvTrayValsArr)
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

def robotMalfunctionMenu(allChallengeWidgetsArr,presentChallengeWidgets):
    for widget in presentChallengeWidgets:
        widget.grid_forget()
    presentChallengeWidgets.clear()
    for index in range(4): #how many widgets there are for robot malfunction
        allChallengeWidgetsArr[index].grid(column=2, row=1+index)
        presentChallengeWidgets.append(allChallengeWidgetsArr[index])

def faultyPartMenu(allChallengeWidgetsArr,presentChallengeWidgets):
    for widget in presentChallengeWidgets:
        widget.grid_forget()
    presentChallengeWidgets.clear()
    for index in range(6): #how many widgets there are for faulty part
        allChallengeWidgetsArr[index+4].grid(column=2, row=1+index)
        presentChallengeWidgets.append(allChallengeWidgetsArr[index+4])

def droppedPartMenu(allChallengeWidgetsArr,presentChallengeWidgets):
    for widget in presentChallengeWidgets:
        widget.grid_forget()
    presentChallengeWidgets.clear()
    for index in range(9): #how many widgets there are for dropped part
        allChallengeWidgetsArr[index+10].grid(column=2, row=1+index)
        presentChallengeWidgets.append(allChallengeWidgetsArr[index+10])

def sensorBlackoutMenu(allChallengeWidgetsArr,presentChallengeWidgets):
    for widget in presentChallengeWidgets:
        widget.grid_forget()
    presentChallengeWidgets.clear()
    for index in range(10): #how many widgets there are for dropped part
        allChallengeWidgetsArr[index+19].grid(column=2, row=1+index)
        presentChallengeWidgets.append(allChallengeWidgetsArr[index+19])


def chooseChallenge(challengeFrame,allChallengeWidgetsArr,presentChallengeWidgets):
    new_robot_malfunction=partial(robotMalfunctionMenu, allChallengeWidgetsArr,presentChallengeWidgets)
    newRobotMalfunctionButton=tk.Button(challengeFrame, text="Add new robot malfunction", command=new_robot_malfunction)
    newRobotMalfunctionButton.grid(column=1)
    new_faulty_part=partial(faultyPartMenu, allChallengeWidgetsArr, presentChallengeWidgets)
    newFaultyPartButton=tk.Button(challengeFrame, text="Add new faulty part", command=new_faulty_part)
    newFaultyPartButton.grid(column=1)
    new_dropped_part=partial(droppedPartMenu, allChallengeWidgetsArr, presentChallengeWidgets)
    newDroppedPartButton=tk.Button(challengeFrame, text="Add new dropped part", command=new_dropped_part)
    newDroppedPartButton.grid(column=1)
    new_sensor_blackout=partial(sensorBlackoutMenu, allChallengeWidgetsArr, presentChallengeWidgets)
    newSensorBlackoutButton=tk.Button(challengeFrame, text="Add new sensor blackout", command=new_sensor_blackout)
    newSensorBlackoutButton.grid(column=1)

def allChallengeWidgets(challengesFrame,allChallengeWidgetsArr):
    #robot malfunction
    rmDuration=tk.StringVar()
    rmDuration.set("0")
    rmDurationLabel=tk.Label(challengesFrame, text="Enter the duration of the robot malfunction")
    rmDurationLabel.grid_forget()
    rmDurationEntry=tk.Entry(challengesFrame, textvariable=rmDuration)
    rmDurationEntry.grid_forget()
    floorRobot=tk.StringVar()
    floorRobot.set("0")
    ceilRobot=tk.StringVar()
    ceilRobot.set("0")
    floorRobotCB=tk.Checkbutton(challengesFrame, text="Floor robot", variable=floorRobot, onvalue="1", offvalue="0", height=1, width=20)
    floorRobotCB.grid_forget()
    ceilRobotCB=tk.Checkbutton(challengesFrame, text="Ceiling robot", variable=ceilRobot, onvalue="1", offvalue="0", height=1, width=20)
    ceilRobotCB.grid_forget()
    allChallengeWidgetsArr.append(rmDurationLabel)
    allChallengeWidgetsArr.append(rmDurationEntry)
    allChallengeWidgetsArr.append(floorRobotCB)
    allChallengeWidgetsArr.append(ceilRobotCB)
    #faulty Part
    currentOrderID=tk.StringVar()
    currentOrderID.set(usedIds[0])
    orderIDLabel=tk.Label(challengesFrame, text="Select the order ID for the faulty part")
    orderIDLabel.grid_forget()
    orderIDMenu=tk.OptionMenu(challengesFrame, currentOrderID, *usedIds)
    orderIDMenu.grid_forget()
    q1=tk.StringVar()
    q1.set('0')
    q2=tk.StringVar()
    q2.set('0')
    q3=tk.StringVar()
    q3.set('0')
    q4=tk.StringVar()
    q4.set('0')
    q1CB=tk.Checkbutton(challengesFrame, text="Quadrant 1", variable=q1, onvalue="1", offvalue="0", height=1, width=20)
    q1CB.grid_forget()
    q2CB=tk.Checkbutton(challengesFrame, text="Quadrant 2", variable=q2, onvalue="1", offvalue="0", height=1, width=20)
    q2CB.grid_forget()
    q3CB=tk.Checkbutton(challengesFrame, text="Quadrant 3", variable=q3, onvalue="1", offvalue="0", height=1, width=20)
    q3CB.grid_forget()
    q4CB=tk.Checkbutton(challengesFrame, text="Quadrant 4", variable=q4, onvalue="1", offvalue="0", height=1, width=20)
    q4CB.grid_forget()
    allChallengeWidgetsArr.append(orderIDLabel)
    allChallengeWidgetsArr.append(orderIDMenu)
    allChallengeWidgetsArr.append(q1CB)
    allChallengeWidgetsArr.append(q2CB)
    allChallengeWidgetsArr.append(q3CB)
    allChallengeWidgetsArr.append(q4CB)
    #dropped part
    robotType=tk.StringVar()
    robotType.set(robotTypes[0])
    robotTypeLabel=tk.Label(challengesFrame, text="Select the robot type for the dropped part")
    robotTypeLabel.grid_forget()
    robotTypeMenu=tk.OptionMenu(challengesFrame, robotType, *robotTypes)
    robotTypeMenu.grid_forget()
    partType=tk.StringVar()
    partType.set(allPartTypes[0])
    partTypeLabel=tk.Label(challengesFrame, text="Select the type of part")
    partTypeLabel.grid_forget()
    partTypeMenu=tk.OptionMenu(challengesFrame, partType, *allPartTypes)
    partTypeMenu.grid_forget()
    partColor=tk.StringVar()
    partColor.set(allPartColors[0])
    partColorLabel=tk.Label(challengesFrame, text="Select the color of the part")
    partColorLabel.grid_forget()
    partColorMenu=tk.OptionMenu(challengesFrame, partColor, *allPartColors)
    partColorMenu.grid_forget()
    dropAfterNum=tk.StringVar()
    dropAfterNum.set("0")
    dropAfterNumLabel=tk.Label(challengesFrame, text="Set the number to drop the part after")
    dropAfterNumLabel.grid_forget()
    dropAfterNumEntry=tk.Entry(challengesFrame, textvariable=dropAfterNum)
    dropAfterNumEntry.grid_forget()
    dropAfterTime=tk.StringVar()
    dropAfterTime.set('0')
    dropAfterTimeLabel=tk.Label(challengesFrame,text="Set the time to drop the part after")
    dropAfterTimeLabel.grid_forget()
    dropAfterTimeEntry=tk.Entry(challengesFrame, textvariable=dropAfterTime)
    dropAfterTimeEntry.grid_forget()
    allChallengeWidgetsArr.append(robotTypeLabel)
    allChallengeWidgetsArr.append(robotTypeMenu)
    allChallengeWidgetsArr.append(partTypeLabel)
    allChallengeWidgetsArr.append(partColorLabel)
    allChallengeWidgetsArr.append(partColorMenu)
    allChallengeWidgetsArr.append(dropAfterNumLabel)
    allChallengeWidgetsArr.append(dropAfterNumEntry)
    allChallengeWidgetsArr.append(dropAfterTimeLabel) 
    allChallengeWidgetsArr.append(dropAfterTimeEntry)
    #sensor blackout
    category=tk.StringVar()
    category.set(sensBOCategories[0])
    categoryLabel=tk.Label(challengesFrame, text="Choose the category for the sensor blackout")
    categoryLabel.grid_forget()
    categoryMenu=tk.OptionMenu(challengesFrame, category, *sensBOCategories)
    categoryMenu.grid_forget()
    sbDuration=tk.StringVar()
    sbDuration.set('0')
    sbDurationLabel=tk.Label(challengesFrame, text="Enter the duration for the sensor blackout")
    sbDurationLabel.grid_forget()
    sbDurationEntry=tk.Entry(challengesFrame, textvariable=sbDuration)
    sbDurationEntry.grid_forget()
    sensor1=tk.StringVar()
    sensor2=tk.StringVar()
    sensor3=tk.StringVar()
    sensor4=tk.StringVar()
    sensor5=tk.StringVar()
    sensor6=tk.StringVar()
    sensor1.set('0')
    sensor2.set('0')
    sensor3.set('0')
    sensor4.set('0')
    sensor5.set('0')
    sensor6.set('0')
    sensor1CB=tk.Checkbutton(challengesFrame, text="break beam", variable=sensor1, onvalue="1", offvalue="0", height=1, width=20)
    sensor1CB.grid_forget()
    sensor2CB=tk.Checkbutton(challengesFrame, text="proximity", variable=sensor2, onvalue="1", offvalue="0", height=1, width=20)
    sensor2CB.grid_forget()
    sensor3CB=tk.Checkbutton(challengesFrame, text="laser profiler", variable=sensor3, onvalue="1", offvalue="0", height=1, width=20)
    sensor3CB.grid_forget()
    sensor4CB=tk.Checkbutton(challengesFrame, text="lidar", variable=sensor4, onvalue="1", offvalue="0", height=1, width=20)
    sensor4CB.grid_forget()
    sensor5CB=tk.Checkbutton(challengesFrame, text="camera", variable=sensor5, onvalue="1", offvalue="0", height=1, width=20)
    sensor5CB.grid_forget()
    sensor6CB=tk.Checkbutton(challengesFrame, text="logical camera", variable=sensor6, onvalue="1", offvalue="0", height=1, width=20)
    sensor6CB.grid_forget()
    allChallengeWidgetsArr.append(categoryLabel)
    allChallengeWidgetsArr.append(categoryMenu)
    allChallengeWidgetsArr.append(sbDurationLabel)
    allChallengeWidgetsArr.append(sbDurationEntry)
    allChallengeWidgetsArr.append(sensor1CB)
    allChallengeWidgetsArr.append(sensor2CB)
    allChallengeWidgetsArr.append(sensor3CB)
    allChallengeWidgetsArr.append(sensor4CB)
    allChallengeWidgetsArr.append(sensor5CB)
    allChallengeWidgetsArr.append(sensor6CB)
    #condition
    condition=tk.StringVar()
    condition.set(conditionTypes[0])
    conditionLabel=tk.Label(challengesFrame, text="Select a condition for the order")
    conditionLabel.grid_forget()
    conditionMenu=tk.OptionMenu(challengesFrame, condition, *conditionTypes)
    conditionMenu.grid_forget()
    conTime=tk.StringVar()
    conTime.set('')
    conTimeLabel=tk.Label(challengesFrame, text="Enter the time")
    conTimeLabel.grid_forget()
    conTimeEntry=tk.Entry(challengesFrame, textvariable=conTime)
    conTimeEntry.grid_forget()
    conAgv=tk.StringVar()
    conAgv.set("")
    conAgvLabel=tk.Label(challengesFrame, text="Choose the agv")
    conAgvLabel.grid_forget()
    conAgvMenu=tk.OptionMenu(challengesFrame, conAgv, *agvOptions)
    conAgvMenu.grid_forget()
    conPartType=tk.StringVar()
    conPartType.set("")
    conPartTypeLabel=tk.Label(challengesFrame, text="Select the type of part")
    conPartTypeLabel.grid_forget()
    conPartTypeMenu=tk.OptionMenu(challengesFrame, conPartType, *allPartTypes)
    conPartTypeMenu.grid_forget()
    conPartColor=tk.StringVar()
    conPartColor.set("")
    conPartColorLabel=tk.Label(challengesFrame, text="Select the color of the part")
    conPartColorLabel.grid_forget()
    conPartColorMenu=tk.OptionMenu(challengesFrame, conPartColor, *allPartColors)
    conPartColorMenu.grid_forget()
    annID=tk.StringVar()
    annID.set("")
    annIDLabel=tk.Label(challengesFrame, text="Select the order ID")
    annIDLabel.grid_forget()
    annIDMenu=tk.OptionMenu(challengesFrame, annID, *usedIds)
    annIDMenu.grid_forget()

def agvTrayWidgets(partsFrame, agvTrayWidgetsArr, agvTrayValsArr):
    agv1TrayId=tk.StringVar()
    agv1TrayId.set(agvTrayIds[0])
    agv2TrayId=tk.StringVar()
    agv2TrayId.set(agvTrayIds[0])
    agv3TrayId=tk.StringVar()
    agv3TrayId.set(agvTrayIds[0])
    agv4TrayId=tk.StringVar()
    agv4TrayId.set(agvTrayIds[0])
    agv1TrayLabel=tk.Label(partsFrame, text="Select the tray Id for agv1")
    agv1TrayLabel.pack()
    agv1TrayIdSelect=tk.OptionMenu(partsFrame, agv1TrayId, *agvTrayIds)
    agv1TrayIdSelect.pack()
    agv2TrayLabel=tk.Label(partsFrame, text="Select the tray Id for agv2")
    agv2TrayLabel.pack()
    agv2TrayIdSelect=tk.OptionMenu(partsFrame, agv2TrayId, *agvTrayIds)
    agv2TrayIdSelect.pack()
    agv3TrayLabel=tk.Label(partsFrame, text="Select the tray Id for agv3")
    agv3TrayLabel.pack()
    agv3TrayIdSelect=tk.OptionMenu(partsFrame, agv3TrayId, *agvTrayIds)
    agv3TrayIdSelect.pack()
    agv4TrayLabel=tk.Label(partsFrame, text="Select the tray Id for agv4")
    agv4TrayLabel.pack()
    agv4TrayIdSelect=tk.OptionMenu(partsFrame, agv4TrayId, *agvTrayIds)
    agv4TrayIdSelect.pack()
    agvTrayValsArr.append(agv1TrayId)
    agvTrayValsArr.append(agv2TrayId)
    agvTrayValsArr.append(agv3TrayId)
    agvTrayValsArr.append(agv4TrayId)
    agvTrayWidgetsArr.append(agv1TrayLabel)
    agvTrayWidgetsArr.append(agv1TrayIdSelect)
    agvTrayWidgetsArr.append(agv2TrayLabel)
    agvTrayWidgetsArr.append(agv2TrayIdSelect)
    agvTrayWidgetsArr.append(agv3TrayLabel)
    agvTrayWidgetsArr.append(agv3TrayIdSelect)
    agvTrayWidgetsArr.append(agv4TrayLabel)
    agvTrayWidgetsArr.append(agv4TrayIdSelect)

def runMainWind(chosenOptions,timeVal):
    presentChallengeWidgets=[]
    allChallengeWidgetsArr=[]
    trayVals=[]
    slotVals=[]
    agvTrayWidgetsArr = []
    agvTrayValsArr = []
    availableTrays=["Tray 0","Tray 1","Tray 2","Tray 3","Tray 4","Tray 5","Tray 6","Tray 7","Tray 8","Tray 9"]
    availableSlots=["Slot 1", "Slot 2", "Slot 3", "Slot 4", "Slot 5", "Slot 6"]
    kittingTrayCounter=[]
    for i in range(6):
        trayVals.append("")
        slotVals.append("")
    mainWind=tk.Tk()
    mainWind.geometry('400x500')
    mainWind.title('notebook testing')

    notebook=ttk.Notebook(mainWind)
    notebook.pack(pady=10, expand=True)

    setupFrame = ttk.Frame(notebook, width=400, height=280)
    

    setupFrame.pack(fill='both', expand=True)

    timeVar=tk.StringVar()
    timeEntry(setupFrame, timeVar, timeVal[0])
    # add frames to notebook

    #kitting trays
    kittingTrayWidgets(setupFrame, kittingTrayCounter, availableSlots, availableTrays, trayVals, slotVals)
    notebook.add(setupFrame, text='Setup')
    partsFrame = ttk.Frame(notebook, width=400, height=280)
    partsFrame.pack(fill='both', expand=True)
    notebook.add(partsFrame, text='Parts')

    binFrame=ttk.Frame(notebook, width=400, height=280)
    binFrame.pack(fill='both', expand=True)
    notebook.add(binFrame, text="Bins")

    convFrame=ttk.Frame(notebook, width=400, height=280)
    convFrame.pack(fill='both', expand=True)
    notebook.add(convFrame, text="Conveyor Belt")

    challengesFrame=ttk.Frame(notebook, width=400, height=280)
    challengesFrame.pack(fill='both', expand=True)
    notebook.add(challengesFrame, text="Challenges")

    #Parts frame
    partFlag=tk.StringVar()
    partFlag.set('0')
    partsWidgets(partsFrame, partFlag, agv1Quadrants,agv2Quadrants,agv3Quadrants,agv4Quadrants,agvTrayWidgetsArr, agvTrayValsArr)
    agvTrayWidgets(partsFrame, agvTrayWidgetsArr, agvTrayValsArr)

    #Bins frame

    #Challenges frame
    allChallengeWidgets(challengesFrame,allChallengeWidgetsArr)
    chooseChallenge(challengesFrame, allChallengeWidgetsArr,presentChallengeWidgets)
    mainWind.mainloop()

if __name__=="__main__":
    chosenOptions=[]
    timeVal=['0']
    runMainWind(chosenOptions, timeVal)