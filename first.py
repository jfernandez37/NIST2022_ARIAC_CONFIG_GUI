import tkinter as tk


def tf():
    if tfOverBins.config('text')[-1] == 'True':
        tfOverBins.config(text='False')
        overBins.set("false")
    elif tfOverBins.config('text')[-1] == 'None':
        tfOverBins.config(text='True')
        overBins.set("true")
    else:
        tfOverBins.config(text='None')
        overBins.set("none")


def tf2():
    if tfOverStations.config('text')[-1] == 'True':
        tfOverStations.config(text='False')
        overStations.set("false")
    elif tfOverStations.config('text')[-1] == 'None':
        tfOverStations.config(text='True')
        overStations.set("true")
    else:
        tfOverStations.config(text='None')
        overStations.set("none")


def tf3():
    if tfStateLogging.config('text')[-1] == 'True':
        tfStateLogging.config(text='False')
        stateLogging.set("false")
    elif tfStateLogging.config('text')[-1] == 'None':
        tfStateLogging.config(text='True')
        stateLogging.set("true")
    else:
        tfStateLogging.config(text='None')
        stateLogging.set("none")


def cgt():
    if gripperTypeButton.config('text')[-1] == 'Gripper Tray':
        gripperTypeButton.config(text='Gripper Part')
        gripperType.set("gripper_part")
    else:
        gripperTypeButton.config(text='Gripper Tray')
        gripperType.set("gripper_tray")


def tl():
    if timeLimitButton.config('text')[-1] == '500':
        timeLimitButton.config(text='-1')
        timeLimit.set("-1")
    else:
        timeLimitButton.config(text='500')
        timeLimit.set("500")


def tray_skip():
    skipFlag.set("1")
    trayInfo.destroy()


if __name__ == "__main__":
    getFileName = tk.Tk()
    fileName = tk.StringVar()
    fileName.set("")
    fileNameLabel = tk.Label(getFileName, text="Enter the file name you would like to save as:")
    fileNameLabel.pack()
    fileNameTextBox = tk.Entry(getFileName, textvariable=fileName)
    fileNameTextBox.pack()
    fileExit = tk.Button(getFileName, text="Next", command=getFileName.destroy)
    fileExit.pack(pady=20)
    getFileName.mainloop()
    # END OF GETTING THE NAME OF THE FILE
    # ----------------------------------------------------------------------------------------------
    # BEGINNING OF OPTIONS
    options = tk.Tk()
    options.geometry("800x500")
    overBins = tk.StringVar()
    overBins.set("true")
    overBinsLabel = tk.Label(options, text="Insert models over bins:")
    overBinsLabel.pack()
    tfOverBins = tk.Button(text="True", width=12, command=tf)
    tfOverBins.pack(pady=5)
    popCycles = tk.StringVar()
    popCycles.set("0")
    popCycleLabel = tk.Label(options, text="Enter the belt population cycles (enter none to skip):")
    popCycleLabel.pack()
    popCycleBox = tk.Entry(options, textvariable=popCycles)
    popCycleBox.pack()
    overStations = tk.StringVar()
    overStations.set("true")
    overStationsLabel = tk.Label(options, text="Insert models over stations:")
    overStationsLabel.pack()
    tfOverStations = tk.Button(text="True", width=12, command=tf2)
    tfOverStations.pack(pady=5)
    stateLogging = tk.StringVar()
    stateLogging.set("true")
    stateLoggingLabel = tk.Label(options, text="Gazebo state logging:")
    stateLoggingLabel.pack()
    tfStateLogging = tk.Button(text="True", width=12, command=tf3)
    tfStateLogging.pack(pady=5)
    gripperType = tk.StringVar()
    gripperType.set("gripper_tray")
    gripperTypeLabel = tk.Label(options, text="Gripper type:")
    gripperTypeLabel.pack()
    gripperTypeButton = tk.Button(text="Gripper Tray", width=12, command=cgt)
    gripperTypeButton.pack(pady=5)
    timeLimit = tk.StringVar()
    timeLimit.set("500")
    timeLimitLabel = tk.Label(options, text="Time limit (-1-No time limit | 500-time used in qualifiers and finals):")
    timeLimitLabel.pack()
    timeLimitButton = tk.Button(text="500", width=12, command=tl)
    timeLimitButton.pack(pady=5)
    nextButton = tk.Button(options, text="Next", command=options.destroy)
    nextButton.pack(pady=20)
    options.mainloop()
    saveFileName = fileName.get()
    if '.yaml' not in saveFileName:
        saveFileName += '.yaml'
    with open(saveFileName, "a") as o:
        o.write("options:\n")
        if overBins.get() != 'none':
            o.write("\tinsert_models_over_bins: " + overBins.get()+"\n")
        if popCycles.get() != 'none':
            o.write("\tbelt_population_cycles: " + popCycles.get()+"\n")
        if overStations.get() != 'none':
            o.write("\tinsert_models_over_stations: "+overStations.get()+"\n")
        if stateLogging.get() != 'none':
            o.write("\tgazebo_state_logging: "+stateLogging.get()+"\n")
        o.write("\t# mandatory: gripper_tray or gripper_part\n")
        o.write("\tcurrent_gripper_type: "+gripperType.get()+"\n")
        o.write("\ttime_limit: "+timeLimit.get()+"\n")
    # END OF GETTING OPTIONS
    # ----------------------------------------------------------------------------------------------------------------------
    # BEGINNING OF TABLE_TRAY_INFOS
    trayInfo = tk.Tk()
    trayInstructions = tk.Label(trayInfo, text="If you would like to skip a tray, leave it blank, leave it blank")
    trayInstructions.pack()
    table1 = tk.StringVar()
    table1.set("")
    table1Label = tk.Label(trayInfo, text="Choose the material for table 1")
    table1Label.pack()
    table1Menu = tk.OptionMenu(trayInfo, table1, "", "movable_tray_dark_wood", "movable_tray_light_wood", "movable_tray_metal_rusty", "movable_tray_metal_shiny")
    table1Menu.pack()
    table1q = tk.StringVar()
    table1q.set("")
    table1qLabel = tk.Label(trayInfo, text="Choose the quantity for table 1")
    table1qLabel.pack()
    table1qMenu = tk.OptionMenu(trayInfo, table1q, "", "1", "2", "3")
    table1qMenu.pack()
    table2 = tk.StringVar()
    table2.set("")
    table2Label = tk.Label(trayInfo, text="Choose the material for table 2")
    table2Label.pack()
    table2Menu = tk.OptionMenu(trayInfo, table2, "", "movable_tray_dark_wood", "movable_tray_light_wood", "movable_tray_metal_rusty", "movable_tray_metal_shiny")
    table2Menu.pack()
    table2q = tk.StringVar()
    table2q.set("")
    table2qLabel = tk.Label(trayInfo, text="Choose the quantity for table 2")
    table2qLabel.pack()
    table2qMenu = tk.OptionMenu(trayInfo, table2q, "", "1", "2", "3")
    table2qMenu.pack()
    trayNext = tk.Button(trayInfo, text="Next", command=trayInfo.destroy)
    trayNext.pack(pady=20)
    skipFlag = tk.StringVar()
    skipFlag.set("0")
    skipButton = tk.Button(trayInfo, text="Skip", command=tray_skip)
    skipButton.pack()
    trayInfo.mainloop()
    if skipFlag == "0":
        with open(saveFileName, "a") as o:
            if (table1.get() != "" and table1q.get() != "") or table2.get() != "" and table2q.get() != "":
                o.write("\n\n\ntable_tray_infos:\n")
            if table1.get() != "" and table1q.get() != "":
                o.write("\ttable_1:\n")
                o.write("\t\ttray_model: "+table1.get()+"\n")
                o.write("\t\tquantity: "+table1q.get()+"\n")
            if table2.get() != "" and table2q.get() != "":
                o.write("\ttable_2:\n")
                o.write("\t\ttray_model: "+table2.get()+"\n")
                o.write("\t\tquantity: "+table2q.get()+"\n")
    # END OF TABLE MENUS
    # -----------------------------------------------------------------------------------
    # BEGINNING OF GETTING AGV LOCATIONS
    agvInfo = tk.Tk()
    
