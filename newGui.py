import tkinter as tk
import tkinter.ttk as ttk
import platform
from os import chdir
from functools import partial
from PIL import Image, ImageTk  # needed for images in gui
from jsonschema import validate
import yaml
import Functions.validateARIAC as validateARIAC
from Functions.allClasses import *
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
pathIncrement = []  # gives the full path for recursive deletion
createdDir = []  # to deleted directories made if canceled
leftColumn=0
middleColumn=1 
middleColumnWidth=62  # width of middle margin for live yaml windows
rightColumn=2
nameLabels = []  # holds temporary flags to be deleted
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
    saveTrayButton=tk.Button(trayWind, text="Save and Continue", command=trayWind.destroy)
    saveTrayButton.grid(column=middleColumn,pady=20)
    cancel_tray_command=partial(cancel_wind, trayWind, cancelFlag)
    cancelTrayButton=tk.button(trayWind, text="Cancel and Exit", command=cancel_tray_command)
    cancelTrayButton.grid(column=middleColumn,pady=20)
    trayWind.mainloop()
