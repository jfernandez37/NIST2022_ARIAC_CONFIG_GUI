import tkinter as tk
from functools import partial
from Functions.checkCancel import *
from newFunctions.newClasses import *
from newFunctions.timeFunctions import validateTime
from newFunctions.validationFunctions import *
agvOptions=["1","2","3","4"]
allPartTypes=["sensor", "pump", "regulator", "battery"]
allPartColors=['green', 'red', 'purple','blue','orange']
robotTypes=["ceiling_robot","floor_robot"]

def newRobotMalfunction(robotMalfunctions):
    robotMalfunctionWind=tk.Toplevel()
    robotMalfunctionWind.geometry("850x600")
    #duration
    duration=tk.StringVar()
    duration.set("0")
    durationLabel=tk.Label(robotMalfunctionWind, text="Enter the duration of the robot malfunction")
    durationLabel.pack()
    durationEntry=tk.Entry(robotMalfunctionWind, textvariable=duration)
    durationEntry.pack()
    #robots to disable
    floorRobot=tk.StringVar()
    floorRobot.set("0")
    ceilRobot=tk.StringVar()
    ceilRobot.set("0")
    floorRobotCB=tk.Checkbutton(robotMalfunctionWind, text="Floor robot", variable=floorRobot, onvalue="1", offvalue="0", height=1, width=20)
    floorRobotCB.pack()
    ceilRobotCB=tk.Checkbutton(robotMalfunctionWind, text="Ceiling robot", variable=ceilRobot, onvalue="1", offvalue="0", height=1, width=20)
    ceilRobotCB.pack()
    #part type
    partType=tk.StringVar()
    partType.set(allPartTypes[0])
    partTypeLabel=tk.Label(robotMalfunctionWind, text="Select the type of part")
    partTypeLabel.pack()
    partTypeMenu=tk.OptionMenu(robotMalfunctionWind, partType, *allPartTypes)
    partTypeMenu.pack()
    #part color
    partColor=tk.StringVar()
    partColor.set(allPartColors[0])
    partColorLabel=tk.Label(robotMalfunctionWind, text="Select the color of the part")
    partColorLabel.pack()
    partColorMenu=tk.OptionMenu(robotMalfunctionWind, partColor, *allPartColors)
    partColorMenu.pack()
    #agv
    agvSelection=tk.StringVar()
    agvSelection.set(agvOptions[0])
    agvLabel=tk.Label(robotMalfunctionWind, text="Select an agv for the robot malfunciton")
    agvLabel.pack()
    agvMenu=tk.OptionMenu(robotMalfunctionWind, agvSelection, *agvOptions)
    agvMenu.pack()
    #save and cancel buttons
    robotMalfSave=tk.Button(robotMalfunctionWind, text="Save", command=robotMalfunctionWind.destroy)
    robotMalfSave.pack(pady=20)
    robotMalfCancelFlag=tk.StringVar()
    robotMalfCancelFlag.set('0')
    cancel_robot_malf_challenge=partial(exitAndFlag, robotMalfunctionWind, robotMalfCancelFlag)
    robotMalfCancel=tk.Button(robotMalfunctionWind, text="Cancel", command=cancel_robot_malf_challenge)
    robotMalfCancel.pack()
    validate_duration=partial(validateTime, duration)
    duration.trace('w', validate_duration)
    robotMalfunctionWind.mainloop()
    if robotMalfCancelFlag.get()=="0":
        robotsString=""
        if floorRobot.get()=="1" and ceilRobot.get()=="1":
            robotsString="[\'floor_robot\', \'ceiling_robot\']"
        elif floorRobot.get()=="1":
            robotsString="[\'floor_robot\']"
        elif ceilRobot.get()=="1":
            robotsString="[\'ceiling_robot\']"
        robotMalfunctions.append(RobotMalfunction(duration.get(), robotsString, partType.get(), partColor.get(), agvSelection.get()))
    
def newFaultyPart(faultyParts, usedIds):
    faultyPartWind=tk.Toplevel()
    #choose order
    currentOrderID=tk.StringVar()
    currentOrderID.set(usedIds[0])
    orderIDLabel=tk.Label(faultyPartWind, text="Select the order ID for the faulty part")
    orderIDLabel.pack()
    orderIDMenu=tk.OptionMenu(faultyPartWind, currentOrderID, *usedIds)
    orderIDMenu.pack()
    #quadrants
    q1=tk.StringVar()
    q1.set('0')
    q2=tk.StringVar()
    q2.set('0')
    q3=tk.StringVar()
    q3.set('0')
    q4=tk.StringVar()
    q4.set('0')
    q1CB=tk.Checkbutton(faultyPartWind, text="Quadrant 1", variable=q1, onvalue="1", offvalue="0", height=1, width=20)
    q1CB.pack()
    q2CB=tk.Checkbutton(faultyPartWind, text="Quadrant 2", variable=q2, onvalue="1", offvalue="0", height=1, width=20)
    q2CB.pack()
    q3CB=tk.Checkbutton(faultyPartWind, text="Quadrant 3", variable=q3, onvalue="1", offvalue="0", height=1, width=20)
    q3CB.pack()
    q4CB=tk.Checkbutton(faultyPartWind, text="Quadrant 4", variable=q4, onvalue="1", offvalue="0", height=1, width=20)
    q4CB.pack()
    #save and cancel buttons
    faultyPartSave=tk.Button(faultyPartWind, text="Save", command=faultyPartWind.destroy)
    faultyPartSave.pack(pady=20)
    faultyPartCancelFlag=tk.StringVar()
    faultyPartCancelFlag.set('0')
    cancel_faulty_part_challenge=partial(exitAndFlag, faultyPartWind, faultyPartCancelFlag)
    faultyPartCancel=tk.Button(faultyPartWind, text="Cancel", command=cancel_faulty_part_challenge)
    faultyPartCancel.pack()
    faultyPartWind.mainloop()
    if faultyPartCancelFlag.get()=="0":
        quadrants=[]
        if q1.get()=="1":
            quadrants.append("1")
        if q2.get()=="1":
            quadrants.append("2")
        if q3.get()=="1":
            quadrants.append("3")
        if q4.get()=="1":
            quadrants.append("4")
        faultyParts.append(FaultyPart(currentOrderID.get(),", ".join(quadrants)))

def newDroppedPart(droppedParts):
    dropPartWind=tk.Toplevel()
    #robot types
    robotType=tk.StringVar()
    robotType.set(robotTypes)
    robotTypeLabel=tk.Label(dropPartWind, text="Select the robot type for the dropped part")
    robotTypeLabel.pack()
    robotTypeMenu=tk.OptionMenu(dropPartWind, robotType, *robotTypes)
    robotTypeMenu.pack()
    #part type
    partType=tk.StringVar()
    partType.set(allPartTypes[0])
    partTypeLabel=tk.Label(dropPartWind, text="Select the type of part")
    partTypeLabel.pack()
    partTypeMenu=tk.OptionMenu(dropPartWind, partType, *allPartTypes)
    partTypeMenu.pack()
    #part color
    partColor=tk.StringVar()
    partColor.set(allPartColors[0])
    partColorLabel=tk.Label(dropPartWind, text="Select the color of the part")
    partColorLabel.pack()
    partColorMenu=tk.OptionMenu(dropPartWind, partColor, *allPartColors)
    partColorMenu.pack()
    #drop after
    dropAfter=tk.StringVar()
    dropAfter.set("0")
    dropAfterLabel=tk.Label(dropPartWind, text="Set the amount of time to drop the part after")
    dropAfterLabel.pack()
    dropAfterEntry=tk.Entry(dropPartWind, textvariable=dropAfter)
    dropAfterEntry.pack()
    #delay
    delayVal=tk.StringVar()
    delayVal.set('0')
    delayLabel=tk.Label(dropPartWind,text="Set the delay for the dropped part")
    delayLabel.pack()
    delayEntry=tk.Entry(dropPartWind, textvariable=delayVal)
    delayEntry.pack()
    #save and cancel buttons
    dropPartSave=tk.Button(dropPartWind, text="Save", command=dropPartWind.destroy)
    dropPartSave.pack(pady=20)
    dropPartCancelFlag=tk.StringVar()
    dropPartCancelFlag.set('0')
    cancel_drop_part_challenge=partial(exitAndFlag, dropPartWind, dropPartCancelFlag)
    dropPartCancel=tk.Button(dropPartWind, text="Cancel", command=cancel_drop_part_challenge)
    dropPartCancel.pack()
    #validation
    validate_drop_after=partial(require_num,dropAfter)
    dropAfter.trace('w',validate_drop_after)
    validate_delay=partial(require_num, delayVal)
    delayVal.trace('w', validate_delay)
    dropPartWind.mainloop()
    if dropPartCancelFlag.get()=="0":
        droppedParts.append(DroppedPart(robotType.get(), partType.get(), partColor.get(), dropAfter.get(), delayVal.get()))
    
def newSensorBlackout(sensorBlackouts):
    sensBOWind=tk.Toplevel()
    sensBOWind.mainloop()