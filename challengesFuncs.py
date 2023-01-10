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
destinations=["warehouse", "as1", "as2","as3","as4","kitting"]
stations=["as1","as2","as3","as4"]
sensBOCategories=["time-based","during kitting", "during assembly","after kitting", "after assembly"]
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

def showAGVMenu(agvShow,agvShowCB, agvMenu, agvLabel, agv, a,b,c):
    if agvShow.get()=="1":
        agvLabel.pack(after=agvShowCB)
        agvMenu.pack(after=agvLabel)
        agv.set(agvOptions[0])
    else:
        agvLabel.pack_forget()
        agvMenu.pack_forget()
        agv.set('')

def showDestMenu(destShow, destShowCB, destMenu, destLabel, destination,a,b,c):
    if destShow.get()=="1":
        destLabel.pack(after=destShowCB)
        destMenu.pack(after=destLabel)
        destination.set(destinations[0])
    else:
        destLabel.pack_forget()
        destMenu.pack_forget()
        destination.set('')

def showStatMenu(statShow, statShowCB, statMenu, statLabel, station, a,b,c):
    if statShow.get()=="1":
        statLabel.pack(after=statShowCB)
        statMenu.pack(after=statLabel)
        station.set(stations[0])
    else:
        statLabel.pack_forget()
        statMenu.pack_forget()
        station.set('')

def showTimeMenu(timeShow, timeShowCB, timeEntry, timeLabel, time, a,b,c):
    if timeShow.get()=="1":
        timeLabel.pack(after=timeShowCB)
        timeEntry.pack(after=timeLabel)
        time.set('0')
    else:
        timeLabel.pack_forget()
        timeEntry.pack_forget()
        time.set('')

def showPartMenu(partShow, partShowCB, partTypeLabel, partTypeMenu, partColorLabel, partColorMenu,partType, partColor,a,b,c):
    if partShow.get()=="1":
        partTypeLabel.pack(after=partShowCB)
        partTypeMenu.pack(after=partTypeLabel)
        partColorLabel.pack(after=partTypeMenu)
        partColorMenu.pack(after=partColorLabel)
        partType.set(allPartTypes[0])
        partColor.set(allPartColors[0])
    else:
        partTypeLabel.pack_forget()
        partTypeMenu.pack_forget()
        partColorLabel.pack_forget()
        partColorMenu.pack_forget()
        partType.set("")
        partColor.set("")

def newSensorBlackout(sensorBlackouts):
    allSensors=[]
    selectedSensors=[]
    sensBOWind=tk.Toplevel()
    #category
    category=tk.StringVar()
    category.set(sensBOCategories[0])
    categoryLabel=tk.Label(sensBOWind, text="Choose the category for the sensor blackout")
    categoryLabel.pack()
    categoryMenu=tk.OptionMenu(sensBOWind, category, *sensBOCategories)
    categoryMenu.pack()
    #duration
    duration=tk.StringVar()
    duration.set('0')
    durationLabel=tk.Label(sensBOWind, text="Enter the duration for the sensor blackout")
    durationLabel.pack()
    durationEntry=tk.Entry(sensBOWind, textvariable=duration)
    durationEntry.pack()
    #part type
    partType=tk.StringVar()
    partType.set(allPartTypes[0])
    partTypeLabel=tk.Label(sensBOWind, text="Select the type of part")
    partTypeLabel.pack()
    partTypeMenu=tk.OptionMenu(sensBOWind, partType, *allPartTypes)
    partTypeMenu.pack()
    #part color
    partColor=tk.StringVar()
    partColor.set(allPartColors[0])
    partColorLabel=tk.Label(sensBOWind, text="Select the color of the part")
    partColorLabel.pack()
    partColorMenu=tk.OptionMenu(sensBOWind, partColor, *allPartColors)
    partColorMenu.pack()
    #sensors to disable
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
    sensor1CB=tk.Checkbutton(sensBOWind, text="break beam", variable=sensor1, onvalue="1", offvalue="0", height=1, width=20)
    sensor1CB.pack()
    sensor2CB=tk.Checkbutton(sensBOWind, text="proximity", variable=sensor2, onvalue="1", offvalue="0", height=1, width=20)
    sensor2CB.pack()
    sensor3CB=tk.Checkbutton(sensBOWind, text="laser profiler", variable=sensor3, onvalue="1", offvalue="0", height=1, width=20)
    sensor3CB.pack()
    sensor4CB=tk.Checkbutton(sensBOWind, text="lidar", variable=sensor4, onvalue="1", offvalue="0", height=1, width=20)
    sensor4CB.pack()
    sensor5CB=tk.Checkbutton(sensBOWind, text="camera", variable=sensor5, onvalue="1", offvalue="0", height=1, width=20)
    sensor5CB.pack()
    sensor6CB=tk.Checkbutton(sensBOWind, text="logical camera", variable=sensor6, onvalue="1", offvalue="0", height=1, width=20)
    sensor6CB.pack()
    #optional items
    optionalLabel=tk.Label(sensBOWind, text="The following are optional. To add them, click the associated checkbox")
    optionalLabel.pack()
    timeShow=tk.StringVar()
    timeShow.set('0')
    timeShowCB=tk.Checkbutton(sensBOWind, text="Time", variable=timeShow, onvalue="1", offvalue='0', height=1, width=20)
    timeShowCB.pack()
    time=tk.StringVar()
    time.set('')
    timeLabel=tk.Label(sensBOWind, text="Enter the time")
    timeLabel.pack_forget()
    timeEntry=tk.Entry(sensBOWind, textvariable=time)
    timeEntry.pack_forget()
    agvShow=tk.StringVar()
    agvShow.set('0')
    agvShowCB=tk.Checkbutton(sensBOWind, text="AGV", variable=agvShow, onvalue="1", offvalue='0', height=1, width=20)
    agvShowCB.pack()
    agv=tk.StringVar()
    agv.set("")
    agvLabel=tk.Label(sensBOWind, text="Choose the agv")
    agvLabel.pack_forget()
    agvMenu=tk.OptionMenu(sensBOWind, agv, *agvOptions)
    agvMenu.pack_forget()
    destShow=tk.StringVar()
    destShow.set('0')
    destShowCB=tk.Checkbutton(sensBOWind, text="Destination", variable=destShow, onvalue="1", offvalue='0', height=1, width=20)
    destShowCB.pack()
    destination=tk.StringVar()
    destination.set(destinations[0])
    destLabel=tk.Label(sensBOWind, text="Choose the destination")
    destLabel.pack_forget()
    destMenu=tk.OptionMenu(sensBOWind, destination, *destinations)
    destMenu.pack_forget()
    statShow=tk.StringVar()
    statShow.set('0')
    statShowCB=tk.Checkbutton(sensBOWind, text="Station", variable=statShow, onvalue="1", offvalue='0', height=1, width=20)
    statShowCB.pack()
    station=tk.StringVar()
    station.set(stations[0])
    stationLabel=tk.Label(sensBOWind, text="Choose the station")
    stationLabel.pack_forget()
    stationMenu=tk.OptionMenu(sensBOWind, station, *stations)
    stationMenu.pack_forget()
    partShow=tk.StringVar()
    partShow.set('0')
    partShowCB=tk.Checkbutton(sensBOWind, text="Part", variable=partShow, onvalue="1", offvalue='0', height=1, width=20)
    partShowCB.pack()
    partType=tk.StringVar()
    partType.set("")
    partTypeLabel=tk.Label(sensBOWind, text="Select the type of part")
    partTypeLabel.pack_forget()
    partTypeMenu=tk.OptionMenu(sensBOWind, partType, *allPartTypes)
    partTypeMenu.pack_forget()
    partColor=tk.StringVar()
    partColor.set("")
    partColorLabel=tk.Label(sensBOWind, text="Select the color of the part")
    partColorLabel.pack_forget()
    partColorMenu=tk.OptionMenu(sensBOWind, partColor, *allPartColors)
    partColorMenu.pack_forget()
    #save and cancel buttons
    sensBOSave=tk.Button(sensBOWind, text="Save", command=sensBOWind.destroy)
    sensBOSave.pack(pady=20)
    sensBOCancelFlag=tk.StringVar()
    sensBOCancelFlag.set('0')
    cancel_sens_bo_challenge=partial(exitAndFlag, sensBOWind, sensBOCancelFlag)
    sensBOCancel=tk.Button(sensBOWind, text="Cancel", command=cancel_sens_bo_challenge)
    sensBOCancel.pack()
    #variable tracing
    show_time_menu=partial(showTimeMenu, timeShow, timeShowCB, timeEntry, timeLabel, time)
    timeShow.trace('w', show_time_menu)
    show_agv_menu=partial(showAGVMenu, agvShow,agvShowCB, agvMenu, agvLabel, agv)
    agvShow.trace('w', show_agv_menu)
    show_dest_menu=partial(showDestMenu,destShow, destShowCB, destMenu, destLabel, destination)
    destShow.trace('w', show_dest_menu)
    show_stat_menu=partial(showStatMenu,statShow, statShowCB, stationMenu, stationLabel, station)
    statShow.trace('w', show_stat_menu)
    sensBOWind.mainloop()
    if sensBOCancelFlag.get()=="0":
        allSensors.append(sensor1.get())
        allSensors.append(sensor2.get())
        allSensors.append(sensor3.get())
        allSensors.append(sensor4.get())
        allSensors.append(sensor5.get())
        allSensors.append(sensor6.get())
        for i in range(len(allSensors)):
            if allSensors[i]=="1":
                selectedSensors.append("\'sensor"+str(i+1)+"\'")
        sensorBlackouts.append(SensorBlackout(category.get(), time.get(),duration.get(),", ".join(selectedSensors), agv.get(), destination.get(), station.get(), partType.get(), partColor.get()))
        
            