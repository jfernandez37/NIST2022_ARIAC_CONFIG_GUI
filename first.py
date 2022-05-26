import tkinter as tk
import os.path
from os import path


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


def get_file_name_next():
    if fileName.get() == "" and reqFlag.get() == "0":
        req_label = tk.Label(getFileName, text="This field is required. Please enter a non-empty file name")
        req_label.pack()
        reqFlag.set('1')
    if (path.exists(fileName.get()) or path.exists(fileName.get()+'.yaml')) and existFlag.get() == '0':
        exist_label = tk.Label(getFileName, text="A file with this name already exists. Please enter another file name.")
        exist_label.pack()
        existFlag.set('1')
    elif fileName.get() != '':
        getFileName.destroy()
        

def add_product():
    product_info = tk.Toplevel()
    x_val = tk.StringVar()
    x_val.set('0')
    y_val = tk.StringVar()
    y_val.set('0')
    z_val = tk.StringVar()
    z_val.set('0')
    r_x_val = tk.StringVar()
    r_x_val.set('0')
    r_y_val = tk.StringVar()
    r_y_val.set('0')
    r_z_val = tk.StringVar()
    r_z_val.set('0')
    agv_id = tk.StringVar(product_info)
    product_menu_label = tk.Label(product_info, text="Choose the agv for the product:")
    product_menu_label.pack()
    product_menu = tk.OptionMenu(product_info, agv_id, "agv1", "agv2", "agv3", "agv4")
    product_menu.pack()
    product_type = tk.StringVar(product_info)
    product_type_menu_label = tk.Label(product_info, text="Choose the product type:")
    product_type_menu_label.pack()
    product_type_menu = tk.OptionMenu(product_info, product_type, "assembly_battery_red", "assembly_battery_green"
                                      ,"assembly_battery_blue", "assembly_pump_red","assembly_pump_green"
                                      ,"assembly_pump_blue", "assembly_regulator_red",
                                      "assembly_regulator_green","assembly_regulator_blue")
    product_type_menu.pack()
    x_val_label = tk.Label(product_info, text="Enter the x value")
    x_val_label.pack()
    x_val_entry = tk.Entry(product_info, textvariable=x_val)
    x_val_entry.pack()
    y_val_label = tk.Label(product_info, text="Enter the y value")
    y_val_label.pack()
    y_val_entry = tk.Entry(product_info, textvariable=y_val)
    y_val_entry.pack()
    z_val_label = tk.Label(product_info, text="Enter the z value")
    z_val_label.pack()
    z_val_entry = tk.Entry(product_info, textvariable=z_val)
    z_val_entry.pack()
    r_x_val_label = tk.Label(product_info, text="Enter the x rotation value")
    r_x_val_label.pack()
    r_x_val_entry = tk.Entry(product_info, textvariable=r_x_val)
    r_x_val_entry.pack()
    r_y_val_label = tk.Label(product_info, text="Enter the y rotation value")
    r_y_val_label.pack()
    r_y_val_entry = tk.Entry(product_info, textvariable=r_y_val)
    r_y_val_entry.pack()
    r_z_val_label = tk.Label(product_info, text="Enter the z rotation value")
    r_z_val_label.pack()
    r_z_val_entry = tk.Entry(product_info, textvariable=r_z_val)
    r_z_val_entry.pack()
    product_info.geometry("500x500")
    prod_save = tk.Button(product_info, text="Save and Exit", command=product_info.destroy)
    prod_save.pack(pady=20)
    product_info.mainloop()
    if agv_id.get() == 'agv1':
        agv1ProdTypes.set(agv1ProdTypes.get()+' '+product_type.get())
        agv1Coords.set(agv1Coords.get()+' '+"["+x_val.get()+','+y_val.get()+','+z_val.get()+"]")
        agv1Rot.set(agv1Rot.get()+' '+'['+r_x_val.get()+','+r_y_val.get()+','+r_z_val.get()+']')
    if agv_id.get() == 'agv2':
        agv2ProdTypes.set(agv2ProdTypes.get()+' '+product_type.get())
        agv2Coords.set(agv2Coords.get() + ' ' + "[" + x_val.get() + ',' + y_val.get() + ',' + z_val.get() + "]")
        agv2Rot.set(agv2Rot.get() + ' ' + '[' + r_x_val.get() + ',' + r_y_val.get() + ',' + r_z_val.get() + ']')
    if agv_id.get() == 'agv3':
        agv3ProdTypes.set(agv3ProdTypes.get()+' '+product_type.get())
        agv3Coords.set(agv3Coords.get() + ' ' + "[" + x_val.get() + ',' + y_val.get() + ',' + z_val.get() + "]")
        agv3Rot.set(agv3Rot.get() + ' ' + '[' + r_x_val.get() + ',' + r_y_val.get() + ',' + r_z_val.get() + ']')
    if agv_id.get() == 'agv4':
        agv4ProdTypes.set(agv4ProdTypes.get()+' '+product_type.get())
        agv4Coords.set(agv4Coords.get() + ' ' + "[" + x_val.get() + ',' + y_val.get() + ',' + z_val.get() + "]")
        agv4Rot.set(agv4Rot.get() + ' ' + '[' + r_x_val.get() + ',' + r_y_val.get() + ',' + r_z_val.get() + ']')


if __name__ == "__main__":
    getFileName = tk.Tk()
    getFileName.title("NIST ARIAC CONFIG GUI")
    fileName = tk.StringVar()
    fileName.set("")
    reqFlag = tk.StringVar()
    reqFlag.set("0")
    existFlag = tk.StringVar()
    existFlag.set("0")
    fileNameLabel = tk.Label(getFileName, text="Enter the file name you would like to save as:")
    fileNameLabel.pack()
    fileNameTextBox = tk.Entry(getFileName, textvariable=fileName)
    fileNameTextBox.pack()
    fileExit = tk.Button(getFileName, text="Next", command=get_file_name_next)
    fileExit.pack(pady=20)
    getFileName.mainloop()
    # END OF GETTING THE NAME OF THE FILE
    # ----------------------------------------------------------------------------------------------
    # BEGINNING OF OPTIONS
    options = tk.Tk()
    options.title("Options")
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
    trayInfo.title("Tray Information")
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
    if skipFlag.get() == "0":
        with open(saveFileName, "a") as o:
            if (table1.get() != "" and table1q.get() != "") or (table2.get() != "" and table2q.get() != ""):
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
    # BEGINNING OF GETTING AGV_INFOS
    agvInfo = tk.Tk()
    agvInfo.title("AGV Information")
    agv1 = tk.StringVar()
    agv1.set("ks1")
    agv1Label = tk.Label(agvInfo, text="AGV1 Location:")
    agv1Label.pack()
    agv1Menu = tk.OptionMenu(agvInfo, agv1, "ks1", "as1", "as2")
    agv1Menu.pack()
    agv1ProdTypes = tk.StringVar()
    agv1ProdTypes.set('')
    agv1Coords = tk.StringVar()
    agv1Coords.set('')
    agv1Rot=tk.StringVar()
    agv1Rot.set('')
    agv2 = tk.StringVar()
    agv2.set("ks2")
    agv2Label = tk.Label(agvInfo, text="AGV2 Location:")
    agv2Label.pack()
    agv2Menu = tk.OptionMenu(agvInfo, agv2, "ks2", "as1", "as2")
    agv2Menu.pack()
    agv2ProdTypes = tk.StringVar()
    agv2ProdTypes.set('')
    agv2Coords = tk.StringVar()
    agv2Coords.set('')
    agv2Rot = tk.StringVar()
    agv2Rot.set('')
    agv3 = tk.StringVar()
    agv3.set("ks3")
    agv3Label = tk.Label(agvInfo, text="AGV3 Location:")
    agv3Label.pack()
    agv3Menu = tk.OptionMenu(agvInfo, agv3, "ks3", "as3", "as4")
    agv3Menu.pack()
    agv3ProdTypes = tk.StringVar()
    agv3ProdTypes.set('')
    agv3Coords = tk.StringVar()
    agv3Coords.set('')
    agv3Rot = tk.StringVar()
    agv3Rot.set('')
    agv4 = tk.StringVar()
    agv4.set("ks4")
    agv4Label = tk.Label(agvInfo, text="AGV4 Location:")
    agv4Label.pack()
    agv4Menu = tk.OptionMenu(agvInfo, agv4, "ks4", "as3", "as4")
    agv4Menu.pack()
    agv4ProdTypes = tk.StringVar()
    agv4ProdTypes.set('')
    agv4Coords = tk.StringVar()
    agv4Coords.set('')
    agv4Rot = tk.StringVar()
    agv4Rot.set('')
    productButton = tk.Button(agvInfo, text="Add Product", command=add_product)
    productButton.pack(pady=20)
    agvNext = tk.Button(agvInfo, text="Next", command=agvInfo.destroy)
    agvNext.pack(pady=20)
    agvInfo.mainloop()
    partID=0
    index=0
    agv1CArr = agv1Coords.get().split(" ")
    agv2CArr = agv2Coords.get().split(" ")
    agv3CArr = agv3Coords.get().split(" ")
    agv4CArr = agv4Coords.get().split(" ")
    agv1RArr = agv1Rot.get().split(' ')
    agv2RArr = agv2Rot.get().split(' ')
    agv3RArr = agv3Rot.get().split(' ')
    agv4RArr = agv4Rot.get().split(' ')
    with open(saveFileName, "a") as o:
        o.write("\n\nagv_infos:\n")
        o.write("\tagv1:\n")
        o.write("\t\tlocation: " + agv1.get() + "\n")
        if len(agv1ProdTypes.get()) != 0:
            o.write("\t\tproducts:\n")
            for i in agv1ProdTypes.get().split(' '):
                if i != '':
                    o.write("\t\t\tpart_"+str(partID)+":\n")
                    o.write("\t\t\t\ttype: " + i + "\n" )
                    o.write("\t\t\t\tpose: \n")
                    o.write("\t\t\t\t\txyz: " + agv1CArr[index+1]+"\n")
                    o.write("\t\t\t\t\trpy: " + agv1RArr[index+1] + "\n")
                    partID += 1
                    index += 1
        index = 0
        o.write("\tagv2:\n")
        o.write("\t\tlocation: " + agv2.get() + "\n")
        if len(agv2ProdTypes.get()) != 0:
            o.write("\t\tproducts:\n")
            for i in agv2ProdTypes.get().split(' '):
                if i != '':
                    o.write("\t\t\tpart_"+str(partID)+":\n")
                    o.write("\t\t\t\ttype: " + i + "\n" )
                    o.write("\t\t\t\tpose: \n")
                    o.write("\t\t\t\t\txyz: " + agv2CArr[index+1]+"\n")
                    o.write("\t\t\t\t\trpy: " + agv2RArr[index+1] + "\n")
                    partID += 1
                    index += 1
        index = 0
        o.write("\tagv3:\n")
        o.write("\t\tlocation: " + agv3.get() + "\n")
        if len(agv3ProdTypes.get()) != 0:
            o.write("\t\tproducts:\n")
            for i in agv3ProdTypes.get().split(' '):
                if i != '':
                    o.write("\t\t\tpart_"+str(partID)+":\n")
                    o.write("\t\t\t\ttype: " + i + "\n" )
                    o.write("\t\t\t\tpose: \n")
                    o.write("\t\t\t\t\txyz: " + agv3CArr[index+1]+"\n")
                    o.write("\t\t\t\t\trpy: " + agv3RArr[index + 1] + "\n")
                    partID += 1
                    index += 1
        index = 0
        o.write("\tagv4:\n")
        o.write("\t\tlocation: " + agv4.get() + "\n")
        if len(agv4ProdTypes.get()) != 0:
            o.write("\t\tproducts:\n")
            for i in agv4ProdTypes.get().split(' '):
                if i != '':
                    o.write("\t\t\tpart_"+str(partID)+":\n")
                    o.write("\t\t\t\ttype: " + i + "\n" )
                    o.write("\t\t\t\tpose: \n")
                    o.write("\t\t\t\t\txyz: " + agv4CArr[index+1]+"\n")
                    o.write("\t\t\t\t\trpy: " + agv4RArr[index + 1] + "\n")
                    partID += 1
                    index += 1
