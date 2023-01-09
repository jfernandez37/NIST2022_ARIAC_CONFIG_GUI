import tkinter as tk
import tkinter.ttk as ttk
import platform
from datetime import datetime
from os import chdir
from functools import partial
from PIL import Image, ImageTk  # needed for images in gui
from jsonschema import validate
import yaml
import Functions.validateARIAC as validateARIAC
from Functions.checkCancel import *
from Functions.updateRanges import *
from Functions.validationFunc import *
from Functions.fileFunc import *
from Functions.buttonFuncs import *
from Functions.orders.orderFuncs import *
from newFunctions.timeFunctions import *
from newFunctions.newClasses import *
from newFunctions.addPartFunc import *
from newFunctions.updateAGVFuncs import updateTrayIds
from newFunctions.addNewBin import *
from newFunctions.addConvPart import addPartConv
from newFunctions.orderFuncs import *
from challengesFuncs import *

CHECKBOXHEIGHT=1
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
agv1Quadrants=["1","2","3","4"]
agv2Quadrants=["1","2","3","4"]
agv3Quadrants=["1","2","3","4"]
agv4Quadrants=["1","2","3","4"]
bins=[]
bin1Slots=[]
bin2Slots=[]
bin3Slots=[]
bin4Slots=[]
bin5Slots=[]
bin6Slots=[]
bin7Slots=[]
bin8Slots=[]
convParts=[]
for i in range(9):
    bin1Slots.append(str(i+1))
    bin2Slots.append(str(i+1))
    bin3Slots.append(str(i+1))
    bin4Slots.append(str(i+1))
    bin5Slots.append(str(i+1))
    bin6Slots.append(str(i+1))
    bin7Slots.append(str(i+1))
    bin8Slots.append(str(i+1))
allOrders=[]
kittingParts=[]
assemblyParts=[]
orderIds=[]
orderCounter=[]
allOrderChallenges=[]
kittingTrayIds=[]
kittingTraySlots=[]
binPresentFlags=[]
for i in range(8):
    binPresentFlags.append(0)
orderKittingParts=[]
orderAssembParts=[]
usedIDs=[]
def randOrSeq():  
    """Cycles through the options for the conveyor belt order"""
    if changeOrder.config('text')[-1] == 'random':
        changeOrder.config(text='sequential')
        convOrder.set("sequential")
    elif changeOrder.config('text')[-1] == 'sequential':
        changeOrder.config(text='random')
        convOrder.set("random")
robotMalfunctions=[]
faultyParts=[]
droppedParts=[]
sensorBlackouts=[]

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
    noTimeLim=tk.Checkbutton(timeWind, text="No time limit", variable=noTimeVal, onvalue="1", offvalue="0", height=CHECKBOXHEIGHT, width=20)
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
    tray0=tk.StringVar()
    tray1=tk.StringVar()
    tray2=tk.StringVar()
    tray3=tk.StringVar()
    tray4=tk.StringVar()
    tray5=tk.StringVar()
    tray6=tk.StringVar()
    tray7=tk.StringVar()
    tray8=tk.StringVar()
    tray9=tk.StringVar()
    tray0.set("0")
    tray1.set("0")
    tray2.set("0")
    tray3.set("0")
    tray4.set("0")
    tray5.set("0")
    tray6.set("0")
    tray7.set("0")
    tray8.set("0")
    tray9.set("0")
    tray0Check=tk.Checkbutton(trayWind, text="Tray 0", variable=tray0, onvalue="1", offvalue="0", height=CHECKBOXHEIGHT, width=20)
    tray0Check.grid(column=leftColumn)
    tray1Check=tk.Checkbutton(trayWind, text="Tray 1", variable=tray1, onvalue="1", offvalue="0", height=CHECKBOXHEIGHT, width=20)
    tray1Check.grid(column=leftColumn)
    tray2Check=tk.Checkbutton(trayWind, text="Tray 2", variable=tray2, onvalue="1", offvalue="0", height=CHECKBOXHEIGHT, width=20)
    tray2Check.grid(column=leftColumn)
    tray3Check=tk.Checkbutton(trayWind, text="Tray 3", variable=tray3, onvalue="1", offvalue="0", height=CHECKBOXHEIGHT, width=20)
    tray3Check.grid(column=leftColumn)
    tray4Check=tk.Checkbutton(trayWind, text="Tray 4", variable=tray4, onvalue="1", offvalue="0", height=CHECKBOXHEIGHT, width=20)
    tray4Check.grid(column=leftColumn)
    tray5Check=tk.Checkbutton(trayWind, text="Tray 5", variable=tray5, onvalue="1", offvalue="0", height=CHECKBOXHEIGHT, width=20)
    tray5Check.grid(column=leftColumn)
    tray6Check=tk.Checkbutton(trayWind, text="Tray 6", variable=tray6, onvalue="1", offvalue="0", height=CHECKBOXHEIGHT, width=20)
    tray6Check.grid(column=leftColumn)
    tray7Check=tk.Checkbutton(trayWind, text="Tray 7", variable=tray7, onvalue="1", offvalue="0", height=CHECKBOXHEIGHT, width=20)
    tray7Check.grid(column=leftColumn)
    tray8Check=tk.Checkbutton(trayWind, text="Tray 8", variable=tray8, onvalue="1", offvalue="0", height=CHECKBOXHEIGHT, width=20)
    tray8Check.grid(column=leftColumn)
    tray9Check=tk.Checkbutton(trayWind, text="Tray 9", variable=tray9, onvalue="1", offvalue="0", height=CHECKBOXHEIGHT, width=20)
    tray9Check.grid(column=leftColumn)
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
    slot1Check=tk.Checkbutton(trayWind, text="Slot 1", variable=slot1, onvalue="1", offvalue="0", height=CHECKBOXHEIGHT, width=20)
    slot1Check.grid(column=rightColumn,row=1)
    slot2Check=tk.Checkbutton(trayWind, text="Slot 2", variable=slot2, onvalue="1", offvalue="0", height=CHECKBOXHEIGHT, width=20)
    slot2Check.grid(column=rightColumn,row=2)
    slot3Check=tk.Checkbutton(trayWind, text="Slot 3", variable=slot3, onvalue="1", offvalue="0", height=CHECKBOXHEIGHT, width=20)
    slot3Check.grid(column=rightColumn,row=3)
    slot4Check=tk.Checkbutton(trayWind, text="Slot 4", variable=slot4, onvalue="1", offvalue="0", height=CHECKBOXHEIGHT, width=20)
    slot4Check.grid(column=rightColumn,row=4)
    slot5Check=tk.Checkbutton(trayWind, text="Slot 5", variable=slot5, onvalue="1", offvalue="0", height=CHECKBOXHEIGHT, width=20)
    slot5Check.grid(column=rightColumn,row=5)
    slot6Check=tk.Checkbutton(trayWind, text="Slot 6", variable=slot6, onvalue="1", offvalue="0", height=CHECKBOXHEIGHT, width=20)
    slot6Check.grid(column=rightColumn,row=6)
    saveTrayButton=tk.Button(trayWind, text="Save and Continue", command=trayWind.destroy)
    saveTrayButton.grid(column=middleColumn,pady=20)
    cancel_tray_command=partial(cancel_wind, trayWind, cancelFlag)
    cancelTrayButton=tk.Button(trayWind, text="Cancel and Exit", command=cancel_tray_command)
    cancelTrayButton.grid(column=middleColumn,pady=20)
    trayWind.mainloop()
    check_cancel(cancelFlag.get(), pathIncrement, fileName, createdDir)
    kittingTrayIds.append(tray0.get())
    kittingTrayIds.append(tray1.get())
    kittingTrayIds.append(tray2.get())
    kittingTrayIds.append(tray3.get())
    kittingTrayIds.append(tray4.get())
    kittingTrayIds.append(tray5.get())
    kittingTrayIds.append(tray6.get())
    kittingTrayIds.append(tray7.get())
    kittingTrayIds.append(tray8.get())
    kittingTrayIds.append(tray9.get())
    kittingTraySlots.append(slot1.get())
    kittingTraySlots.append(slot2.get())
    kittingTraySlots.append(slot3.get())
    kittingTraySlots.append(slot4.get())
    kittingTraySlots.append(slot5.get())
    kittingTraySlots.append(slot6.get())
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
    add_new_part=partial(addPart,agv1Parts, agv2Parts, agv3Parts, agv4Parts, agv1Quadrants,agv2Quadrants,agv3Quadrants,agv4Quadrants, partsWind)
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
    # END OF PARTS
    # ----------------------------------------------------------------------------------------------
    # START OF BINS
    binsWind=tk.Tk()
    binsWind.geometry("850x600")
    add_bin_func=partial(addBin,bins,bin1Slots,bin2Slots,bin3Slots,bin4Slots,bin5Slots,bin6Slots,bin7Slots,bin8Slots)
    addBinsButton=tk.Button(binsWind, text="Add Bins", command=add_bin_func)
    addBinsButton.pack(pady=20)
    saveBinsButton=tk.Button(binsWind, text="Save and Continue", command=binsWind.destroy)
    saveBinsButton.pack(pady=20)
    cancel_bins_command=partial(cancel_wind, binsWind, cancelFlag)
    cancelBinsButton=tk.Button(binsWind, text="Cancel and Exit", command=cancel_bins_command)
    cancelBinsButton.pack(pady=20)
    binsWind.mainloop()
    check_cancel(cancelFlag.get(), pathIncrement, fileName, createdDir)
    # END OF BINS
    # ----------------------------------------------------------------------------------------------
    # START OF CONVEYOR BELT
    convWind=tk.Tk()
    convWind.title("Conveyor Belt")
    convWind.geometry("850x600")
    conveyorBeltLabel=tk.Label(convWind, text="Conveyor Belt Settings")
    conveyorBeltLabel.pack()
    convActive=tk.StringVar()
    convActive.set('0')
    activeCheck=tk.Checkbutton(convWind, text="Active", variable=convActive, onvalue="1", offvalue="0", height=3, width=20)
    activeCheck.pack()
    spawnRate=tk.StringVar()
    spawnRate.set('0')
    spawnRateEntryLabel=tk.Label(convWind, text="Enter the spawn rate for the conveyor belt")
    spawnRateEntryLabel.pack()
    spawnRateEntry=tk.Entry(convWind, textvariable=spawnRate)
    spawnRateEntry.pack()
    convOrder=tk.StringVar()
    convOrder.set("random")
    changeOrder = tk.Button(text="random", command=randOrSeq)
    changeOrder.pack(pady=10)
    add_conv_part=partial(addPartConv, convParts)
    addPartConvButton=tk.Button(convWind, text="Add part", command=add_conv_part)
    addPartConvButton.pack(pady=20)
    saveConvButton=tk.Button(convWind, text="Save and Continue", command=convWind.destroy)
    saveConvButton.pack(pady=20)
    cancel_conv_command=partial(cancel_wind, convWind, cancelFlag)
    cancelConvButton=tk.Button(convWind, text="Cancel and Exit", command=cancel_conv_command)
    cancelConvButton.pack(pady=20)
    validate_spawn_rate=partial(require_num, spawnRate)
    spawnRate.trace('w', validate_spawn_rate)
    convWind.mainloop()
    check_cancel(cancelFlag.get(), pathIncrement, fileName, createdDir)
    # END OF CONVEYOR BELT
    # ----------------------------------------------------------------------------------------------
    # START OF ORDERS
    ordersWind=tk.Tk()
    ordersWind.geometry("850x600")
    new_order_func=partial(addNewOrder, allOrders, orderCounter, allOrderChallenges,orderKittingParts,orderAssembParts, usedIDs)
    newOrderButton=tk.Button(ordersWind, text="New Order", command=new_order_func)
    newOrderButton.pack()
    saveOrdersButton=tk.Button(ordersWind, text="Save and Continue", command=ordersWind.destroy)
    saveOrdersButton.pack(pady=20)
    cancel_orders_command=partial(cancel_wind, ordersWind, cancelFlag)
    cancelOrdersButton=tk.Button(ordersWind, text="Cancel and Exit", command=cancel_orders_command)
    cancelOrdersButton.pack(pady=20)
    ordersWind.mainloop()
    check_cancel(cancelFlag.get(), pathIncrement, fileName, createdDir)
    allOrders.reverse()
    orderKittingParts.reverse()
    orderAssembParts.reverse()
    # END OF ORDERS
    # ----------------------------------------------------------------------------------------------
    #START OF CHALLENGES
    challengeWind=tk.Tk()
    challengeWind.geometry("850x600")
    new_robot_malfunction=partial(newRobotMalfunction, robotMalfunctions)
    robotMalfunctionButton=tk.Button(challengeWind, text="Add robot malfunction", command=new_robot_malfunction)
    robotMalfunctionButton.pack(pady=10)
    new_faulty_part=partial(newFaultyPart, faultyParts, usedIDs)
    faultyPartButton=tk.Button(challengeWind, text="Add faulty part", command=new_faulty_part)
    faultyPartButton.pack(pady=10)
    new_dropped_part=partial(newDroppedPart, droppedParts)
    droppedPartButton=tk.Button(challengeWind, text="Add dropped part", command=new_dropped_part)
    droppedPartButton.pack(pady=10)
    new_sensor_blackout=partial(newSensorBlackout, sensorBlackouts)
    sensorBlackoutButton=tk.Button(challengeWind, text="Add sensor blackout", command=new_sensor_blackout)
    sensorBlackoutButton.pack(pady=10)
    saveChallengeButton=tk.Button(challengeWind, text="Save and Continue", command=challengeWind.destroy)
    saveChallengeButton.pack(pady=20)
    cancel_challenge_command=partial(cancel_wind, challengeWind, cancelFlag)
    cancelChallengeButton=tk.Button(challengeWind, text="Cancel and Exit", command=cancel_challenge_command)
    cancelChallengeButton.pack(pady=20)
    challengeWind.mainloop()
    check_cancel(cancelFlag.get(), pathIncrement, fileName, createdDir)
    #Finds which bins are present
    for i in bins:
        if i.binName=="bin1":
            binPresentFlags[0]=1
        if i.binName=="bin2":
            binPresentFlags[1]=1
        if i.binName=="bin3":
            binPresentFlags[2]=1
        if i.binName=="bin4":
            binPresentFlags[3]=1
        if i.binName=="bin5":
            binPresentFlags[4]=1
        if i.binName=="bin6":
            binPresentFlags[5]=1
        if i.binName=="bin7":
            binPresentFlags[6]=1
        if i.binName=="bin8":
            binPresentFlags[7]=1    
    
    
    # START TO WRITE TO FILE
    tempStr=''
    with open(saveFileName, "a") as o:
        o.write("# Trial Name: "+saveFileName+"\n")
        o.write("# ARIAC2023\n")
        o.write("# "+datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"\n\n")
        o.write("# ENVIRONMENT SETUP\n")
        if noTimeVal.get()=="1":
            o.write("time_limit: -1")
        else:
            o.write("time_limit: "+timeVal.get())
        o.write(" # options: -1 (no time limit) or number of seconds (max 500)\n")
        o.write("\nkitting_trays: # Which kitting trays will be spawned\n")
        o.write("  tray_ids: [")
        for i in range(len(kittingTrayIds)):
            if kittingTrayIds[i]=="1":
                tempStr+=str(i)+", "
        o.write(tempStr[:-2]+"]\n")
        o.write("  slots: [")
        tempStr=''
        for i in range(len(kittingTraySlots)):
            if kittingTraySlots[i]=="1":
                tempStr+=str(i+1)+", "
        o.write(tempStr[:-2]+"]\n")
        o.write("\nparts:\n")
        o.write("  agvs:\n")
    if len(agv1Parts)>0:
        writePartsToFile("agv1", agv1TrayId.get(), agv1Parts, saveFileName)
    if len(agv2Parts)>0:
        writePartsToFile("agv2", agv2TrayId.get(), agv2Parts, saveFileName)
    if len(agv3Parts)>0:
        writePartsToFile("agv3", agv3TrayId.get(), agv3Parts, saveFileName)
    if len(agv4Parts)>0:
        writePartsToFile("agv4", agv4TrayId.get(), agv4Parts, saveFileName)
    with open(saveFileName, "a") as o:
        o.write("\n  bins: # bin params - 8 total bins each bin has nine total slots (1-9)\n")
    if binPresentFlags[0]==1:
        writeBinsToFile("bin1", bins, saveFileName)
    if binPresentFlags[1]==1:
        writeBinsToFile("bin2", bins, saveFileName)
    if binPresentFlags[2]==1:
        writeBinsToFile("bin3", bins, saveFileName)
    if binPresentFlags[3]==1:
        writeBinsToFile("bin4", bins, saveFileName)
    if binPresentFlags[4]==1:
        writeBinsToFile("bin5", bins, saveFileName)
    if binPresentFlags[5]==1:
        writeBinsToFile("bin6", bins, saveFileName)
    if binPresentFlags[6]==1:
        writeBinsToFile("bin7", bins, saveFileName)
    if binPresentFlags[7]==1:
        writeBinsToFile("bin8", bins, saveFileName)
    with open(saveFileName, "a") as o:
        o.write("\n  conveyor_belt: #population params for conveyor belt\n")
        if convActive.get()=="1":
            o.write("    active: true\n")
        else:
            o.write("    active: false\n")
        o.write("    spawn_rate: "+spawnRate.get()+" # seconds between spawn\n")
        o.write("    order: "+convOrder.get()+" # random or sequential\n")
        if len(convParts)>0:
            o.write("    parts_to_spawn:\n")
            for part in convParts:
                o.write("      - type: "+part.type)
                o.write("\n        color: "+part.color)
                o.write("\n        number: "+part.number)
                o.write("\n        offset: "+part.offset+" # between -1 and 1")
                o.write("\n        rotation: "+ part.rotation)
                o.write("\n        # time_before_next_part: 2 # seconds\n")
        o.write("\n# ORDER SETUP\n")
        o.write("orders:\n")
        for order in allOrders:
            o.write("  - order_category: "+order.category)
            o.write("\n    id: \'"+order.id+"\'\n")
            o.write("    type: \'"+order.type+"\'\n")
            o.write("    announcement:\n")
            """STILL NEEDS TO BE IMPLEMENTED"""
            o.write("    priority: "+order.priority+"\n")
            if order.type=="kitting":
                o.write("    kitting_task:\n")
                o.write("      agv: "+order.agvNumber+"\n")
                o.write("      tray_id: "+order.trayId+"\n")
                o.write("      destination: \'"+order.destination+"\'\n")
                o.write("      products:\n")
                for prod in orderKittingParts:
                    if prod.orderId==order.id:
                        o.write("        - type: \'"+prod.type+"\'\n")
                        o.write("          color: \'"+prod.color+"\'\n")
                        o.write("          quadrant: "+prod.quadrant+"\n")
            else:
                o.write("    assembly_task:\n")
                o.write("      agv: ["+order.agvNumber+"]\n")
                o.write("      station: \'"+order.station+"\'\n")
                o.write("      products:\n")
                for prod in orderAssembParts:
                    if prod.orderId==order.id:
                        o.write("        - type: \'"+prod.type+"\'\n")
                        o.write("          color: \'"+prod.color+"\'\n")
                        o.write("          assembled_pose: # relative to briefcase frame\n")
                        o.write("            xyz: "+prod.xyz+"\n")
                        o.write("            rpy: "+prod.rpy+"\n")
                        o.write("          assembly_direction: "+prod.direction+"\n")
        o.write("\n# GLOBAL CHALLENGES\n")
        o.write("challenges:\n")
        for malf in robotMalfunctions:
            o.write("  - robot_malfunction:\n")
            o.write("      duration: "+malf.duration+"\n")
            o.write("      robots_to_disable: "+malf.robot+"\n")
            o.write("      part_type: \'"+malf.type+"\'\n")
            o.write("      part_color: \'"+malf.color+"\'\n")
            o.write("      agv: "+malf.agv+"\n")
        for part in faultyParts:
            o.write("  - faulty_part:\n")
            o.write("      order_id: \'"+part.orderID+"\'\n")
            o.write("      quadrant: ["+part.quadrant+"]\n")