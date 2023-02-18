import tkinter as tk
from tkinter import ttk
from functools import partial
from notebookParts import partsWidgets
from notebookBins import binWidgets
from notebookConveyor import convWidgets
from notebookOrders import orderWidgets
from notebookChallenges import allChallengeWidgets, chooseChallenge

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
orderMSGS=[]
orderConditions=[] 
usedIDs=[] 
kittingParts=[] 
assemblyParts=[]
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

    setupFrame = ttk.Frame(notebook, width=800, height=600)
    

    setupFrame.pack(fill='both', expand=True)

    timeVar=tk.StringVar()
    timeEntry(setupFrame, timeVar, timeVal[0])
    # add frames to notebook

    #kitting trays
    kittingTrayWidgets(setupFrame, kittingTrayCounter, availableSlots, availableTrays, trayVals, slotVals)
    notebook.add(setupFrame, text='Setup')
    partsFrame = ttk.Frame(notebook, width=800, height=600)
    partsFrame.pack(fill='both', expand=True)
    notebook.add(partsFrame, text='Parts')

    binFrame=ttk.Frame(notebook, width=800, height=600)
    binFrame.pack(fill='both', expand=True)
    notebook.add(binFrame, text="Bins")

    convFrame=ttk.Frame(notebook, width=800, height=600)
    convFrame.pack(fill='both', expand=True)
    notebook.add(convFrame, text="Conveyor Belt")

    ordersFrame=ttk.Frame(notebook, width=800, height=600)
    ordersFrame.pack(fill='both', expand=True)
    notebook.add(ordersFrame, text="Orders")

    challengesFrame=ttk.Frame(notebook, width=800, height=600)
    challengesFrame.pack(fill='both', expand=True)
    notebook.add(challengesFrame, text="Challenges")

    #Parts frame
    partFlag=tk.StringVar()
    partFlag.set('0')
    partsWidgets(partsFrame, partFlag, agv1Quadrants,agv2Quadrants,agv3Quadrants,agv4Quadrants,agvTrayWidgetsArr, agvTrayValsArr, chosenOptions)
    agvTrayWidgets(partsFrame, agvTrayWidgetsArr, agvTrayValsArr)

    #Bins frame
    bin1Slots=[] # holds the available slots for bin1
    bin2Slots=[] # holds the available slots for bin2
    bin3Slots=[] # holds the available slots for bin3
    bin4Slots=[] # holds the available slots for bin4
    bin5Slots=[] # holds the available slots for bin5
    bin6Slots=[] # holds the available slots for bin6
    bin7Slots=[] # holds the available slots for bin7
    bin8Slots=[] # holds the available slots for bin8
    for i in range(9):
        bin1Slots.append(str(i+1))
        bin2Slots.append(str(i+1))
        bin3Slots.append(str(i+1))
        bin4Slots.append(str(i+1))
        bin5Slots.append(str(i+1))
        bin6Slots.append(str(i+1))
        bin7Slots.append(str(i+1))
        bin8Slots.append(str(i+1))
    binWidgets(binFrame,bin1Slots,bin2Slots,bin3Slots,bin4Slots,bin5Slots,bin6Slots,bin7Slots,bin8Slots)
    
    #Conveyor fame
    convWidgets(convFrame)
    
    #Orders frame
    orderWidgets(ordersFrame, orderMSGS,orderConditions, usedIDs, kittingParts, assemblyParts)
    #Challenges frame
    allChallengeWidgets(challengesFrame,allChallengeWidgetsArr)
    chooseChallenge(challengesFrame, allChallengeWidgetsArr,presentChallengeWidgets)
    mainWind.mainloop()

if __name__=="__main__":
    chosenOptions=[]
    timeVal=['0']
    runMainWind(chosenOptions, timeVal)