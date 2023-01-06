import tkinter as tk
from functools import partial
from Functions.checkCancel import *
from newFunctions.newClasses import *
agvOptions=["1","2","3","4"]
allPartTypes=["sensor", "pump", "regulator", "battery"]
allPartColors=['green', 'red', 'purple','blue','orange']

def newRobotMalfunction(robotMalfunctions):
    robotMalfunctionWind=tk.Tk()
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
    ceilRobot=tk.StringVar()
    floorRobot.set('0')
    ceilRobot.set('0')
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
    robotMalfunctionWind.mainloop()
    if robotMalfCancelFlag.get()=="0":
        robotsString=""
        if floorRobot.get()=="1" and ceilRobot.get()=="1":
            robotsString="[\'floor_robot\',\'ceiling_robot\']"
        elif floorRobot.get()=="1":
            robotsString="[\'floor_robot\']"
        elif ceilRobot.get()=="1":
            robotsString="[\'ceiling_robot\']"
        robotMalfunctions.append(RobotMalfunction(duration.get(), robotsString, partType.get(), partColor.get(), agvSelection.get()))