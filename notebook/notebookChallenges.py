import tkinter as tk
from tkinter import ttk
from functools import partial
usedIds=["ABCDFGHI"] #Temporary for testing
allPartTypes=["sensor", "pump", "regulator", "battery"]
allPartColors=['green', 'red', 'purple','blue','orange']
robotTypes=["ceiling_robot","floor_robot"]
agvOptions=["1","2","3","4"]
sensBOCategories=["time-based","during kitting", "during assembly","after kitting", "after assembly"]
conditionTypes=['time','partPlace','submission']

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