import tkinter as tk
import tkinter.ttk as ttk
import platform
from os import chdir
from functools import partial
from PIL import Image, ImageTk  # needed for images in gui
from jsonschema import validate
import yaml
import Functions.validateARIAC as validateARIAC
from Functions.checkCancel import *
from Functions.updateRanges import *
from Functions.validationFunc import *
from Functions.roboBreakdown import add_robot_breakdown
from Functions.addDrop import add_drop_region
from Functions.fileFunc import *
from Functions.faultyProd import add_faulty_prod
from Functions.beltFunc import add_belt
from Functions.addProduct import add_product
from Functions.stationFunc import add_station
from Functions.binFunc import add_bin
from Functions.buttonFuncs import *
from Functions.orders.orderFuncs import *
from newFunctions.timeFunctions import *
from newClasses import *
from addPartFunc import addPart
from updateAGVFuncs import updateTrayIds
pathIncrement = []  # gives the full path for recursive deletion
createdDir = []  # to deleted directories made if canceled
leftColumn=0
middleColumn=1 
middleColumnWidth=62  # width of middle margin for live yaml windows
rightColumn=2
nameLabels = []  # holds temporary flags to be deleted
agv1Parts=[]
agv2Parts=[]
agv3Parts=[]
agv4Parts=[]
agvTrayIds=["","0","1","2","3","4","5","6"]
trayIds=["0","1","2","3","4","5","6"]
agv1Quadrants=["0","1","2","3"]
agv2Quadrants=["0","1","2","3"]
agv3Quadrants=["0","1","2","3"]
agv4Quadrants=["0","1","2","3"]
if __name__=="__main__":
    getFileName = tk.Tk()
    fileNameVar = tk.StringVar()
    faultySkipFlag = tk.StringVar()
    faultySkipFlag.set('0')
    dropsSkipFlag = tk.StringVar()
    dropsSkipFlag.set('0')
    sensor_blackout_skip_flag = tk.StringVar()
    sensor_blackout_skip_flag.set('0')
    secondOrderFlag = tk.StringVar()
    secondOrderFlag.set('0')
    assembProdsFlag = tk.StringVar()
    assembProdsFlag.set('0')
    kitProdsFlag = tk.StringVar()
    kitProdsFlag.set('0')
    orderFlag = tk.StringVar()
    orderFlag.set('0')
    orderNextFlag = tk.StringVar()
    orderNextFlag.set('0')
    kittingFlag = tk.StringVar()
    kittingFlag.set('0')
    assembFlag = tk.StringVar()
    assembFlag.set('0')
    frame = tk.Frame(getFileName)
    getFileName.geometry("850x600")
    frame.pack()
    if platform.system()=="Windows":
        nistLogo = ImageTk.PhotoImage(Image.open("GUI_Images\\new_NIST_logo.png"))
    else:
        nistLogo = ImageTk.PhotoImage(Image.open("GUI_Images/new_NIST_logo.png"))
    logoImgLabel = tk.Label(frame, image=nistLogo)
    logoImgLabel.pack()
    cancelFlag = tk.StringVar()
    cancelFlag.set('0')
    getFileName.title("NIST ARIAC CONFIG GUI")
    fileName = tk.StringVar()
    fileName.set("")
    invalidFlag = tk.StringVar()
    invalidFlag.set('0')
    reqFlag = tk.StringVar()
    reqFlag.set("0")
    existFlag = tk.StringVar()
    existFlag.set("0")
    fileNameCorrectFunc = partial(correct_file_name, fileName)
    saveAndExit = partial(make_file, getFileName, fileNameVar)
    openFileExp = tk.Button(getFileName, text="Create file", command=saveAndExit)
    openFileExp.pack()
    cancel_file = partial(cancel_wind, getFileName, cancelFlag)
    cancelFile = tk.Button(getFileName, text="Cancel and Exit", command=cancel_file)
    cancelFile.pack(side=tk.BOTTOM, pady=20)
    fileFunc=partial(get_file_name_next, fileName, invalidFlag, nameLabels, getFileName, reqFlag, existFlag)
    fileExit = tk.Button(getFileName, text="Next", command=fileFunc)
    fileExit.pack(side=tk.BOTTOM, pady=20)
    fileName.trace('w', fileNameCorrectFunc)
    getFileName.mainloop()
    if cancelFlag.get()=='1':
        quit()
    tempFilePath=''
    if platform.system()=="Windows":
        brokenPath=fileNameVar.get().split("\\")
        for i in brokenPath[:-1]:
            tempFilePath+=i+"\\"
        fileNameStr=brokenPath[len(brokenPath)-1]
        chdir(tempFilePath)
        saveFileName=fileNameStr
    else:
        brokenPath=fileNameVar.get().split("/")
        for i in brokenPath[:-1]:
            tempFilePath+=i+"/"
        fileNameStr=brokenPath[len(brokenPath)-1]
        chdir(tempFilePath)
        saveFileName=fileNameStr
    fileName.set(saveFileName)
    # END OF GETTING THE NAME OF THE FILE
    # ----------------------------------------------------------------------------------------------
    # START OF GETTING TIME LIMIT
    timeWind=tk.Tk()
    timeWind.title("Time limit")
    timeWind.geometry("850x600")
    #margin=tk.Label(timeWind, text=" "*middleColumnWidth)
    #margin.grid(column=leftColumn)
    timeInstructions=tk.Label(timeWind, text="Enter the time limit you would like for the simulation (max value: 500)")
    #timeInstructions.grid(column=middleColumn, pady=100)
    timeInstructions.pack(pady=100)
    timeVal=tk.StringVar()
    timeVal.set("0")
    noTimeVal=tk.StringVar()
    noTimeVal.set("0")
    noTimeLim=tk.Checkbutton(timeWind, text="No time limit", variable=noTimeVal, onvalue="1", offvalue="0", height=5, width=20)
    #noTimeLim.grid(column=middleColumn)
    noTimeLim.pack()
    getTime=tk.Entry(timeWind, textvariable=timeVal)
    #getTime.grid(column=middleColumn)
    getTime.pack()
    saveTimeButton=tk.Button(timeWind, text="Save and Continue", command=timeWind.destroy)
    #saveTimeButton.grid(column=middleColumn,pady=20)
    saveTimeButton.pack(pady=20)
    cancel_time_command=partial(cancel_wind, timeWind, cancelFlag)
    cancelTimeButton=tk.Button(timeWind, text="Cancel and Exit", command=cancel_time_command)
    #cancelTimeButton.grid(column=middleColumn,pady=20)
    cancelTimeButton.pack(pady=20)
    updateGetTime=partial(updateTimeInputBox, noTimeVal, getTime)
    validateTimeInput=partial(validateTime, timeVal)
    noTimeVal.trace('w', updateGetTime)
    timeVal.trace('w', validateTimeInput)
    timeWind.mainloop()
    check_cancel(cancelFlag.get(), pathIncrement, fileName, createdDir)
    # END OF TIME LIMIT
    # ----------------------------------------------------------------------------------------------
    # START OF GETTING KITTING TRAYS
    trayWind=tk.Tk()
    trayIDLabel=tk.Label(trayWind, text="Select the tray ID's to be spawned")
    trayIDLabel.grid(column=leftColumn)
    tray1=tk.StringVar()
    tray2=tk.StringVar()
    tray3=tk.StringVar()
    tray4=tk.StringVar()
    tray5=tk.StringVar()
    tray6=tk.StringVar()
    tray1.set("0")
    tray2.set("0")
    tray3.set("0")
    tray4.set("0")
    tray5.set("0")
    tray6.set("0")
    tray1Check=tk.Checkbutton(trayWind, text="Tray 1", variable=tray1, onvalue="1", offvalue="0", height=5, width=20)
    tray1Check.grid(column=leftColumn)
    tray2Check=tk.Checkbutton(trayWind, text="Tray 2", variable=tray2, onvalue="1", offvalue="0", height=5, width=20)
    tray2Check.grid(column=leftColumn)
    tray3Check=tk.Checkbutton(trayWind, text="Tray 3", variable=tray3, onvalue="1", offvalue="0", height=5, width=20)
    tray3Check.grid(column=leftColumn)
    tray4Check=tk.Checkbutton(trayWind, text="Tray 4", variable=tray4, onvalue="1", offvalue="0", height=5, width=20)
    tray4Check.grid(column=leftColumn)
    tray5Check=tk.Checkbutton(trayWind, text="Tray 5", variable=tray5, onvalue="1", offvalue="0", height=5, width=20)
    tray5Check.grid(column=leftColumn)
    tray6Check=tk.Checkbutton(trayWind, text="Tray 6", variable=tray6, onvalue="1", offvalue="0", height=5, width=20)
    tray6Check.grid(column=leftColumn)
    slotsLabel=tk.Label(trayWind, text="Select the slots for the trays")
    slotsLabel.grid(column=rightColumn, row=0)
    slot1=tk.StringVar()
    slot2=tk.StringVar()
    slot3=tk.StringVar()
    slot4=tk.StringVar()
    slot5=tk.StringVar()
    slot6=tk.StringVar()
    slot1.set("0")
    slot2.set("0")
    slot3.set("0")
    slot4.set("0")
    slot5.set("0")
    slot6.set("0")
    slot1Check=tk.Checkbutton(trayWind, text="Slot 1", variable=slot1, onvalue="1", offvalue="0", height=5, width=20)
    slot1Check.grid(column=rightColumn,row=1)
    slot2Check=tk.Checkbutton(trayWind, text="Slot 2", variable=slot2, onvalue="1", offvalue="0", height=5, width=20)
    slot2Check.grid(column=rightColumn,row=2)
    slot3Check=tk.Checkbutton(trayWind, text="Slot 3", variable=slot3, onvalue="1", offvalue="0", height=5, width=20)
    slot3Check.grid(column=rightColumn,row=3)
    slot4Check=tk.Checkbutton(trayWind, text="Slot 4", variable=slot4, onvalue="1", offvalue="0", height=5, width=20)
    slot4Check.grid(column=rightColumn,row=4)
    slot5Check=tk.Checkbutton(trayWind, text="Slot 5", variable=slot5, onvalue="1", offvalue="0", height=5, width=20)
    slot5Check.grid(column=rightColumn,row=5)
    slot6Check=tk.Checkbutton(trayWind, text="Slot 6", variable=slot6, onvalue="1", offvalue="0", height=5, width=20)
    slot6Check.grid(column=rightColumn,row=6)
    saveTrayButton=tk.Button(trayWind, text="Save and Continue", command=trayWind.destroy)
    saveTrayButton.grid(column=middleColumn,pady=20)
    cancel_tray_command=partial(cancel_wind, trayWind, cancelFlag)
    cancelTrayButton=tk.Button(trayWind, text="Cancel and Exit", command=cancel_tray_command)
    cancelTrayButton.grid(column=middleColumn,pady=20)
    trayWind.mainloop()
    check_cancel(cancelFlag.get(), pathIncrement, fileName, createdDir)
    # END OF GETTING KITTING TRAYS
    # ----------------------------------------------------------------------------------------------
    # START OF PARTS
    partsWind=tk.Tk()
    partsWind.geometry("850x600")
    agv1TrayId=tk.StringVar()
    agv1TrayId.set(agvTrayIds[0])
    agv2TrayId=tk.StringVar()
    agv2TrayId.set(agvTrayIds[0])
    agv3TrayId=tk.StringVar()
    agv3TrayId.set(agvTrayIds[0])
    agv4TrayId=tk.StringVar()
    agv4TrayId.set(agvTrayIds[0])
    agv1TrayLabel=tk.Label(partsWind, text="Select the tray Id for agv1")
    agv1TrayLabel.pack()
    agv1TrayIdSelect=tk.OptionMenu(partsWind, agv1TrayId, *agvTrayIds)
    agv1TrayIdSelect.pack()
    agv2TrayLabel=tk.Label(partsWind, text="Select the tray Id for agv2")
    agv2TrayLabel.pack()
    agv2TrayIdSelect=tk.OptionMenu(partsWind, agv2TrayId, *agvTrayIds)
    agv2TrayIdSelect.pack()
    agv3TrayLabel=tk.Label(partsWind, text="Select the tray Id for agv3")
    agv3TrayLabel.pack()
    agv3TrayIdSelect=tk.OptionMenu(partsWind, agv3TrayId, *agvTrayIds)
    agv3TrayIdSelect.pack()
    agv4TrayLabel=tk.Label(partsWind, text="Select the tray Id for agv4")
    agv4TrayLabel.pack()
    agv4TrayIdSelect=tk.OptionMenu(partsWind, agv4TrayId, *agvTrayIds)
    agv4TrayIdSelect.pack()
    add_new_part=partial(addPart,agv1Parts, agv2Parts, agv3Parts, agv4Parts, agv1Quadrants,agv2Quadrants,agv3Quadrants,agv4Quadrants)
    addPartsButton=tk.Button(partsWind, text="Add part", command=add_new_part)
    addPartsButton.pack()
    savePartsButton=tk.Button(partsWind, text="Save and Continue", command=partsWind.destroy)
    savePartsButton.pack()
    cancel_parts_command=partial(cancel_wind, partsWind, cancelFlag)
    cancelPartsButton=tk.Button(partsWind, text="Cancel and Exit", command=cancel_parts_command)
    cancelPartsButton.pack()
    update_agv_ids=partial(updateTrayIds,agv1TrayId, agv2TrayId, agv3TrayId, agv4TrayId, agv1TrayIdSelect, agv2TrayIdSelect, agv3TrayIdSelect, agv4TrayIdSelect,agvTrayIds)
    agv1TrayId.trace('w', update_agv_ids)
    agv2TrayId.trace('w', update_agv_ids)
    agv3TrayId.trace('w', update_agv_ids)
    agv4TrayId.trace('w', update_agv_ids)
    partsWind.mainloop()
    check_cancel(cancelFlag.get(), pathIncrement, fileName, createdDir)

