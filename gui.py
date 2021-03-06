import tkinter as tk
import tkinter.ttk as ttk
import math
import platform
import os.path
from os import chdir, path
import os
from pathlib import Path
from functools import partial
from PIL import Image, ImageTk  # needed for images in gui

orderCount = []  # Used in counter in new_order function
tempKits = []  # holds kitting information for orders
tempAssemb = []  # holds assembly information for orders
kitProds = []  # holds products for kitting in orders
assembProds = []  # holds products for assembly in orders
orderInd = 0  # index for reading through the orders
kProdInd = []  # holds the indices for products in kitting
aProdInd = []  # holds the indices for products in assembly
prodList = ["assembly_battery_red", "assembly_battery_green",
            "assembly_battery_blue", "assembly_pump_red", "assembly_pump_green",
            "assembly_pump_blue", "assembly_regulator_red",
            "assembly_regulator_green", "assembly_regulator_blue", "assembly_sensor_red",
            "assembly_sensor_green", "assembly_sensor_blue"]  # list of all parts
agv1List = ['ks1', 'as1', 'as2']  # all possible locations for agv1
agv2List = ['ks2', 'as1', 'as2']  # all possible locations for agv2
agv3List = ['ks3', 'as3', 'as4']  # all possible locations for agv3
agv4List = ['ks4', 'as3', 'as4']  # all possible locations for agv4
kAgv1List = ['[ks1]', '[as1]', '[as2]']  # all possible locations for agv1 in the kitting format
kAgv2List = ['[ks2]', '[as1]', '[as2]']  # all possible locations for agv2 in the kitting format
kAgv3List = ['[ks3]', '[as3]', '[as4]']  # all possible locations for agv3 in the kitting format
kAgv4List = ['[ks4]', '[as3]', '[as4]']  # all possible locations for agv4 in the kitting format
allStations = ['ks1', 'ks2', 'ks3', 'ks4', 'as1', 'as2', 'as3', 'as4']  # list of all locations
trayTypes = ["movable_tray_dark_wood", "movable_tray_light_wood",
             "movable_tray_metal_rusty", "movable_tray_metal_shiny"]  # list of all tray types
modelsOverBinsInfo = []  # holds the information from the models over bins function
modelsOverStationsInfo = []  # holds all the information from the models over stations function
beltCycleInfo = []  # holds all the information from the belt cycle function
faultyProdList = []  # holds all the information for the faulty product menu
dropsInfo = []  # holds all the information for the drops menu
agv1Prods = []  # holds the products on agv1
agv2Prods = []  # holds the products on agv2
agv3Prods = []  # holds the products on agv3
agv4Prods = []  # holds the products on agv4
binProds = []  # holds the products which are present in bins
nameLabels = []  # holds temporary flags to be deleted
kittingShipTempInput = []
round_slide = .05  # what coordinates are rounded to
if platform.system()=="Windows": #allows paths as inputs for linux
    invalidFileChar = " /~`,;\"\'\\!@#$%^&*()+=[]"  # characters not allowed in file names for windows
else:
    invalidFileChar = " `,;\"\'\\!@#$%^&*()+=[]"  # characters not allowed in file names for linux
createdDir = []  # to deleted directories made if canceled
pathIncrement = []  # gives the full path for recursive deletion
firstLengths = []  # holds the number of products in the first order


def correct_file_name(tempFileName, a, b , c):  # deletes any invalid characters in file name
    """This function removes any characters which can not be used in the file name. It does so as the user is typing"""
    tempStr = tempFileName.get()
    for char in invalidFileChar:
        if char in tempStr:
            tempStr = tempStr.replace(char, '')
    tempFileName.set(tempStr)


def exitAndFlag(window, parFlag):
    """Exits the given window and activates the given flag"""
    parFlag.set('1')
    window.destroy()

def activateButton(button, parFlag, c, d, e):
    """Depending on the status of the flag, it will activate a deactivated button"""
    if parFlag.get() == '1':
        button.config(state=tk.NORMAL)


def deactivateButton(button, parFlag, c, d, e):
    """Depending on the status of the flag, it will deactivate an activated button"""
    if parFlag.get() =='1':
        button.config(state=tk.DISABLED)

def get_final_num(num):  # returns the final string for the coordinates
    """For returning the number for the sliders. Not used anymore"""
    return str(round_twentieth(float(num.get())))


def round_twentieth(num):  # rounds number to the nearest twentieth (or round_slide)
    """Rounds a number to the nearest 0.05. This function was used for the sliders and is not used any more"""
    return round(round(num/round_slide)*round_slide,-int(math.floor(math.log10(round_slide))))


def tf():  # cycles through the true or false button for the over bins option
    """Cycles through the options for the Models Over Bins Button"""
    if tfOverBins.config('text')[-1] == 'True':
        tfOverBins.config(text='False')
        overBins.set("false")
    elif tfOverBins.config('text')[-1] == 'False':
        tfOverBins.config(text='True')
        overBins.set("true")
    #else:
        #tfOverBins.config(text='Skip')
        #overBins.set("skip")


def tf2():  # cycles through the true or false button for the over stations option
    """Cycles through the options for the Models Over Stations Button"""
    if tfOverStations.config('text')[-1] == 'True':
        tfOverStations.config(text='False')
        overStations.set("false")
    elif tfOverStations.config('text')[-1] == 'False':
        tfOverStations.config(text='True')
        overStations.set("true")
    #else:
        #tfOverStations.config(text='Skip')
        #overStations.set("skip")


def tf3():  # cycles through the true or false button for the gazebo state logging option
    """Cycles through the options for the Gazebo State Logging"""
    if tfStateLogging.config('text')[-1] == 'True':
        tfStateLogging.config(text='False')
        stateLogging.set("false")
    elif tfStateLogging.config('text')[-1] == 'False':
        tfStateLogging.config(text='True')
        stateLogging.set("true")
    #else:
        #tfStateLogging.config(text='Skip')
        #stateLogging.set("skip")


def cgt():  # cycles through the options for the current gripper type option
    """Cycles through the options for the Gripper Type button"""
    if gripperTypeButton.config('text')[-1] == 'Gripper Tray':
        gripperTypeButton.config(text='Gripper Part')
        gripperType.set("gripper_part")
    else:
        gripperTypeButton.config(text='Gripper Tray')
        gripperType.set("gripper_tray")


def tl():  # cycles through the options for the time limit option
    """Cycles through the options for the Time Limit button"""
    if timeLimitButton.config('text')[-1] == '500':
        timeLimitButton.config(text='-1')
        timeLimit.set("-1")
    else:
        timeLimitButton.config(text='500')
        timeLimit.set("500")


def skip_wind(flag, window):  # function for skipping a window
    """Sets a given flag and destroys a windos for skip buttons"""
    flag.set('1')
    window.destroy()


def get_file_name_next():  # checks to see if the file name the user selects exists or is empty
    """Reads the file name and puts a message on the window if invalid characters are found
    the file is empty, or if the file inputted already exists"""
    inv_char_found = []
    output_inv = ''
    c=1
    for i in fileName.get():
        if i in invalidFileChar:
            inv_char_found.append(i)
    if len(inv_char_found)>0:
        output_inv+="\""+inv_char_found[0]+"\""
        for i in inv_char_found[1:]:
            c+=1
            if c==len(inv_char_found):
                output_inv+=", and \""+i+"\""
            else:
                output_inv+=", \""+i+"\""
    if len(inv_char_found)!=0 and invalidFlag.get()=='0':
        for label in nameLabels:
            label.destroy()
        nameLabels.clear()
        invalid_char_label = tk.Label(getFileName, text="The name entered contains invalid characters: "+output_inv)
        invalid_char_label.pack()
        nameLabels.append(invalid_char_label)
        invalidFlag.set('1')
        reqFlag.set('0')
        existFlag.set('0')
        inv_char_found.clear()
        output_inv = ''
        c=0
    elif fileName.get() == "" and reqFlag.get() == "0":
        for label in nameLabels:
            label.destroy()
        nameLabels.clear()
        req_label = tk.Label(getFileName, text="This field is required. Please enter a non-empty file name")
        req_label.pack()
        nameLabels.append(req_label)
        reqFlag.set('1')
        invalidFlag.set('0')
        existFlag.set('0')
    elif (path.exists(fileName.get()) or path.exists(fileName.get() + '.yaml')) and existFlag.get() == '0':
        for label in nameLabels:
            label.destroy()
        nameLabels.clear()
        exist_label = tk.Label(getFileName,
                               text="A file with this name already exists. Please enter another file name.")
        exist_label.pack()
        nameLabels.append(exist_label)
        existFlag.set('1')
        invalidFlag.set('0')
        reqFlag.set('0')
    elif fileName.get() != '' and not (path.exists(fileName.get()) or path.exists(fileName.get() + '.yaml')) and invalidFlag.get()!='1':
        getFileName.destroy()
    invalidFlag.set('0')


def cancel_func(wind, flag):
    """Sets flag to 1 and destroys a window for when the user wants to cancel and exit"""
    wind.destroy()
    flag.set("1")

def update_val_label(label, func, c, d, e):  # for having the current number for the slider
    """Live label for the current value of a slider. Not being used"""
    label.configure(text="Current value = "+func())


def get_current_val(val):  # gets the current number from the slider
    """Gets the current value of a slider rounded to a twentieth for the live label. Not being used right now"""
    return '{: .2f}'.format(round_twentieth(float(val.get())))


def add_product():  # adds a product in agv_infos
    """Adds a product in the agv_infos section. Returns the value through arrays depending on which AGV the user decides to put the product on"""
    product_info = tk.Toplevel()
    add_product_cancel_flag = tk.StringVar()
    add_product_cancel_flag.set("0")
    x_val = tk.StringVar()
    x_val.set('0')
    y_val = tk.StringVar()
    y_val.set('0')
    z_val = tk.StringVar()
    z_val.set('0')
    r_val = tk.StringVar()
    r_val.set('0')
    p_val = tk.StringVar()
    p_val.set('0')
    y_rpy_val = tk.StringVar()
    y_rpy_val.set('0')
    agv_id = tk.StringVar(product_info)
    agv_id.set("agv1")
    product_menu_label = tk.Label(product_info, text="Choose the agv for the product:")
    product_menu_label.pack()
    product_menu = tk.OptionMenu(product_info, agv_id, "agv1", "agv2", "agv3", "agv4")
    product_menu.pack()
    product_type = tk.StringVar(product_info)
    product_type.set(prodList[0])
    product_type_menu_label = tk.Label(product_info, text="Choose the product type:")
    product_type_menu_label.pack()
    product_type_menu = tk.OptionMenu(product_info, product_type, *prodList)
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
    r_val_label = tk.Label(product_info, text="Enter the r value")
    r_val_label.pack()
    r_val_entry = tk.Entry(product_info, textvariable=r_val)
    r_val_entry.pack()
    p_val_label = tk.Label(product_info, text="Enter the p value")
    p_val_label.pack()
    p_val_entry = tk.Entry(product_info, textvariable=p_val)
    p_val_entry.pack()
    y_rpy_val_label = tk.Label(product_info, text="Enter the y (rpy) value")
    y_rpy_val_label.pack()
    y_rpy_val_entry = tk.Entry(product_info, textvariable=y_rpy_val)
    y_rpy_val_entry.pack()
    product_info.geometry("500x750")
    cancel_prod_func = partial(cancel_func, product_info, add_product_cancel_flag)
    cancel_prod_button = tk.Button(product_info, text="Cancel", command=cancel_prod_func)
    cancel_prod_button.pack()
    prod_save = tk.Button(product_info, text="Save and Exit", command=product_info.destroy)
    prod_save.pack(pady=20)
    product_info.mainloop()
    if add_product_cancel_flag.get()=="0":
        if agv_id.get() == 'agv1':
            agv1Prods.append(Products(product_type.get(),
                                    str("["+x_val.get()+", "+y_val.get()+", "+z_val.get()+"]"),
                                    str("["+r_val.get()+", "+p_val.get()+", "+y_rpy_val.get()+"]")))
        if agv_id.get() == 'agv2':
            agv2Prods.append(Products(product_type.get(),
                                    str("["+x_val.get()+", "+y_val.get()+", "+z_val.get()+"]"),
                                    str("["+r_val.get()+", "+p_val.get()+", "+y_rpy_val.get()+"]")))
        if agv_id.get() == 'agv3':
            agv3Prods.append(Products(product_type.get(),
                                    str("["+x_val.get()+", "+y_val.get()+", "+z_val.get()+"]"),
                                    str("["+r_val.get()+", "+p_val.get()+", "+y_rpy_val.get()+"]")))
        if agv_id.get() == 'agv4':
            agv4Prods.append(Products(product_type.get(),
                                    str("["+x_val.get()+", "+y_val.get()+", "+z_val.get()+"]"),
                                    str("["+r_val.get()+", "+p_val.get()+", "+y_rpy_val.get()+"]")))


def new_order():  # this menu pops up to make a new order for the user
    """Adds a new order. Returns the order using the all orders array. Different values are returned for the first order
    different components of the menu are present for the second order selection"""
    if len(orderCount)>=1:
        secondOrderFlag.set('1')
    global tempKits
    global tempAssemb
    orderCount.append(0)
    add_order = tk.Toplevel()
    kittingFlag.set('0')
    kittingFlag.set('0')
    temp_priority = tk.StringVar()
    temp_priority.set('Regular')
    temp_k_health = tk.StringVar()
    temp_k_health.set('1')
    temp_a_health = tk.StringVar()
    temp_a_health.set('1')
    temp_announcement_cond = tk.StringVar()
    temp_announcement_cond.set('time')
    temp_ann_val = tk.StringVar()
    temp_ann_val.set('0')
    if len(orderCount) > 1:  # only occurs for order_1
        get_priority_label = tk.Label(add_order, text="Enter the priority of the order")
        get_priority_label.pack()
        get_priority = tk.OptionMenu(add_order, temp_priority, "Regular", "High Priority")
        get_priority.pack()
    get_k_health_label = tk.Label(add_order, text="Select the kitting robot health of the order")
    get_k_health_label.pack()
    get_k_health = tk.OptionMenu(add_order, temp_k_health, "0", "1")
    get_k_health.pack()
    get_a_health_label = tk.Label(add_order, text="Select the assembly robot health of the order")
    get_a_health_label.pack()
    get_a_health = tk.OptionMenu(add_order, temp_a_health, "0", "1")
    get_a_health.pack()
    if len(orderCount) > 1:  # only occurs for order_1
        get_announcement_condition_label = tk.Label(add_order, text="Enter the announcement condition of the order")
        get_announcement_condition_label.pack()
        get_announcement_condition = tk.Entry(add_order, textvariable=temp_announcement_cond)
        get_announcement_condition.pack()
    get_ann_val_label = tk.Label(add_order, text="Enter the announcement value of the order")
    get_ann_val_label.pack()
    get_ann_val = tk.Entry(add_order, textvariable=temp_ann_val)
    get_ann_val.pack()
    order_kitting = tk.Button(add_order, text="Kitting", command=kitting, state=tk.NORMAL)
    order_kitting.pack(pady=20)
    order_assembly = tk.Button(add_order, text="Assembly", command=assembly, state=tk.NORMAL)
    order_assembly.pack(pady=20)
    orderExitFunc = partial(exitAndFlag, add_order, orderNextFlag)
    order_save = tk.Button(add_order, text="Save and Exit", command=orderExitFunc, state=tk.DISABLED)
    order_save.pack(pady=20)
    orderActButtonFunc = partial(activateButton, order_save, orderFlag)
    deactivateKitting = partial(deactivateButton, order_kitting, kittingFlag)
    deactivateAssemb = partial(deactivateButton, order_assembly, assembFlag)
    orderFlag.trace('w', orderActButtonFunc)
    kittingFlag.trace('w', deactivateKitting)
    assembFlag.trace('w', deactivateAssemb)
    add_order.mainloop()
    if len(firstLengths)==0:
        if len(tempKits)>1:
            firstLengths.append(len(tempKits[1].products))
        elif len(tempKits)>0:
            firstLengths.append(len(tempKits[0].products))
        else:
            firstLengths.append(0)
        if len(tempAssemb)>1:
            firstLengths.append(len(tempAssemb[1].products))
        elif len(tempAssemb)>0:
            firstLengths.append(len(tempAssemb[0].products))
        else:
            firstLengths.append(0)
    if temp_priority.get()=="Regular":
        priority_val = 1
    else:
        priority_val=3
    if len(orderCount) == 1:
        allOrders.append(Order('1', temp_k_health.get(), temp_a_health.get(),
                               "time", temp_ann_val.get(), tempKits, tempAssemb))
        tempKits = []
        tempAssemb = []
    else:
        allOrders.append(Order(str(priority_val), temp_k_health.get(), temp_a_health.get(),
                               temp_announcement_cond.get(), temp_ann_val.get(), tempKits, tempAssemb))
        tempKits = []
        tempAssemb = []
    #if len(tempKits) != 0:  # checks if there are products present to avoid errors
        #kProdInd.append(len(tempKits[len(allOrders)-1].products)-1)
    #if len(tempAssemb) != 0:
        #aProdInd.append(len(tempAssemb[len(allOrders)-1].products)-1)


def update_dest(a, b, c, d, e, f):  # switches the options present based off of the agv selected
    """Updates the possible stations for agvs"""
    menu = a['menu']
    menu.delete(0, 'end')
    if b.get() == 'agv1':
        c.set(kAgv1List[0])
        for dest in kAgv1List:
            menu.add_command(label=dest, command=lambda dest=dest: c.set(dest))
    elif b.get() == 'agv2':
        c.set(kAgv2List[0])
        for dest in kAgv2List:
            menu.add_command(label=dest, command=lambda dest=dest: c.set(dest))
    elif b.get() == 'agv3':
        c.set(kAgv3List[0])
        for dest in kAgv3List:
            menu.add_command(label=dest, command=lambda dest=dest: c.set(dest))
    else:
        c.set(kAgv4List[0])
        for dest in kAgv4List:
            menu.add_command(label=dest, command=lambda dest=dest: c.set(dest))


def update_id_range(a, b, c, d, e, f):  # updates the ids for faulty products
    """Updates the range of possible id's based on bins"""
    menu = a['menu']
    menu.delete(0, 'end')
    bin_prods_ind = 0
    for binProd in binProds:
        if binProd.pType == b.get():
            break
        bin_prods_ind += 1
    c.set('1')
    for num in range(int(binProds[bin_prods_ind].pNum)):
        temp_num = str(num + 1)
        menu.add_command(label=temp_num, command=lambda temp_num=temp_num: c.set(temp_num))


def update_kitting_ship(second_tray, second_agv, ship_count, second_dest, window, d,e,f):  # updates the trays for kitting shipments
    """Updates the kitting menu based on the shipment count"""
    if ship_count.get() == '1':
        second_tray.set('')
        second_agv.set('')
        second_dest.set('')
        for entry in kittingShipTempInput:
            entry.destroy()
    else:
        second_tray.set(trayTypes[0])
        second_agv.set('agv1')
        second_dest.set(kAgv1List[0])
        second_k_tray = tk.Label(window, text="Second Kitting Tray")
        second_k_tray.pack()
        second_get_tray = tk.OptionMenu(window, second_tray, *trayTypes)
        second_get_tray.pack()
        second_k_agv_label = tk.Label(window, text="Enter the second Kitting agv")
        second_k_agv_label.pack()
        second_get_agv = tk.OptionMenu(window, second_agv, "agv1", "agv2", "agv3", "agv4")
        second_get_agv.pack()
        second_k_dest_label = tk.Label(window, text="Enter the second Kitting destination")
        second_k_dest_label.pack()
        second_get_k_dest = tk.OptionMenu(window, second_dest, *kAgv1List)
        second_get_k_dest.pack()
        second_update_with_arg = partial(update_dest, second_get_k_dest, second_agv, second_dest)
        second_agv.trace('w', second_update_with_arg)
        kittingShipTempInput.append(second_k_tray)
        kittingShipTempInput.append(second_get_tray)
        kittingShipTempInput.append(second_k_agv_label)
        kittingShipTempInput.append(second_get_agv)
        kittingShipTempInput.append(second_k_dest_label)
        kittingShipTempInput.append(second_get_k_dest)


def kitting():  # allows the user to add kitting to an order
    """Adds a new kitting order to the orders. Returned through tempKits"""
    kitting_wind = tk.Toplevel()
    second_tray = tk.StringVar()
    second_tray.set('')
    second_agv = tk.StringVar()
    second_agv.set('')
    second_dest = tk.StringVar()
    second_dest.set('')
    ship_count = tk.StringVar()
    ship_count.set('1')
    trays = tk.StringVar()
    trays.set('movable_tray_metal_rusty')
    k_agv = tk.StringVar()
    k_agv.set('agv1')
    k_destination = tk.StringVar()
    k_destination.set('[ks1]')  # list of as choices
    k_ship_count = tk.Label(kitting_wind, text="Enter the shipping count")
    k_ship_count.pack()
    ship_count_menu = tk.OptionMenu(kitting_wind, ship_count, "1", "2")
    ship_count_menu.pack()
    k_trays = tk.Label(kitting_wind, text="Kitting Tray")
    k_trays.pack()
    get_tray = tk.OptionMenu(kitting_wind, trays, *trayTypes)
    get_tray.pack()
    k_agv_label = tk.Label(kitting_wind, text="Enter the Kitting agv")
    k_agv_label.pack()
    get_agv = tk.OptionMenu(kitting_wind, k_agv, "agv1", "agv2", "agv3", "agv4")
    get_agv.pack()
    k_dest_label = tk.Label(kitting_wind, text="Enter the Kitting destination")
    k_dest_label.pack()
    get_k_dest = tk.OptionMenu(kitting_wind, k_destination, *agv1List)
    get_k_dest.pack()
    kittingAddedFunc = partial(exitAndFlag, kitting_wind, orderFlag)
    order_kitting = tk.Button(kitting_wind, text="Save and Exit", command=kittingAddedFunc, state=tk.DISABLED)
    order_kitting.pack(side=tk.BOTTOM, pady=20)
    add_k_products = tk.Button(kitting_wind, text="Add Product", command=get_k_products)
    add_k_products.pack(side=tk.BOTTOM, pady=20)
    update_with_arg = partial(update_dest, get_k_dest, k_agv, k_destination)
    update_ship = partial(update_kitting_ship, second_tray, second_agv, ship_count, second_dest, kitting_wind)
    kitActButtonFunc = partial(activateButton, order_kitting, kitProdsFlag)
    kitProdsFlag.trace('w', kitActButtonFunc)
    k_agv.trace('w', update_with_arg)
    ship_count.trace('w', update_ship)
    kittingFlag.set('1')
    kitting_wind.mainloop()
    tempKits.append(Kitting(ship_count.get(), trays.get(), second_tray.get(), k_agv.get(),
                            second_agv.get(), k_destination.get(), second_dest.get(), kitProds))


def get_k_products():  # adds a product to kitting
    """Adds products to a kitting order. Returned through kitProds"""
    k_products = tk.Toplevel()
    x_val_k = tk.StringVar()
    x_val_k.set('0')
    y_val_k = tk.StringVar()
    y_val_k.set('0')
    z_val_k = tk.StringVar()
    z_val_k.set('0')
    r_val_k = tk.StringVar()
    r_val_k.set('0')
    p_val_k = tk.StringVar()
    p_val_k.set('0')
    y_rpy_val_k = tk.StringVar()
    y_rpy_val_k.set('0')
    k_product_info = tk.StringVar()
    k_product_info.set(prodList[0])
    k_product_type_menu = tk.OptionMenu(k_products, k_product_info, *prodList)
    k_product_type_menu.pack()
    x_val_k_label = tk.Label(k_products, text="Enter the x value")
    x_val_k_label.pack()
    x_val_k_entry = tk.Entry(k_products, textvariable=x_val_k)
    x_val_k_entry.pack()
    y_val_k_label = tk.Label(k_products, text="Enter the y value")
    y_val_k_label.pack()
    y_val_k_entry = tk.Entry(k_products, textvariable=y_val_k)
    y_val_k_entry.pack()
    z_val_k_label = tk.Label(k_products, text="Enter the z value")
    z_val_k_label.pack()
    z_val_k_entry = tk.Entry(k_products, textvariable=z_val_k)
    z_val_k_entry.pack()
    r_val_k_label = tk.Label(k_products, text="Enter the r value")
    r_val_k_label.pack()
    r_val_k_entry = tk.Entry(k_products, textvariable=r_val_k)
    r_val_k_entry.pack()
    p_val_k_label = tk.Label(k_products, text="Enter the p value")
    p_val_k_label.pack()
    p_val_k_entry = tk.Entry(k_products, textvariable=p_val_k)
    p_val_k_entry.pack()
    y_rpy_val_k_label = tk.Label(k_products, text="Enter the y (rpy) value")
    y_rpy_val_k_label.pack()
    y_rpy_val_k_entry = tk.Entry(k_products, textvariable=y_rpy_val_k)
    y_rpy_val_k_entry.pack()
    exitFunc = partial(exitAndFlag, k_products, kitProdsFlag)
    kitting_prod_exit = tk.Button(k_products, text="Save and Exit", command=exitFunc)
    kitting_prod_exit.pack(pady=20)
    k_products.mainloop()
    kitProds.append(Products(k_product_info.get(),
                             str("["+x_val_k.get()+", "+y_val_k.get()+', '+z_val_k.get()+"]"),
                             str("["+r_val_k.get()+", "+p_val_k.get()+", "+y_rpy_val_k.get()+"]")))


def assembly():  # adds assembly to an order
    """Adds an assembly order. Returned through tempAssemb"""
    assemb_wind = tk.Toplevel()
    a_ship_count = tk.StringVar()
    a_ship_count.set('1')
    a_ship_count_label = tk.Label(assemb_wind, text="Enter the shipment count")
    a_ship_count_label.pack()
    a_ship_count_entry = tk.Entry(assemb_wind, textvariable=a_ship_count)
    a_ship_count_entry.pack()
    a_stations = tk.StringVar()
    a_stations.set('1')
    a_stations_label = tk.Label(assemb_wind, text="Enter the assembly stations")
    a_stations_label.pack()
    a_stations_entry = tk.Entry(assemb_wind, textvariable=a_stations)
    a_stations_entry.pack()
    add_a_products = tk.Button(assemb_wind, text="Add Product", command=get_a_products)
    add_a_products.pack(pady=20)
    exitAssemb = partial(exitAndFlag, assemb_wind, orderFlag)
    order_assemb = tk.Button(assemb_wind, text="Save and Exit", command=exitAssemb, state=tk.DISABLED)
    order_assemb.pack(pady=20)
    assembActButtonFunc = partial(activateButton, order_assemb, assembProdsFlag)
    assembProdsFlag.trace('w', assembActButtonFunc)
    assembFlag.set('1')
    assemb_wind.mainloop()
    tempAssemb.append(Assembly(a_ship_count.get(), a_stations.get(), assembProds))


def get_a_products():  # adds a product to assembly
    """Adds a product to an assembly order. Returned through assembProds"""
    a_products = tk.Toplevel()
    x_val_a = tk.StringVar()
    x_val_a.set('0')
    y_val_a = tk.StringVar()
    y_val_a.set('0')
    z_val_a = tk.StringVar()
    z_val_a.set('0')
    r_val_a = tk.StringVar()
    r_val_a.set('0')
    p_val_a = tk.StringVar()
    p_val_a.set('0')
    y_rpy_val_a = tk.StringVar()
    y_rpy_val_a.set('0')
    a_product_info = tk.StringVar()
    a_product_info.set(prodList[0])
    a_product_type_menu = tk.OptionMenu(a_products, a_product_info, *prodList)
    a_product_type_menu.pack()
    x_val_a_label = tk.Label(a_products, text="Enter the x value")
    x_val_a_label.pack()
    x_val_a_entry = tk.Entry(a_products, textvariable=x_val_a)
    x_val_a_entry.pack()
    y_val_a_label = tk.Label(a_products, text="Enter the y value")
    y_val_a_label.pack()
    y_val_a_entry = tk.Entry(a_products, textvariable=y_val_a)
    y_val_a_entry.pack()
    z_val_a_label = tk.Label(a_products, text="Enter the z value")
    z_val_a_label.pack()
    z_val_a_entry = tk.Entry(a_products, textvariable=z_val_a)
    z_val_a_entry.pack()
    r_val_a_label = tk.Label(a_products, text="Enter the r value")
    r_val_a_label.pack()
    r_val_a_entry = tk.Entry(a_products, textvariable=r_val_a)
    r_val_a_entry.pack()
    p_val_a_label = tk.Label(a_products, text="Enter the p value")
    p_val_a_label.pack()
    p_val_a_entry = tk.Entry(a_products, textvariable=p_val_a)
    p_val_a_entry.pack()
    y_rpy_val_a_label = tk.Label(a_products, text="Enter the y (rpy) value")
    y_rpy_val_a_label.pack()
    y_rpy_val_a_entry = tk.Entry(a_products, textvariable=y_rpy_val_a)
    y_rpy_val_a_entry.pack()
    exitAssembProd = partial(exitAndFlag, a_products, assembProdsFlag)
    assemb_prod_exit = tk.Button(a_products, text="Save and Exit", command=exitAssembProd)
    assemb_prod_exit.pack(pady=20)
    a_products.mainloop()
    assembProds.append(Products(a_product_info.get(),
                       str("[" + x_val_a.get() + ", " + y_val_a.get() + ', ' + z_val_a.get() + "]"),
                       str("[" + r_val_a.get() + ", " + p_val_a.get() + ", " + z_val_a.get() + "]")))


def add_bin():  # adds a bin for models over bins
    """Adds a bin in the models over bins section. Returned through modelsOverBinsInfo and binProds"""
    add_bin_wind = tk.Toplevel()
    cancel_bin_flag = tk.StringVar()
    cancel_bin_flag.set('0')
    bin_prod = tk.StringVar()
    bin_prod.set(prodList[0])
    bin_num = tk.StringVar()
    bin_num.set('bin1')
    dim = tk.StringVar()
    dim.set('2x2')
    x_val_s = tk.StringVar()
    x_val_s.set('0')
    y_val_s = tk.StringVar()
    y_val_s.set('0')
    z_val_s = tk.StringVar()
    z_val_s.set('0')
    x_val_e = tk.StringVar()
    x_val_e.set('0')
    y_val_e = tk.StringVar()
    y_val_e.set('0')
    z_val_e = tk.StringVar()
    z_val_e.set('0')
    r_val_b = tk.StringVar()
    r_val_b.set('0')
    p_val_b = tk.StringVar()
    p_val_b.set('0')
    y_rpy_val_b = tk.StringVar()
    y_rpy_val_b.set('0')
    b_num_label = tk.Label(add_bin_wind, text="Select the bin number")
    b_num_label.pack()
    b_num_menu = tk.OptionMenu(add_bin_wind, bin_num, 'bin1', 'bin2', 'bin3', 'bin4')
    b_num_menu.pack()
    b_product_label = tk.Label(add_bin_wind, text="Select the product for the bin")
    b_product_label.pack()
    b_product_type_menu = tk.OptionMenu(add_bin_wind, bin_prod, *prodList)
    b_product_type_menu.pack()
    x_val_s_label = tk.Label(add_bin_wind, text="Enter the start x value")
    x_val_s_label.pack()
    x_val_s_entry = tk.Entry(add_bin_wind, textvariable=x_val_s)
    x_val_s_entry.pack()
    y_val_s_label = tk.Label(add_bin_wind, text="Enter the start y value")
    y_val_s_label.pack()
    y_val_s_entry = tk.Entry(add_bin_wind, textvariable=y_val_s)
    y_val_s_entry.pack()
    z_val_s_label = tk.Label(add_bin_wind, text="Enter the start z value")
    z_val_s_label.pack()
    z_val_s_entry = tk.Entry(add_bin_wind, textvariable=z_val_s)
    z_val_s_entry.pack()
    x_val_e_label = tk.Label(add_bin_wind, text="Enter the end x value")
    x_val_e_label.pack()
    x_val_e_entry = tk.Entry(add_bin_wind, textvariable=x_val_e)
    x_val_e_entry.pack()
    y_val_e_label = tk.Label(add_bin_wind, text="Enter the end y value")
    y_val_e_label.pack()
    y_val_e_entry = tk.Entry(add_bin_wind, textvariable=y_val_e)
    y_val_e_entry.pack()
    z_val_e_label = tk.Label(add_bin_wind, text="Enter the end z value")
    z_val_e_label.pack()
    z_val_e_entry = tk.Entry(add_bin_wind, textvariable=z_val_e)
    z_val_e_entry.pack()
    r_val_b_label = tk.Label(add_bin_wind, text="Enter the r value")
    r_val_b_label.pack()
    r_val_b_entry = tk.Entry(add_bin_wind, textvariable=r_val_b)
    r_val_b_entry.pack()
    p_val_b_label = tk.Label(add_bin_wind, text="Enter the p value")
    p_val_b_label.pack()
    p_val_b_entry = tk.Entry(add_bin_wind, textvariable=p_val_b)
    p_val_b_entry.pack()
    y_rpy_val_b_label = tk.Label(add_bin_wind, text="Enter the y (rpy) value")
    y_rpy_val_b_label.pack()
    y_rpy_val_b_entry = tk.Entry(add_bin_wind, textvariable=y_rpy_val_b)
    y_rpy_val_b_entry.pack()
    b_dim_label = tk.Label(add_bin_wind, text="Select the dimensions for the bin")
    b_dim_label.pack()
    b_dim_menu = tk.OptionMenu(add_bin_wind, dim, '2x2', '3x3')
    b_dim_menu.pack()
    cancel_bin_func = partial(cancel_func, add_bin_wind, cancel_bin_flag)
    cancel_bin_button = tk.Button(add_bin_wind, text="Cancel", command=cancel_bin_func)
    cancel_bin_button.pack()
    add_bin_exit = tk.Button(add_bin_wind, text="Save and Exit", command=add_bin_wind.destroy)
    add_bin_exit.pack(pady=20)
    add_bin_wind.mainloop()
    width = '2'
    if dim.get() == '3x3':
        width = '3'
    if cancel_bin_flag.get() == "0":
        modelsOverBinsInfo.append(ModelOverBin(bin_num.get(), bin_prod.get(),
                                            str("["+x_val_s.get()+", "+y_val_s.get()+", "+z_val_s.get()+"]"),
                                            str("["+x_val_e.get()+", "+y_val_e.get()+", "+z_val_e.get()+"]"),
                                            str("["+r_val_b.get()+", "+p_val_b.get()+", "+y_rpy_val_b.get()+"]"),
                                            width, width))
        binProds.append(PresentProducts(bin_prod.get(), str(int(width)**2)))


def add_station():  # adds a station to models over stations
    """Adds a station to models over stations returns through models over stations info"""
    add_station_wind = tk.Toplevel()
    cancel_station_flag = tk.StringVar()
    cancel_station_flag.set("0")
    x_val_stat = tk.StringVar()
    x_val_stat.set('0')
    y_val_stat = tk.StringVar()
    y_val_stat.set('0')
    z_val_stat = tk.StringVar()
    z_val_stat.set('0')
    r_val_stat = tk.StringVar()
    r_val_stat.set('0')
    p_val_stat = tk.StringVar()
    p_val_stat.set('0')
    y_rpy_val_stat = tk.StringVar()
    y_rpy_val_stat.set('0')
    station = tk.StringVar()
    station.set(allStations[0])
    stat_prod = tk.StringVar()
    stat_prod.set(prodList[0])
    station_label = tk.Label(add_station_wind, text="Select the station")
    station_label.pack()
    station_menu = tk.OptionMenu(add_station_wind, station, *allStations)
    station_menu.pack()
    station_product_label = tk.Label(add_station_wind, text="Select the product for the station")
    station_product_label.pack()
    station_product_type_menu = tk.OptionMenu(add_station_wind, stat_prod, *prodList)
    station_product_type_menu.pack()
    x_val_stat_label = tk.Label(add_station_wind, text="Enter the x value")
    x_val_stat_label.pack()
    x_val_stat_entry = tk.Entry(add_station_wind, textvariable=x_val_stat)
    x_val_stat_entry.pack()
    y_val_stat_label = tk.Label(add_station_wind, text="Enter the y value")
    y_val_stat_label.pack()
    y_val_stat_entry = tk.Entry(add_station_wind, textvariable=y_val_stat)
    y_val_stat_entry.pack()
    z_val_stat_label = tk.Label(add_station_wind, text="Enter the z value")
    z_val_stat_label.pack()
    z_val_stat_entry = tk.Entry(add_station_wind, textvariable=z_val_stat)
    z_val_stat_entry.pack()
    r_val_stat_label = tk.Label(add_station_wind, text="Enter the r value")
    r_val_stat_label.pack()
    r_val_stat_entry = tk.Entry(add_station_wind, textvariable=r_val_stat)
    r_val_stat_entry.pack()
    p_val_stat_label = tk.Label(add_station_wind, text="Enter the p value")
    p_val_stat_label.pack()
    p_val_stat_entry = tk.Entry(add_station_wind, textvariable=p_val_stat)
    p_val_stat_entry.pack()
    y_rpy_val_stat_label = tk.Label(add_station_wind, text="Enter the y (rpy) value")
    y_rpy_val_stat_label.pack()
    y_rpy_val_stat_entry = tk.Entry(add_station_wind, textvariable=y_rpy_val_stat)
    y_rpy_val_stat_entry.pack()
    cancel_station_func = partial(cancel_func, add_station_wind, cancel_station_flag)
    cancel_stat_button = tk.Button(add_station_wind, text="Cancel", command=cancel_station_func)
    cancel_stat_button.pack()
    add_stat_exit = tk.Button(add_station_wind, text="Save and Exit", command=add_station_wind.destroy)
    add_stat_exit.pack(pady=20)
    add_station_wind.mainloop()
    if cancel_station_flag.get()=="0":
        modelsOverStationsInfo.append(ModelOverStation(station.get(), stat_prod.get(),
                                                    str("["+x_val_stat.get()+", "+y_val_stat.get() +
                                                        ", "+z_val_stat.get()+"]"),
                                                    str("["+r_val_stat.get()+", "+p_val_stat.get() +
                                                        ", "+y_rpy_val_stat.get()+"]")))


def add_belt():  # adds a belt to belt models
    """Adds a belt to belt models. Uses beltCycleInfo to return"""
    add_belt_wind = tk.Toplevel()
    cancel_belt_flag = tk.StringVar()
    cancel_belt_flag.set('0')
    belt_prod = tk.StringVar()
    belt_prod.set(prodList[0])
    belt_time = tk.StringVar()
    belt_time.set('1.0')
    x_val_belt = tk.StringVar()
    x_val_belt.set('0')
    y_val_belt = tk.StringVar()
    y_val_belt.set('0')
    z_val_belt = tk.StringVar()
    z_val_belt.set('0')
    r_val_belt = tk.StringVar()
    r_val_belt.set('0')
    p_val_belt = tk.StringVar()
    p_val_belt.set('0')
    y_rpy_val_belt = tk.StringVar()
    y_rpy_val_belt.set('0')
    belt_product_label = tk.Label(add_belt_wind, text="Select the product for the belt")
    belt_product_label.pack()
    belt_product_type_menu = tk.OptionMenu(add_belt_wind, belt_prod, *prodList)
    belt_product_type_menu.pack()
    belt_time_label = tk.Label(add_belt_wind, text="Enter the wait time for the part")
    belt_time_label.pack()
    belt_time_entry = tk.Entry(add_belt_wind, textvariable=belt_time)
    belt_time_entry.pack()
    x_val_belt_label = tk.Label(add_belt_wind, text="Enter the x value")
    x_val_belt_label.pack()
    x_val_belt_entry = tk.Entry(add_belt_wind, textvariable=x_val_belt)
    x_val_belt_entry.pack()
    y_val_belt_label = tk.Label(add_belt_wind, text="Enter the y value")
    y_val_belt_label.pack()
    y_val_belt_entry = tk.Entry(add_belt_wind, textvariable=y_val_belt)
    y_val_belt_entry.pack()
    z_val_belt_label = tk.Label(add_belt_wind, text="Enter the z value")
    z_val_belt_label.pack()
    z_val_belt_entry = tk.Entry(add_belt_wind, textvariable=z_val_belt)
    z_val_belt_entry.pack()
    r_val_belt_label = tk.Label(add_belt_wind, text="Enter the r value")
    r_val_belt_label.pack()
    r_val_belt_entry = tk.Entry(add_belt_wind, textvariable=r_val_belt)
    r_val_belt_entry.pack()
    p_val_belt_label = tk.Label(add_belt_wind, text="Enter the p value")
    p_val_belt_label.pack()
    p_val_belt_entry = tk.Entry(add_belt_wind, textvariable=p_val_belt)
    p_val_belt_entry.pack()
    y_rpy_val_belt_label = tk.Label(add_belt_wind, text="Enter the y (rpy) value")
    y_rpy_val_belt_label.pack()
    y_rpy_val_belt_entry = tk.Entry(add_belt_wind, textvariable=y_rpy_val_belt)
    y_rpy_val_belt_entry.pack()
    cancel_belt_func = partial(cancel_func, add_belt_wind, cancel_belt_flag)
    belt_cancel_button = tk.Button(add_belt_wind, text="Cancel", command=cancel_belt_func)
    belt_cancel_button.pack()
    belt_save = tk.Button(add_belt_wind, text="Save and Exit", command=add_belt_wind.destroy)
    belt_save.pack(pady=20)
    add_belt_wind.mainloop()
    if cancel_belt_flag.get()=="0":
        beltCycleInfo.append(BeltCycle(belt_prod.get(), belt_time.get(),
                                   str("["+x_val_belt.get()+", "+y_val_belt.get()+", "+z_val_belt.get()+"]"),
                                   str("["+r_val_belt.get()+", "+p_val_belt.get()+", "+y_rpy_val_belt.get()+"]")))


def add_faulty_prod():  # adds a faulty product for the faulty product challenge
    """Adds a faulty product for the faulty product challenge. Returned through faultyProdList"""
    faulty_prod_window = tk.Toplevel()
    cancel_faulty_flag = tk.StringVar()
    cancel_faulty_flag.set('0')
    temp_prod = tk.StringVar()
    prod_id = tk.StringVar()
    prod_id.set('1')
    available_prod_list = []
    id_range = []
    binProds.reverse()
    for product in binProds:
        available_prod_list.append(product.pType)
    temp_prod.set(available_prod_list[0])
    faulty_prod_menu = tk.OptionMenu(faulty_prod_window, temp_prod, *available_prod_list)
    faulty_prod_menu.pack()
    prod_id_label = tk.Label(faulty_prod_window, text="Enter the product id")
    prod_id_label.pack()
    for num in range(int(binProds[0].pNum)):
        id_range.append(num+1)
    prod_id_menu = tk.OptionMenu(faulty_prod_window, prod_id, *id_range)
    prod_id_menu.pack()
    cancel_faulty_func = partial(cancel_func, faulty_prod_window, cancel_faulty_flag)
    cancel_faulty_button = tk.Button(faulty_prod_window, text = "Cancel", command = cancel_faulty_func)
    cancel_faulty_button.pack()
    faulty_prod_save = tk.Button(faulty_prod_window, text="Save and Exit", command=faulty_prod_window.destroy)
    faulty_prod_save.pack(pady=20)
    update_id_with_arg = partial(update_id_range, prod_id_menu, temp_prod, prod_id)
    temp_prod.trace('w', update_id_with_arg)
    faulty_prod_window.mainloop()
    if cancel_faulty_flag.get()=="0":
        faultyProdList.append(str(temp_prod.get()+"_"+prod_id.get()))


def add_drop_region():  # adds a drop region for the faulty gripper challenge
    """Adds a drop region for the faulty gripper challenge. Returned through dropsInfo"""
    add_drop_wind = tk.Toplevel()
    drop_cancel_flag = tk.StringVar()
    drop_cancel_flag.set("0")
    temp_frame = tk.StringVar()
    temp_frame.set('')
    x_val_min = tk.StringVar()
    x_val_min.set('0')
    y_val_min = tk.StringVar()
    y_val_min.set('0')
    z_val_min = tk.StringVar()
    z_val_min.set('0')
    x_val_max = tk.StringVar()
    x_val_max.set('0')
    y_val_max = tk.StringVar()
    y_val_max.set('0')
    z_val_max = tk.StringVar()
    z_val_max.set('0')
    x_val_dest = tk.StringVar()
    x_val_dest.set('0')
    y_val_dest = tk.StringVar()
    y_val_dest.set('0')
    z_val_dest = tk.StringVar()
    z_val_dest.set('0')
    r_val_dest = tk.StringVar()
    r_val_dest.set('0')
    p_val_dest = tk.StringVar()
    p_val_dest.set('0')
    y_rpy_val_dest = tk.StringVar()
    y_rpy_val_dest.set('0')
    drop_prod = tk.StringVar()
    drop_prod.set(prodList[0])
    robot_type = tk.StringVar()
    robot_type.set('kitting')
    drop_frame_label = tk.Label(add_drop_wind, text="Enter the frame")
    drop_frame_label.pack()
    drop_frame_entry = tk.Entry(add_drop_wind, textvariable=temp_frame)
    drop_frame_entry.pack()
    x_val_min_label = tk.Label(add_drop_wind, text="Enter the min x value")
    x_val_min_label.pack()
    x_val_min_entry = tk.Entry(add_drop_wind, textvariable=x_val_min)
    x_val_min_entry.pack()
    y_val_min_label = tk.Label(add_drop_wind, text="Enter the min y value")
    y_val_min_label.pack()
    y_val_min_entry = tk.Entry(add_drop_wind, textvariable=y_val_min)
    y_val_min_entry.pack()
    z_val_min_label = tk.Label(add_drop_wind, text="Enter the min z value")
    z_val_min_label.pack()
    z_val_min_entry = tk.Entry(add_drop_wind, textvariable=z_val_min)
    z_val_min_entry.pack()
    x_val_max_label = tk.Label(add_drop_wind, text="Enter the max x value")
    x_val_max_label.pack()
    x_val_max_entry = tk.Entry(add_drop_wind, textvariable=x_val_max)
    x_val_max_entry.pack()
    y_val_max_label = tk.Label(add_drop_wind, text="Enter the max y value")
    y_val_max_label.pack()
    y_val_max_entry = tk.Entry(add_drop_wind, textvariable=y_val_max)
    y_val_max_entry.pack()
    z_val_max_label = tk.Label(add_drop_wind, text="Enter the max z value")
    z_val_max_label.pack()
    z_val_max_entry = tk.Entry(add_drop_wind, textvariable=z_val_max)
    z_val_max_entry.pack()
    x_val_dest_label = tk.Label(add_drop_wind, text="Enter the destination x value")
    x_val_dest_label.pack()
    x_val_dest_entry = tk.Entry(add_drop_wind, textvariable=x_val_dest)
    x_val_dest_entry.pack()
    y_val_dest_label = tk.Label(add_drop_wind, text="Enter the destination y value")
    y_val_dest_label.pack()
    y_val_dest_entry = tk.Entry(add_drop_wind, textvariable=y_val_dest)
    y_val_dest_entry.pack()
    z_val_dest_label = tk.Label(add_drop_wind, text="Enter the destination z value")
    z_val_dest_label.pack()
    z_val_dest_entry = tk.Entry(add_drop_wind, textvariable=z_val_dest)
    z_val_dest_entry.pack()
    r_val_dest_label = tk.Label(add_drop_wind, text="Enter the r value for the destination")
    r_val_dest_label.pack()
    r_val_dest_entry = tk.Entry(add_drop_wind, textvariable=r_val_dest)
    r_val_dest_entry.pack()
    p_val_dest_label = tk.Label(add_drop_wind, text="Enter the p value for the destination")
    p_val_dest_label.pack()
    p_val_dest_entry = tk.Entry(add_drop_wind, textvariable=p_val_dest)
    p_val_dest_entry.pack()
    y_rpy_val_dest_label = tk.Label(add_drop_wind, text="Enter the y (rpy) value for the destination")
    y_rpy_val_dest_label.pack()
    y_rpy_val_dest_entry = tk.Entry(add_drop_wind, textvariable=y_rpy_val_dest)
    y_rpy_val_dest_entry.pack()
    drop_prod_label = tk.Label(add_drop_wind, text="Select the product type to drop")
    drop_prod_label.pack()
    drop_prod_menu = tk.OptionMenu(add_drop_wind, drop_prod, *prodList)
    drop_prod_menu.pack()
    drop_robot_type_label = tk.Label(add_drop_wind, text="Select the robot type for the drop")
    drop_robot_type_label.pack()
    drop_robot_type_menu = tk.OptionMenu(add_drop_wind, robot_type, "kitting", "gantry")
    drop_robot_type_menu.pack()
    cancel_drop_func = partial(cancel_func, add_drop_wind, drop_cancel_flag)
    cancel_drop_button = tk.Button(add_drop_wind, text="Cancel", command=cancel_drop_func)
    cancel_drop_button.pack()
    add_drop_save = tk.Button(add_drop_wind, text="Save and Exit", command=add_drop_wind.destroy)
    add_drop_save.pack()
    add_drop_wind.mainloop()
    if drop_cancel_flag.get()=="0":
        dropsInfo.append(Drops(temp_frame.get(), str("["+x_val_min.get()+", "+y_val_min.get()+", "+z_val_min.get()+"]"),
                            str("["+x_val_max.get()+", "+y_val_max.get()+", "+z_val_max.get()+"]"),
                            str("["+x_val_dest.get()+", "+y_val_dest.get()+", "+z_val_dest.get()+"]"),
                            str("["+r_val_dest.get()+", "+p_val_dest.get()+", "+y_rpy_val_dest.get()+"]"),
                            drop_prod.get(), robot_type.get()))


def cancel_wind(window):  # cancels at any point in the program
    """Used to chancel a window"""
    cancelFlag.set('1')
    window.destroy()


def check_cancel(cancel_flag):  # deletes the file if the user cancels from inside the program
    """Checks if the program is canceled. If it is, the program removes the file and quits. If directories have been created,
    those are removed as well"""
    if cancel_flag == '1':
        for dir in pathIncrement:
            chdir(dir)
        if path.exists(fileName.get()):
            os.remove(fileName.get())
        elif path.exists(fileName.get() + '.yaml'):
            os.remove(fileName.get() + '.yaml')
        chdir('../')
        createdDir.reverse()
        for dir in createdDir:
            if len(os.listdir(dir))!=0:
                break
            os.rmdir(dir)
            chdir('../')
        quit()


class Order:  # for organizing the data from the order menu
    """Holds the information for an order"""
    def __init__(self, priority, k_health, a_health, an_cond, cond_val, kit_info, assem_info):
        self.priority = priority
        self.kittingHealth = k_health
        self.assemblyHealth = a_health
        self.announcementCondition = an_cond
        self.conditionValue = cond_val
        self.kitting = kit_info
        self.assembly = assem_info


class Kitting:  # for organizing the data from the kitting menu
    """Holds the information for a kitting order"""
    def __init__(self, ship_count, tray, second_tray, agv, second_agv, destinations, second_dest, products):
        self.shipmentCount = ship_count
        self.tray = tray
        self.secondTray = second_tray
        self.agv = agv
        self.secondAgv = second_agv
        self.destinations = destinations
        self.secondDest = second_dest
        self.products = products


class Assembly:  # for organizing the data from the assembly menu
    """Holds the information for an assembly order"""
    def __init__(self, ship_count, stations, products):
        self.shipmentCount = ship_count
        self.stations = stations
        self.products = products


class Products:  # for organizing the data for all products
    """Holds the information for a product"""
    def __init__(self, p_type, xyz, rpy):
        self.pType = p_type
        self.xyz = xyz
        self.rpy = rpy


class ModelOverBin:  # for organizing the data from the models over bins menu
    """Holds the information for a bin for models over bins"""
    def __init__(self, bin_num, prod_temp, start, end, rpy, num_mod_x, num_mod_y):
        self.binNum = bin_num
        self.product = prod_temp
        self.xyz_start = start
        self.xyz_end = end
        self.rpy = rpy
        self.num_mod_x = num_mod_x
        self.num_mod_y = num_mod_y


class ModelOverStation:  # for organizing the data from the models over stations menu
    """Holds the information for a station for the models over stations"""
    def __init__(self, station, part, xyz, rpy):
        self.station = station
        self.part = part
        self.xyz = xyz
        self.rpy = rpy


class BeltCycle:  # for organizing the data from the belt models menu
    """Holds the information for a belt cycle"""
    def __init__(self, part, time, xyz, rpy):
        self.part = part
        self.time = time
        self.xyz = xyz
        self.rpy = rpy


class Drops:  # for organizing the data from the drops menu
    """Holds the information for a drop region"""
    def __init__(self, drops_frame, min_xyz, max_xyz, dest_xyz, dest_rpy, type_to_drop, robot_type):
        self.frame = drops_frame
        self.minXyz = min_xyz
        self.maxXyz = max_xyz
        self.destXyz = dest_xyz
        self.destRpy = dest_rpy
        self.typeToDrop = type_to_drop
        self.robotType = robot_type


class PresentProducts:  # holds the products which from bins
    """Holds the products which are present in the program"""
    def __init__(self, product_type, num):
        self.pType = product_type
        self.pNum = num


if __name__ == "__main__":
    """Main part of program. Goes through the main windows of the program and holds all global tkinter stringvars"""
    getFileName = tk.Tk()
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
    getFileName.geometry("500x600")
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
    fileNameLabel = tk.Label(getFileName, text="Enter the file name you would like to save as:")
    fileNameLabel.pack()
    fileNameTextBox = tk.Entry(getFileName, textvariable=fileName)
    fileNameTextBox.pack()
    cancel_file = partial(cancel_wind, getFileName)
    cancelFile = tk.Button(getFileName, text="Cancel and Exit", command=cancel_file)
    cancelFile.pack(side=tk.BOTTOM, pady=20)
    fileExit = tk.Button(getFileName, text="Next", command=get_file_name_next)
    fileExit.pack(side=tk.BOTTOM, pady=20)
    fileName.trace('w', fileNameCorrectFunc)
    getFileName.mainloop()
    if platform.system()=="Linux":
        fileName.set("~/ariac_ws/src/ARIAC/nist_gear/config/my_files/"+fileName.get())
    if cancelFlag.get() == '1':
        quit()
    # END OF GETTING THE NAME OF THE FILE
    # ----------------------------------------------------------------------------------------------
    # BEGINNING OF OPTIONS
    options = tk.Tk()
    options.title("Options")
    options.geometry("500x600")
    overBins = tk.StringVar()
    overBins.set("true")
    overBinsLabel = tk.Label(options, text="Insert models over bins:")
    overBinsLabel.pack()
    tfOverBins = tk.Button(text="True", width=12, command=tf)
    tfOverBins.pack(pady=5)
    beltCycles = tk.StringVar()
    beltCycles.set("0")
    popCycleLabel = tk.Label(options, text="Enter the belt population cycles (enter skip to skip):")
    popCycleLabel.pack()
    popCycleBox = tk.Entry(options, textvariable=beltCycles)
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
    cancel_options = partial(cancel_wind, options)
    cancelOptions = tk.Button(options, text="Cancel and Exit", command=cancel_options)
    cancelOptions.pack(pady=20)
    options.mainloop()
    saveFileName = fileName.get()
    if '.yaml' not in saveFileName:
        saveFileName += '.yaml'
    if saveFileName[0]=="~" and platform.system()=="Linux":
        os.chdir(Path.home())
        saveFileName.replace("~","")
        saveFileName = saveFileName[2:]
        fileName.set(saveFileName)
    if saveFileName.count("/")>0:
        tempFileName = saveFileName.split("/")
        for dir in tempFileName[:-1]:
            pathIncrement.append(dir)
            if not path.exists(dir):
                os.mkdir(dir)
                os.chdir(dir)
                createdDir.append(dir)
        os.chdir(Path.home())
    with open(saveFileName, "a") as o:
        o.write("# yaml-language-server: $schema=yamlSchemaARIAC.json\n") 
        o.write("options:\n")
        if overBins.get() != 'skip':
            o.write(" insert_models_over_bins: " + overBins.get() + "\n")
        if beltCycles.get() != 'skip':
            o.write(" belt_population_cycles: " + beltCycles.get() + "\n")
        if overStations.get() != 'skip':
            o.write(" insert_models_over_stations: " + overStations.get() + "\n")
        if stateLogging.get() != 'skip':
            o.write(" gazebo_state_logging: " + stateLogging.get() + "\n")
        o.write(" # mandatory: gripper_tray or gripper_part\n")
        o.write(" current_gripper_type: " + gripperType.get() + "\n")
        o.write("time_limit: " + timeLimit.get() + "\n")
    check_cancel(cancelFlag.get())
    # END OF GETTING OPTIONS
    # ----------------------------------------------------------------------------------------------------------------------
    # BEGINNING OF TABLE_TRAY_INFOS
    trayInfo = tk.Tk()
    trayInfo.title("Tray Information")
    trayInfo.geometry("500x600")
    trayInstructions = tk.Label(trayInfo, text="If you would like to skip a tray, leave it blank, leave it blank")
    trayInstructions.pack()
    table1 = tk.StringVar()
    table1.set("")
    table1Label = tk.Label(trayInfo, text="Choose the material for table 1")
    table1Label.pack()
    table1Menu = tk.OptionMenu(trayInfo, table1, "", "movable_tray_dark_wood", "movable_tray_light_wood",
                               "movable_tray_metal_rusty", "movable_tray_metal_shiny")
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
    table2Menu = tk.OptionMenu(trayInfo, table2, "", "movable_tray_dark_wood", "movable_tray_light_wood",
                               "movable_tray_metal_rusty", "movable_tray_metal_shiny")
    table2Menu.pack()
    table2q = tk.StringVar()
    table2q.set("")
    table2qLabel = tk.Label(trayInfo, text="Choose the quantity for table 2")
    table2qLabel.pack()
    table2qMenu = tk.OptionMenu(trayInfo, table2q, "", "1", "2", "3")
    table2qMenu.pack()
    trayNext = tk.Button(trayInfo, text="Next", command=trayInfo.destroy)
    trayNext.pack(pady=20)
    traySkipFlag = tk.StringVar()
    traySkipFlag.set("0")
    tray_skip = partial(skip_wind, traySkipFlag, trayInfo)
    skipButton = tk.Button(trayInfo, text="Skip", command=tray_skip)
    skipButton.pack()
    cancel_tray = partial(cancel_wind, trayInfo)
    cancelTray = tk.Button(trayInfo, text="Cancel and Exit", command=cancel_tray)
    cancelTray.pack()
    trayInfo.mainloop()
    if traySkipFlag.get() == "0":
        with open(saveFileName, "a") as o:
            if (table1.get() != "" and table1q.get() != "") or (table2.get() != "" and table2q.get() != ""):
                o.write("\n\n\ntable_tray_infos:\n")
            if table1.get() != "" and table1q.get() != "":
                o.write(" table_1:\n")
                o.write("  tray_model: " + table1.get() + "\n")
                o.write("  quantity: " + table1q.get() + "\n")
            if table2.get() != "" and table2q.get() != "":
                o.write(" table_2:\n")
                o.write("  tray_model: " + table2.get() + "\n")
                o.write("  quantity: " + table2q.get() + "\n")
    check_cancel(cancelFlag.get())
    # END OF TABLE MENUS
    # -----------------------------------------------------------------------------------
    # BEGINNING OF GETTING AGV_INFOS
    agvInfo = tk.Tk()
    agvInfo.geometry("500x600")
    agvInfo.title("AGV Information")
    agv1 = tk.StringVar()
    agv1.set("ks1")
    agv1Label = tk.Label(agvInfo, text="AGV1 Location:")
    agv1Label.pack()
    agv1Menu = tk.OptionMenu(agvInfo, agv1, *agv1List)
    agv1Menu.pack()
    agv2 = tk.StringVar()
    agv2.set("ks2")
    agv2Label = tk.Label(agvInfo, text="AGV2 Location:")
    agv2Label.pack()
    agv2Menu = tk.OptionMenu(agvInfo, agv2, *agv2List)
    agv2Menu.pack()
    agv3 = tk.StringVar()
    agv3.set("ks3")
    agv3Label = tk.Label(agvInfo, text="AGV3 Location:")
    agv3Label.pack()
    agv3Menu = tk.OptionMenu(agvInfo, agv3, *agv3List)
    agv3Menu.pack()
    agv4 = tk.StringVar()
    agv4.set("ks4")
    agv4Label = tk.Label(agvInfo, text="AGV4 Location:")
    agv4Label.pack()
    agv4Menu = tk.OptionMenu(agvInfo, agv4, *agv4List)
    agv4Menu.pack()
    productButton = tk.Button(agvInfo, text="Add Product", command=add_product)
    productButton.pack(pady=20)
    agvNext = tk.Button(agvInfo, text="Next", command=agvInfo.destroy)
    agvNext.pack(pady=20)
    cancel_agv = partial(cancel_wind, agvInfo)
    cancelAgv = tk.Button(agvInfo, text="Cancel and Exit", command=cancel_agv)
    cancelAgv.pack(pady=20)
    agvInfo.mainloop()
    partID = 0
    with open(saveFileName, "a") as o:
        o.write("\n\nagv_infos:\n")
        o.write(" agv1:\n")
        o.write("  location: " + agv1.get() + "\n")
        if len(agv1Prods) > 0:
            agv1Prods.reverse()
            o.write("  products:\n")
            for i in agv1Prods:
                if i != '':
                    o.write("   part_" + str(partID) + ":\n")
                    o.write("    type: " + i.pType + "\n")
                    o.write("    pose: \n")
                    o.write("     xyz: " + i.xyz + "\n")
                    o.write("     rpy: " + i.rpy + "\n")
                    partID += 1
        o.write(" agv2:\n")
        o.write("  location: " + agv2.get() + "\n")
        if len(agv2Prods) > 0:
            agv2Prods.reverse()
            o.write("  products:\n")
            for i in agv2Prods:
                if i != '':
                    o.write("   part_" + str(partID) + ":\n")
                    o.write("    type: " + i.pType + "\n")
                    o.write("    pose: \n")
                    o.write("     xyz: " + i.xyz + "\n")
                    o.write("     rpy: " + i.rpy + "\n")
                    partID += 1
        o.write(" agv3:\n")
        o.write("  location: " + agv3.get() + "\n")
        if len(agv3Prods) > 0:
            agv3Prods.reverse()
            o.write("  products:\n")
            for i in agv3Prods:
                if i != '':
                    o.write("   part_" + str(partID) + ":\n")
                    o.write("    type: " + i.pType + "\n")
                    o.write("    pose: \n")
                    o.write("     xyz: " + i.xyz + "\n")
                    o.write("     rpy: " + i.rpy + "\n")
                    partID += 1
        o.write(" agv4:\n")
        o.write("  location: " + agv4.get() + "\n")
        if len(agv4Prods) > 0:
            o.write("  products:\n")
            for i in agv4Prods:
                if i != '':
                    o.write("   part_" + str(partID) + ":\n")
                    o.write("    type: " + i.pType + "\n")
                    o.write("    pose: \n")
                    o.write("     xyz: " + i.xyz + "\n")
                    o.write("     rpy: " + i.rpy + "\n")
                    partID += 1
    check_cancel(cancelFlag.get())
    # END OF AGV OPTIONS
    # ----------------------------------------------------------------------------------------------------------------------
    # BEGINNING OF ORDERS
    orderID = 0
    ordersInfo = tk.Tk()
    ordersInfo.geometry("500x600")
    allOrders = []
    ordersInfo.title("Orders Information")
    newOrder = tk.Button(ordersInfo, text="New Order", command=new_order)
    newOrder.pack(pady=20)
    ordersNext = tk.Button(ordersInfo, text="Next", command=ordersInfo.destroy, state=tk.DISABLED)
    ordersNext.pack(pady=20)
    enableOrdersNext = partial(activateButton, ordersNext, orderNextFlag)
    orderNextFlag.trace('w', enableOrdersNext)
    deactivateNewOrder = partial(deactivateButton, newOrder, secondOrderFlag)
    secondOrderFlag.trace('w', deactivateNewOrder)
    cancel_orders = partial(cancel_wind, ordersInfo)
    cancelOrders = tk.Button(ordersInfo, text="Cancel and Exit", command=cancel_orders)
    cancelOrders.pack(pady=20)
    ordersInfo.mainloop()
    allOrders.reverse()
    partC = 0
    check_cancel(cancelFlag.get())
    if len(allOrders)> 0:
        if len(allOrders[0].kitting)>0:
            allOrders[0].kitting[0].products.reverse()
            if len(allOrders[0].kitting[0].products) != firstLengths[0]:
                firstLengths[0] = len(allOrders[0].kitting[0].products) - firstLengths[0]
        else:
            firstLengths[0]=0
        if len(allOrders[0].assembly)>0:
            allOrders[0].assembly[0].products.reverse()
            if len(allOrders[0].assembly[0].products)!= firstLengths[1]:
                firstLengths[1] = len(allOrders[0].assembly[0].products) - firstLengths[1]
        else:
            firstLengths[1]=0
    with open(saveFileName, "a") as o:
        if len(allOrders) > 0:
            o.write("\n\norders:\n")
            for i in allOrders:
                firstKitProd = 0
                firstAssembProd = 0
                o.write(" order_"+str(orderID)+":\n")
                o.write("  priority: " + i.priority+"\n")
                o.write("  kitting_robot_health: " + i.kittingHealth+"\n")
                o.write("  assembly_robot_health: " + i.assemblyHealth+"\n")
                o.write("  announcement_condition: " + i.announcementCondition+"\n")
                o.write("  announcement_condition_value: "+i.conditionValue+"\n")
                if len(i.kitting) != 0:
                    o.write("  kitting:\n")
                    o.write("   shipment_count: " + i.kitting[orderInd].shipmentCount + "\n")
                    o.write("   trays: [" + i.kitting[orderInd].tray)
                    if i.kitting[orderInd].secondTray != '':
                        o.write(", "+i.kitting[orderInd].secondTray)
                    o.write("]\n")
                    o.write("   agvs: [" + i.kitting[orderInd].agv)
                    if i.kitting[orderInd].secondAgv != '':
                        o.write(", "+i.kitting[orderInd].secondAgv)
                    o.write("]\n")
                    o.write("   destinations: " + i.kitting[orderInd].destinations.replace("]", ''))
                    if i.kitting[orderInd].secondDest != '':
                        o.write(", "+i.kitting[orderInd].secondDest.replace("[", '')+"\n")
                    else:
                        o.write("]\n")
                    if orderID==0:
                        for k in i.kitting[orderInd].products[:firstLengths[0]]:
                            if firstKitProd == 0:
                                o.write("   products:\n")
                                firstKitProd = 1
                            o.write("    part_" + str(partC) + ":\n")
                            partC += 1
                            o.write("     type: " + k.pType + "\n")
                            o.write("     pose:\n")
                            o.write("      xyz: " + k.xyz + "\n")
                            o.write("      rpy: " + k.rpy + "\n")
                    else:
                        for k in i.kitting[orderInd].products[firstLengths[0]:]:
                            if firstKitProd == 0:
                                o.write("   products:\n")
                                firstKitProd = 1
                            o.write("    part_" + str(partC) + ":\n")
                            partC += 1
                            o.write("     type: " + k.pType + "\n")
                            o.write("     pose:\n")
                            o.write("      xyz: " + k.xyz + "\n")
                            o.write("      rpy: " + k.rpy + "\n")
                if len(i.assembly) != 0:
                    o.write("  assembly:\n")
                    o.write("   shipment_count: " + i.assembly[orderInd].shipmentCount + '\n')
                    o.write("   stations: " + i.assembly[orderInd].stations + '\n')
                    if orderID==0:
                        for k in i.assembly[orderInd].products[:firstLengths[1]]:
                            if firstAssembProd==0:
                                o.write("   products:\n")
                                firstAssembProd = 1
                            o.write("     part_" + str(partC) + ":\n")
                            partC += 1
                            o.write("      type: " + k.pType + "\n")
                            o.write("      pose:\n")
                            o.write("       xyz: " + k.xyz + "\n")
                            o.write("       rpy: " + k.rpy + "\n")
                    else:
                        for k in i.assembly[orderInd].products[firstLengths[1]:]:
                            if firstAssembProd==0:
                                o.write("   products:\n")
                                firstAssembProd = 1
                            o.write("     part_" + str(partC) + ":\n")
                            partC += 1
                            o.write("      type: " + k.pType + "\n")
                            o.write("      pose:\n")
                            o.write("       xyz: " + k.xyz + "\n")
                            o.write("       rpy: " + k.rpy + "\n")
                orderID += 1
            o.write("\n")
    # END OF ORDERS
    # ----------------------------------------------------------------------------------------------------------------------
    # BEGINNING OF MODELS OVER BINS
    if overBins.get() == 'true':
        overBinsWind = tk.Tk()
        overBinsWind.geometry("500x600")
        overBinsWind.title("Models Over Bins Menu")
        addBinButton = tk.Button(overBinsWind, text="Add bin", command=add_bin)
        addBinButton.pack(pady=20)
        overBinsNext = tk.Button(overBinsWind, text="Next", command=overBinsWind.destroy)
        overBinsNext.pack(pady=20)
        cancel_over_bins = partial(cancel_wind, overBinsWind)
        cancelOverBins = tk.Button(overBinsWind, text="Cancel and Exit", command=cancel_over_bins)
        cancelOverBins.pack(pady=20)
        overBinsWind.mainloop()
        check_cancel(cancelFlag.get())
        if len(modelsOverBinsInfo) > 0:
            modelsOverBinsInfo.reverse()
            with open(saveFileName, "a") as o:
                o.write("\nmodels_over_bins:\n")
                for i in modelsOverBinsInfo:
                    o.write(" "+i.binNum+":\n")
                    o.write("  models:\n")
                    o.write("   "+i.product+":\n")
                    o.write("    xyz_start: "+i.xyz_start+"\n")
                    o.write("    xyz_end: "+i.xyz_end+"\n")
                    o.write("    rpy: "+i.rpy+"\n")
                    o.write("    num_models_x: "+i.num_mod_x+"\n")
                    o.write("    num_models_y: "+i.num_mod_y+"\n")
                o.write("\n")
    # END OF MODELS OVER BINS
    # ----------------------------------------------------------------------------------------------------------------------
    # BEGINNING OF MODELS OVER STATIONS
    if overStations.get() == 'true':
        overStationsWind = tk.Tk()
        overStationsWind.geometry("500x600")
        overStationsWind.title("Models Over Stations Menu")
        addStationButton = tk.Button(overStationsWind, text="Add station", command=add_station)
        addStationButton.pack(pady=20)
        overStationsNext = tk.Button(overStationsWind, text="Next", command=overStationsWind.destroy)
        overStationsNext.pack(pady=20)
        cancel_over_stations = partial(cancel_wind, overStationsWind)
        cancelOverStations = tk.Button(overStationsWind, text="Cancel and Exit", command=cancel_over_stations)
        cancelOverStations.pack(pady=20)
        overStationsWind.mainloop()
        check_cancel(cancelFlag.get())
        if len(modelsOverStationsInfo) > 0:
            modelsOverStationsInfo.reverse()
            with open(saveFileName, "a") as o:
                o.write("\nmodels_over_stations:\n")
                for i in modelsOverStationsInfo:
                    o.write(" "+i.station+":\n")
                    o.write("  models:\n")
                    o.write("   "+i.part+":\n")
                    o.write("    xyz: "+i.xyz+"\n")
                    o.write("    rpy: "+i.rpy+"\n")
                o.write("\n")
    # END OF MODELS OVER STATIONS
    # ----------------------------------------------------------------------------------------------------------------------
    # BEGINNING OF BELT MODELS
    if beltCycles.get() != '0':
        beltCyclesWind = tk.Tk()
        beltCyclesWind.geometry("500x600")
        beltCyclesWind.title("Belt Cycles Menu")
        addBeltCycle = tk.Button(beltCyclesWind, text="Add belt cycle", command=add_belt)
        addBeltCycle.pack(pady=20)
        beltCycleNext = tk.Button(beltCyclesWind, text="Next", command=beltCyclesWind.destroy)
        beltCycleNext.pack(pady=20)
        cancel_belt_cycles = partial(cancel_wind, beltCyclesWind)
        cancelBeltCycle = tk.Button(beltCyclesWind, text="Cancel and Exit", command=cancel_belt_cycles)
        cancelBeltCycle.pack(pady=20)
        beltCyclesWind.mainloop()
        check_cancel(cancelFlag.get())
        if len(beltCycleInfo) > 0:
            beltCycleInfo.reverse()
            with open(saveFileName, "a") as o:
                o.write("\nbelt_models:\n")
                for i in beltCycleInfo:
                    o.write(" "+i.part+":\n")
                    o.write("  "+i.time+":\n")
                    o.write("   pose:\n")
                    o.write("    xyz: "+i.xyz+"\n")
                    o.write("    rpy: "+i.rpy+"\n")
                o.write("\n")
    # END OF BELT CYCLES
    # -----------------------------------------------------------------------------------
    # BEGINNING OF CHALLENGE SELECTION
    challengeWind = tk.Tk()
    challengeWind.geometry("500x600")
    challengeWind.title("Challenge Selection Window")
    faultyProdSelection = tk.StringVar()
    faultyProdSelection.set('0')
    dropSelection = tk.StringVar()
    dropSelection.set('0')
    sensorBlackoutSelection = tk.StringVar()
    sensorBlackoutSelection.set('0')
    mainChallengeLabel = tk.Label(challengeWind, text="Please select the challenges you would like to do")
    mainChallengeLabel.pack()
    if len(binProds)>0:
        faultyProductCheckbox = tk.Checkbutton(challengeWind, text='Faulty Product', variable=faultyProdSelection, onvalue='1', offvalue='0')
        faultyProductCheckbox.pack()
    faultyGripperCheckbox = tk.Checkbutton(challengeWind, text='Faulty Gripper', variable=dropSelection, onvalue='1', offvalue='0')
    faultyGripperCheckbox.pack()
    sensorBlackoutCheckbox = tk.Checkbutton(challengeWind, text='Sensor Blackout', variable=sensorBlackoutSelection, onvalue='1', offvalue='0')
    sensorBlackoutCheckbox.pack()
    challengeNext = tk.Button(challengeWind, text="Next", command=challengeWind.destroy)
    challengeNext.pack(pady=20)
    cancel_challenge_func = partial(cancel_wind, challengeWind)
    cancelChallenge = tk.Button(challengeWind, text="Cancel and Exit", command=cancel_challenge_func)
    cancelChallenge.pack(pady=20)
    challengeWind.mainloop()
    check_cancel(cancelFlag.get())
    # END OF CHALLENGE SELECTION
    # -----------------------------------------------------------------------------------
    # BEGINNING OF FAULTY PRODUCTS
    if len(binProds)>0 and faultyProdSelection.get()=='1':
        faultyWind = tk.Tk()
        faultyWind.geometry("500x600")
        faultyWind.title("Faulty Products Menu")
        faultySkipFlag = tk.StringVar()
        faultySkipFlag.set('0')
        faultyWindLabel = tk.Label(faultyWind, text="This is needed for the Faulty Product Challenge")
        faultyWindLabel.pack()
        addProd = tk.Button(faultyWind, text="Add Product", command=add_faulty_prod)
        addProd.pack(pady=20)
        faulty_skip = partial(skip_wind, faultySkipFlag, faultyWind)
        skipFaultyProd = tk.Button(faultyWind, text="Skip", command=faulty_skip)
        skipFaultyProd.pack(pady=20)
        faultyProdNext = tk.Button(faultyWind, text="Next", command=faultyWind.destroy)
        faultyProdNext.pack(pady=20)
        cancel_faulty_products = partial(cancel_wind, faultyWind)
        cancelFaultyProd = tk.Button(faultyWind, text="Cancel and Exit", command=cancel_faulty_products)
        cancelFaultyProd.pack(pady=20)
        faultyWind.mainloop()
        check_cancel(cancelFlag.get())
        if faultySkipFlag.get() == '0' and len(faultyProdList) > 0:
            faultyProdList.reverse()
            with open(saveFileName, 'a') as o:
                o.write("\nfaulty_products:\n")
                for prod in faultyProdList:
                    o.write(" - "+prod+"\n")
                o.write("\n")
    # END OF FAULTY PRODUCTS
    # --------------------------------------------------------------------------
    # BEGINNING OF DROPS
    if dropSelection.get()=='1':
        dropsWind = tk.Tk()
        dropsWind.title("Drops Menu")
        dropsWind.geometry("500x600")
        dropsSkipFlag = tk.StringVar()
        dropsSkipFlag.set('0')
        dropsWindLabel = tk.Label(dropsWind, text="This is needed for the Faulty Gripper Challenge")
        dropsWindLabel.pack()
        addDrop = tk.Button(dropsWind, text="Add New Drop Region", command=add_drop_region)
        addDrop.pack()
        drops_skip = partial(skip_wind, dropsSkipFlag, dropsWind)
        skipDrops = tk.Button(dropsWind, text="Skip", command=drops_skip)
        skipDrops.pack(pady=20)
        dropsNext = tk.Button(dropsWind, text="Next", command=dropsWind.destroy)
        dropsNext.pack(pady=20)
        cancel_drops = partial(cancel_wind, dropsWind)
        cancelDrops = tk.Button(dropsWind, text="Cancel and Exit", command=cancel_drops)
        cancelDrops.pack(pady=20)
        dropsWind.mainloop()
        check_cancel(cancelFlag.get())
        dropCount = 0
        if dropsSkipFlag.get() == '0' and len(dropsInfo) > 0:
            dropsInfo.reverse()
            with open(saveFileName, 'a') as o:
                o.write("\ndrops:\n drop_regions:\n")
                for drop in dropsInfo:
                    o.write("  shipping_box_"+str(dropCount)+"_impeding:\n")
                    dropCount += 1
                    o.write("   frame: "+drop.frame+"\n")
                    o.write("   min:\n")
                    o.write("    xyz: "+drop.minXyz+"\n")
                    o.write("   max:\n")
                    o.write("    xyz: "+drop.maxXyz+'\n')
                    o.write("   destination:\n")
                    o.write("    xyz: "+drop.destXyz+"\n")
                    o.write("    rpy: "+drop.destRpy+"\n")
                    o.write("   product_type_to_drop: "+drop.typeToDrop+"\n")
                    o.write("   robot_type: "+drop.robotType+"\n")
                o.write("\n")
    # END OF DROPS
    # --------------------------------------------------------------------------
    # BEGINNING OF SENSOR BLACKOUT
    if sensorBlackoutSelection.get()=='1':
        sensorBlackoutWind = tk.Tk()
        sensorBlackoutWind.title("Sensor Blackout")
        sensorBlackoutWind.geometry("500x600")
        prodCount = tk.StringVar()
        prodCount.set('0')
        duration = tk.StringVar()
        duration.set('0')
        sensor_blackout_skip_flag = tk.StringVar()
        sensor_blackout_skip_flag.set('0')
        prodCountLabel = tk.Label(sensorBlackoutWind, text="Enter the product count for the sensor blackout")
        prodCountLabel.pack()
        prodCountEntry = tk.Entry(sensorBlackoutWind, textvariable=prodCount)
        prodCountEntry.pack()
        durationLabel = tk.Label(sensorBlackoutWind, text="Enter the duration of the sensor blackout")
        durationLabel.pack()
        durationEntry = tk.Entry(sensorBlackoutWind, textvariable=duration)
        durationEntry.pack()
        sensor_blackout_skip = partial(skip_wind, sensor_blackout_skip_flag, sensorBlackoutWind)
        sensorBlackoutSkip = tk.Button(sensorBlackoutWind, text="Skip and Exit", command=sensor_blackout_skip)
        sensorBlackoutSkip.pack(pady=20)
        sensorBlackoutSE = tk.Button(sensorBlackoutWind, text="Save and Exit", command=sensorBlackoutWind.destroy)
        sensorBlackoutSE.pack(pady=20)
        cancel_sensor_blackout = partial(cancel_wind, sensorBlackoutWind)
        cancelSensorBlackout = tk.Button(sensorBlackoutWind, text="Cancel and Exit", command=cancel_sensor_blackout)
        cancelSensorBlackout.pack(pady=20)
        sensorBlackoutWind.mainloop()
        check_cancel(cancelFlag.get())
        if sensor_blackout_skip_flag.get() == '0':
            with open(saveFileName, 'a') as o:
                o.write("\nsensor_blackout:\n")
                o.write(" product_count: "+prodCount.get()+"\n")
                o.write(" duration: "+duration.get()+"\n")
                o.write("\n")
