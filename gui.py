"""GUI for the creation of YAML files for NIST ARIAC. Notes: functions with variables like (a, b, c) have dummy variables. The
tkinter trace function passes variables to functions which are not needed for the function to work properly"""
import tkinter as tk
from tkinter import filedialog
import tkinter.ttk as ttk
import platform
from os import chdir, path
from pathlib import Path
from functools import partial
from PIL import Image, ImageTk  # needed for images in gui
from jsonschema import validate
import json
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
schemaFile=open('./yamlSchemaARIAC.json',)  # opens the schema file

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
createdDir = []  # to deleted directories made if canceled
pathIncrement = []  # gives the full path for recursive deletion
firstLengths = []  # holds the number of products in the first order
breakdowns = []  # holds the robot breakdowns for the robot breakdown order
breakdownAGVs = ['agv1', 'agv2', 'agv3', 'agv4']
breakdownAll = ['agv1', 'agv2', 'agv3', 'agv4', 'as1', 'as2', 'as3', 'as4']
leftColumn=0
middleColumn=1 
middleColumnWidth=10  # width of middle margin for live yaml windows
rightColumn=2

def update_options_yaml(a, b, c):
    """Updates the live yaml file for the options window. This function runs anytime the user input changes"""
    yamlMOB.config(text="  insert_models_over_bins: "+overBins.get())
    yamlMOS.config(text="  insert_models_over_stations: "+overStations.get())
    require_num(beltCycles, 1,2,3)
    yamlBeltOptions.config(text="  belt_population_cycles: "+beltCycles.get())
    yamlGazLogging.config(text="  gazebo_state_logging: "+stateLogging.get())
    yamlGripperType.config(text="  current_gripper_type: "+gripperType.get())
    yamlTimeLim.config(text="time_limit: "+timeLimit.get())


def update_tray_yaml(a, b, c):
    """Updates the live yaml file for the tray window. This function runs anytime the user input changes"""
    if (table1.get()!='' and table1q.get()!='') or (table2.get()!='' and table2q.get()!=''):
        agvHeader.config(text="table_tray_infos:")
        if (table1.get()!='' and table1q.get()!='') and not (table2.get()!='' and table2q.get()!=''):
            table1Label.config(text="  table_1:")
            trayModel1.config(text="    tray_model: "+table1.get())
            quantity1.config(text="    quantity: "+table1q.get())
            table2Label.config(text="")
            trayModel2.config(text="")
            quantity2.config(text="")
        elif (table2.get()!='' and table2q.get()!='') and not (table1.get()!='' and table1q.get()!=''):
            table1Label.config(text="  table_2:")
            trayModel1.config(text="    tray_model: "+table2.get())
            quantity1.config(text="    quantity: "+table2q.get())
            table2Label.config(text="")
            trayModel2.config(text="")
            quantity2.config(text="")
        else:
            table1Label.config(text="  table_1:")
            trayModel1.config(text="    tray_model: "+table1.get())
            quantity1.config(text="    quantity: "+table1q.get())
            table2Label.config(text="  table_2:")
            trayModel2.config(text="    tray_model: "+table2.get())
            quantity2.config(text="    quantity: "+table2q.get())
    else:
        agvHeader.config(text="")
        table1Label.config(text="")
        trayModel1.config(text="")
        quantity1.config(text="")
        table2Label.config(text="")
        trayModel2.config(text="")
        quantity2.config(text="")


def update_agv_info(a, b, c):
    """Updates the live yaml file for the agv_info window. This function runs anytime the user input changes"""
    agv1_loaction.config(text="    location: "+agv1.get())
    agv2_loaction.config(text="    location: "+agv2.get())
    agv3_loaction.config(text="    location: "+agv3.get())
    agv4_loaction.config(text="    location: "+agv4.get())


def update_sensor_blackout(a, b, c):
    """Updates the live yaml file for the sensor_blackout window. This function runs anytime the user input changes"""
    prod_count_yaml.configure(text="  product_count: "+prodCount.get())
    duration_yaml.configure(text="  duration: "+ duration.get())


def update_aisle_layout(a,b,c):
    """Updates the live yaml file for the aisle_layout window. This function runs anytime the user input changes"""
    require_num(human2Wait)
    require_num(human4Wait)
    if human2Wait.get()!='' or human4Wait.get()!='':
        human_header.config(text="aisle_layout:")
        if human2Wait.get()!='' and human4Wait.get()=='':
            person1_header.config(text="  person_1:  # located at as2")
            person1_location.config(text="    location: 3.")
            person1_start.config(text="   start_time: 0.")
            person1_move.config(text="    move_time: 5.")
            person1_wait.config(text="    wait_time: "+human2Wait.get()+".")
        elif human2Wait.get()=='' and human4Wait.get()!='':
            person1_header.config(text="  person_2:  # located at as4")
            person1_location.config(text="    location: -3.")
            person1_start.config(text="   start_time: 16.")
            person1_move.config(text="    move_time: 5.")
            person1_wait.config(text="    wait_time: "+human4Wait.get()+".")
        else:
            person1_header.config(text="  person_1:  # located at as2")
            person1_location.config(text="    location: 3.")
            person1_start.config(text="   start_time: 0.")
            person1_move.config(text="    move_time: 5.")
            person1_wait.config(text="    wait_time: "+human2Wait.get()+".")
            person2_header.config(text="  person_2:  # located at as4")
            person2_location.config(text="    location: -3.")
            person2_start.config(text="   start_time: 16.")
            person2_move.config(text="    move_time: 5.")
            person2_wait.config(text="    wait_time: "+human4Wait.get()+".")
    else:
        human_header.config(text="")
        person1_header.config(text="")
        person1_location.config(text="")
        person1_start.config(text="")
        person1_move.config(text="")
        person1_wait.config(text="")
        person2_header.config(text="")
        person2_location.config(text="")
        person2_start.config(text="")
        person2_move.config(text="")
        person2_wait.config(text="")


def deactivateButton(button, parFlag, c, d, e):
    """Depending on the status of the flag, it will deactivate an activated button"""
    if parFlag.get() =='1':
        button.config(state=tk.DISABLED)


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
    x_val_k_num_func=partial(require_num, x_val_k)
    x_val_k.trace('w', x_val_k_num_func)
    y_val_k_num_func=partial(require_num, y_val_k)
    y_val_k.trace('w', y_val_k_num_func)
    z_val_k_num_func=partial(require_num, z_val_k)
    z_val_k.trace('w', z_val_k_num_func)
    check_rpy = partial(rpy_validation, r_val_k, p_val_k, y_rpy_val_k, kitting_prod_exit)
    r_val_k.trace('w', check_rpy)
    p_val_k.trace('w', check_rpy)
    y_rpy_val_k.trace('w', check_rpy)
    k_products.mainloop()
    add_quotes(r_val_k)
    add_quotes(p_val_k)
    add_quotes(y_rpy_val_k)
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
    x_val_a_num_func=partial(require_num, x_val_a)
    x_val_a.trace('w', x_val_a_num_func)
    y_val_a_num_func=partial(require_num, y_val_a)
    y_val_a.trace('w', y_val_a_num_func)
    z_val_a_num_func=partial(require_num, z_val_a)
    z_val_a.trace('w', z_val_a_num_func)
    check_rpy = partial(rpy_validation, r_val_a, p_val_a, y_rpy_val_a, assemb_prod_exit)
    r_val_a.trace('w', check_rpy)
    p_val_a.trace('w', check_rpy)
    y_rpy_val_a.trace('w', check_rpy)
    a_products.mainloop()
    add_quotes(r_val_a)
    add_quotes(p_val_a)
    add_quotes(y_rpy_val_a)
    assembProds.append(Products(a_product_info.get(),
                       str("[" + x_val_a.get() + ", " + y_val_a.get() + ', ' + z_val_a.get() + "]"),
                       str("[" + r_val_a.get() + ", " + p_val_a.get() + ", " + y_rpy_val_a.get() + "]")))


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
    x_val_s_num_func=partial(require_num, x_val_s)
    x_val_s.trace('w', x_val_s_num_func)
    y_val_s_num_func=partial(require_num, y_val_s)
    y_val_s.trace('w', y_val_s_num_func)
    z_val_s_num_func=partial(require_num, z_val_s)
    z_val_s.trace('w', z_val_s_num_func)
    x_val_e_num_func=partial(require_num, x_val_e)
    x_val_e.trace('w', x_val_e_num_func)
    y_val_e_num_func=partial(require_num, y_val_e)
    y_val_e.trace('w', y_val_e_num_func)
    z_val_e_num_func=partial(require_num, z_val_e)
    z_val_e.trace('w', z_val_e_num_func)
    check_rpy = partial(rpy_validation, r_val_b, p_val_b, y_rpy_val_b, add_bin_exit)
    r_val_b.trace('w', check_rpy)
    p_val_b.trace('w', check_rpy)
    y_rpy_val_b.trace('w', check_rpy)
    add_bin_wind.mainloop()
    add_quotes(r_val_b)
    add_quotes(p_val_b)
    add_quotes(y_rpy_val_b)
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





if __name__ == "__main__":
    """Main part of program. Goes through the main windows of the program and holds all global tkinter stringvars"""
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
    # BEGINNING OF OPTIONS
    options = tk.Tk()
    options.title("Options")
    options.geometry("850x600")
    overBins = tk.StringVar()
    overBins.set("true")
    overBinsLabel = tk.Label(options, text="Insert models over bins:")
    overBinsLabel.grid(column=leftColumn)
    tfOverBins = tk.Button(text="True", width=12, command=tf)
    tfOverBins.grid(column=leftColumn, pady=5)
    overStations = tk.StringVar()
    overStations.set("true")
    overStationsLabel = tk.Label(options, text="Insert models over stations:")
    overStationsLabel.grid(column=leftColumn)
    tfOverStations = tk.Button(text="True", width=12, command=tf2)
    tfOverStations.grid(column=leftColumn, pady=5)
    beltCycles = tk.StringVar()
    beltCycles.set("0")
    popCycleLabel = tk.Label(options, text="Enter the belt population cycles (enter nothing to skip):")
    popCycleLabel.grid(column=leftColumn)
    popCycleBox = tk.Entry(options, textvariable=beltCycles)
    popCycleBox.grid(column=leftColumn)
    stateLogging = tk.StringVar()
    stateLogging.set("true")
    stateLoggingLabel = tk.Label(options, text="Gazebo state logging:")
    stateLoggingLabel.grid(column=leftColumn)
    tfStateLogging = tk.Button(text="True", width=12, command=tf3)
    tfStateLogging.grid(column=leftColumn, pady=5)
    gripperType = tk.StringVar()
    gripperType.set("gripper_tray")
    gripperTypeLabel = tk.Label(options, text="Gripper type:")
    gripperTypeLabel.grid(column=leftColumn)
    gripperTypeButton = tk.Button(text="Gripper Tray", width=12, command=cgt)
    gripperTypeButton.grid(column=leftColumn, pady=5)
    timeLimit = tk.StringVar()
    timeLimit.set("500")
    timeLimitLabel = tk.Label(options, text="Time limit (-1-No time limit | 500-time used in qualifiers and finals):")
    timeLimitLabel.grid(column=leftColumn)
    timeLimitButton = tk.Button(text="500", width=12, command=tl)
    timeLimitButton.grid(column=leftColumn, pady=5)
    nextButton = tk.Button(options, text="Next", command=options.destroy)
    nextButton.grid(column=leftColumn, pady=20)
    cancel_options = partial(cancel_wind, options, cancelFlag)
    cancelOptions = tk.Button(options, text="Cancel and Exit", command=cancel_options)
    cancelOptions.grid(column=leftColumn, pady=20)
    #end of options and menu | beginning of sample yaml output
    optionsMiddleMargin = tk.Label(options, text=" "*middleColumnWidth)
    optionsMiddleMargin.grid(column=middleColumn, row=0)
    optionsHeader=tk.Label(options, text="options:")
    optionsHeader.grid(column=rightColumn, row=0, sticky=tk.W)
    yamlMOB = tk.Label(options, text="  insert_models_over_bins: "+overBins.get())
    yamlMOB.grid(column=rightColumn, row=1, sticky=tk.W)
    yamlMOS = tk.Label(options, text="  insert_models_over_stations: "+overStations.get())
    yamlMOS.grid(column=rightColumn, row=2, sticky=tk.W)
    yamlBeltOptions = tk.Label(options, text="  belt_population_cycles: "+beltCycles.get())
    yamlBeltOptions.grid(column=rightColumn, row=3, sticky=tk.W)
    yamlGazLogging = tk.Label(options, text="  gazebo_state_logging: "+stateLogging.get())
    yamlGazLogging.grid(column=rightColumn, row=4, sticky=tk.W)
    yamlOptionsComment = tk.Label(options, text="  # mandatory: gripper_tray or gripper_part")
    yamlOptionsComment.grid(column=rightColumn, row=5, sticky=tk.W)
    yamlGripperType = tk.Label(options, text="  current_gripper_type: "+gripperType.get())
    yamlGripperType.grid(column=rightColumn, row=6, sticky=tk.W)
    yamlTimeLim = tk.Label(options, text="time_limit: "+timeLimit.get())
    yamlTimeLim.grid(column=rightColumn, row=7, sticky=tk.W)
    overBins.trace('w', update_options_yaml)
    overStations.trace('w', update_options_yaml)
    beltCycles.trace('w', update_options_yaml)
    stateLogging.trace('w', update_options_yaml)
    gripperType.trace('w', update_options_yaml)
    timeLimit.trace('w', update_options_yaml)
    options.mainloop()
    check_cancel(cancelFlag.get(), pathIncrement, fileName, createdDir)
    # END OF GETTING OPTIONS
    # ----------------------------------------------------------------------------------------------------------------------
    # BEGINNING OF TABLE_TRAY_INFOS
    trayInfo = tk.Tk()
    trayInfo.title("Tray Information")
    trayInfo.geometry("850x600")
    trayInstructions = tk.Label(trayInfo, text="If you would like to skip a tray, leave it blank, leave it blank")
    trayInstructions.grid(column=leftColumn)
    table1 = tk.StringVar()
    table1.set("")
    table1Label = tk.Label(trayInfo, text="Choose the material for table 1")
    table1Label.grid(column=leftColumn)
    table1Menu = tk.OptionMenu(trayInfo, table1, "", "movable_tray_dark_wood", "movable_tray_light_wood",
                               "movable_tray_metal_rusty", "movable_tray_metal_shiny")
    table1Menu.grid(column=leftColumn)
    table1q = tk.StringVar()
    table1q.set("")
    table1qLabel = tk.Label(trayInfo, text="Choose the quantity for table 1")
    table1qLabel.grid(column=leftColumn)
    table1qMenu = tk.OptionMenu(trayInfo, table1q, "", "1", "2", "3")
    table1qMenu.grid(column=leftColumn)
    table2 = tk.StringVar()
    table2.set("")
    table2Label = tk.Label(trayInfo, text="Choose the material for table 2")
    table2Label.grid(column=leftColumn)
    table2Menu = tk.OptionMenu(trayInfo, table2, "", "movable_tray_dark_wood", "movable_tray_light_wood",
                               "movable_tray_metal_rusty", "movable_tray_metal_shiny")
    table2Menu.grid(column=leftColumn)
    table2q = tk.StringVar()
    table2q.set("")
    table2qLabel = tk.Label(trayInfo, text="Choose the quantity for table 2")
    table2qLabel.grid(column=leftColumn)
    table2qMenu = tk.OptionMenu(trayInfo, table2q, "", "1", "2", "3")
    table2qMenu.grid(column=leftColumn)
    trayNext = tk.Button(trayInfo, text="Next", command=trayInfo.destroy)
    trayNext.grid(column=leftColumn, pady=20)
    traySkipFlag = tk.StringVar()
    traySkipFlag.set("0")
    tray_skip = partial(skip_wind, traySkipFlag, trayInfo)
    skipButton = tk.Button(trayInfo, text="Skip", command=tray_skip)
    skipButton.grid(column=leftColumn)
    cancel_tray = partial(cancel_wind, trayInfo, cancelFlag)
    cancelTray = tk.Button(trayInfo, text="Cancel and Exit", command=cancel_tray)
    cancelTray.grid(column=leftColumn)
    #end of options and menu | beginning of sample yaml output
    trayMiddleMargin = tk.Label(trayInfo, text=" "*middleColumnWidth)
    trayMiddleMargin.grid(column=middleColumn, row=0)
    agvHeader=tk.Label(trayInfo, text="")
    agvHeader.grid(column=rightColumn, row=0, sticky=tk.W)
    table1Label=tk.Label(trayInfo, text="")
    table1Label.grid(column=rightColumn, row=1, sticky=tk.W)
    trayModel1=tk.Label(trayInfo, text="")
    trayModel1.grid(column=rightColumn, row=2, sticky=tk.W)
    quantity1 = tk.Label(trayInfo, text="")
    quantity1.grid(column=rightColumn, row=3, sticky=tk.W)
    table2Label=tk.Label(trayInfo, text="")
    table2Label.grid(column=rightColumn, row=4, sticky=tk.W)
    trayModel2=tk.Label(trayInfo, text="")
    trayModel2.grid(column=rightColumn, row=5, sticky=tk.W)
    quantity2 = tk.Label(trayInfo, text="")
    quantity2.grid(column=rightColumn, row=6, sticky=tk.W)
    table1.trace('w', update_tray_yaml)
    table1q.trace('w', update_tray_yaml)
    table2.trace('w', update_tray_yaml)
    table2q.trace('w', update_tray_yaml)
    trayInfo.mainloop()
    check_cancel(cancelFlag.get(), pathIncrement, fileName, createdDir)
    # END OF TABLE MENUS
    # -----------------------------------------------------------------------------------
    # BEGINNING OF GETTING AGV_INFOS
    agvInfo = tk.Tk()
    agvInfo.geometry("850x600")
    agvInfo.title("AGV Information")
    agv1 = tk.StringVar()
    agv1.set("ks1")
    agv1Label = tk.Label(agvInfo, text="AGV1 Location:")
    agv1Label.grid(column=leftColumn)
    agv1Menu = tk.OptionMenu(agvInfo, agv1, *agv1List)
    agv1Menu.grid(column=leftColumn)
    agv2 = tk.StringVar()
    agv2.set("ks2")
    agv2Label = tk.Label(agvInfo, text="AGV2 Location:")
    agv2Label.grid(column=leftColumn)
    agv2Menu = tk.OptionMenu(agvInfo, agv2, *agv2List)
    agv2Menu.grid(column=leftColumn)
    agv3 = tk.StringVar()
    agv3.set("ks3")
    agv3Label = tk.Label(agvInfo, text="AGV3 Location:")
    agv3Label.grid(column=leftColumn)
    agv3Menu = tk.OptionMenu(agvInfo, agv3, *agv3List)
    agv3Menu.grid(column=leftColumn)
    agv4 = tk.StringVar()
    agv4.set("ks4")
    agv4Label = tk.Label(agvInfo, text="AGV4 Location:")
    agv4Label.grid(column=leftColumn)
    agv4Menu = tk.OptionMenu(agvInfo, agv4, *agv4List)
    agv4Menu.grid(column=leftColumn)
    addProdFunc=partial(add_product,agv1Prods, agv2Prods, agv3Prods, agv4Prods)
    productButton = tk.Button(agvInfo, text="Add Product", command=addProdFunc)
    productButton.grid(column=leftColumn)
    agvNext = tk.Button(agvInfo, text="Next", command=agvInfo.destroy)
    agvNext.grid(column=leftColumn, pady=20)
    cancel_agv = partial(cancel_wind, agvInfo, cancelFlag)
    cancelAgv = tk.Button(agvInfo, text="Cancel and Exit", command=cancel_agv)
    cancelAgv.grid(column=leftColumn, pady=20)
    #end of options and menu | beginning of sample yaml output
    agvMiddleMargin = tk.Label(agvInfo, text=" "*middleColumnWidth)
    agvMiddleMargin.grid(column=middleColumn, row=0)
    agv_header=tk.Label(agvInfo, text="agv_infos")
    agv_header.grid(column=rightColumn, row=0, sticky=tk.W)
    agv1_header=tk.Label(agvInfo, text="  agv1:")
    agv1_header.grid(column=rightColumn, row=1, sticky=tk.W)
    agv1_loaction=tk.Label(agvInfo, text="    location: "+agv1.get())
    agv1_loaction.grid(column=rightColumn, row=2, sticky=tk.W)
    agv2_header=tk.Label(agvInfo, text="  agv2:")
    agv2_header.grid(column=rightColumn, row=3, sticky=tk.W)
    agv2_loaction=tk.Label(agvInfo, text="    location: "+agv2.get())
    agv2_loaction.grid(column=rightColumn, row=4, sticky=tk.W)
    agv3_header=tk.Label(agvInfo, text="  agv3:")
    agv3_header.grid(column=rightColumn, row=5, sticky=tk.W)
    agv3_loaction=tk.Label(agvInfo, text="    location: "+agv3.get())
    agv3_loaction.grid(column=rightColumn, row=6, sticky=tk.W)
    agv4_header=tk.Label(agvInfo, text="  agv4:")
    agv4_header.grid(column=rightColumn, row=7, sticky=tk.W)
    agv4_loaction=tk.Label(agvInfo, text="    location: "+agv4.get())
    agv4_loaction.grid(column=rightColumn, row=8, sticky=tk.W)
    agv1.trace('w', update_agv_info)
    agv2.trace('w', update_agv_info)
    agv3.trace('w', update_agv_info)
    agv4.trace('w', update_agv_info)
    agvInfo.mainloop()
    check_cancel(cancelFlag.get(), pathIncrement, fileName, createdDir)
    # END OF AGV OPTIONS
    # ----------------------------------------------------------------------------------------------------------------------
    # BEGINNING OF ORDERS
    orderID = 0
    ordersInfo = tk.Tk()
    ordersInfo.geometry("850x600")
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
    cancel_orders = partial(cancel_wind, ordersInfo, cancelFlag)
    cancelOrders = tk.Button(ordersInfo, text="Cancel and Exit", command=cancel_orders)
    cancelOrders.pack(pady=20)
    ordersInfo.mainloop()
    allOrders.reverse()
    partC = 0
    check_cancel(cancelFlag.get(), pathIncrement, fileName, createdDir)
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
    # END OF ORDERS
    # ----------------------------------------------------------------------------------------------------------------------
    # BEGINNING OF MODELS OVER BINS
    if overBins.get() == 'true':
        overBinsWind = tk.Tk()
        overBinsWind.geometry("850x600")
        overBinsWind.title("Models Over Bins Menu")
        addBinButton = tk.Button(overBinsWind, text="Add bin", command=add_bin)
        addBinButton.pack(pady=20)
        overBinsNext = tk.Button(overBinsWind, text="Next", command=overBinsWind.destroy)
        overBinsNext.pack(pady=20)
        cancel_over_bins = partial(cancel_wind, overBinsWind, cancelFlag)
        cancelOverBins = tk.Button(overBinsWind, text="Cancel and Exit", command=cancel_over_bins)
        cancelOverBins.pack(pady=20)
        overBinsWind.mainloop()
        check_cancel(cancelFlag.get(), pathIncrement, fileName, createdDir)
    # END OF MODELS OVER BINS
    # ----------------------------------------------------------------------------------------------------------------------
    # BEGINNING OF MODELS OVER STATIONS
    if overStations.get() == 'true':
        overStationsWind = tk.Tk()
        overStationsWind.geometry("850x600")
        overStationsWind.title("Models Over Stations Menu")
        addStationFunc=partial(add_station, modelsOverStationsInfo)
        addStationButton = tk.Button(overStationsWind, text="Add station", command=addStationFunc)
        addStationButton.pack(pady=20)
        overStationsNext = tk.Button(overStationsWind, text="Next", command=overStationsWind.destroy)
        overStationsNext.pack(pady=20)
        cancel_over_stations = partial(cancel_wind, overStationsWind, cancelFlag)
        cancelOverStations = tk.Button(overStationsWind, text="Cancel and Exit", command=cancel_over_stations)
        cancelOverStations.pack(pady=20)
        overStationsWind.mainloop()
        check_cancel(cancelFlag.get(), pathIncrement, fileName, createdDir)
    # END OF MODELS OVER STATIONS
    # ----------------------------------------------------------------------------------------------------------------------
    # BEGINNING OF BELT MODELS
    if beltCycles.get() != '0':
        beltCyclesWind = tk.Tk()
        beltCyclesWind.geometry("850x600")
        beltCyclesWind.title("Belt Cycles Menu")
        addBeltFunc=partial(add_belt, beltCycleInfo)
        addBeltCycle = tk.Button(beltCyclesWind, text="Add belt cycle", command=addBeltFunc)
        addBeltCycle.pack(pady=20)
        beltCycleNext = tk.Button(beltCyclesWind, text="Next", command=beltCyclesWind.destroy)
        beltCycleNext.pack(pady=20)
        cancel_belt_cycles = partial(cancel_wind, beltCyclesWind, cancelFlag)
        cancelBeltCycle = tk.Button(beltCyclesWind, text="Cancel and Exit", command=cancel_belt_cycles)
        cancelBeltCycle.pack(pady=20)
        beltCyclesWind.mainloop()
        check_cancel(cancelFlag.get(), pathIncrement, fileName, createdDir)
    # END OF BELT CYCLES
    # -----------------------------------------------------------------------------------
    # BEGINNING OF AGILITY CHALLENGE SELECTION
    challengeWind = tk.Tk()
    challengeWind.geometry("850x600")
    challengeWind.title("agility challenge Selection Window")
    robotBreakdownSelection = tk.StringVar()
    robotBreakdownSelection.set('0')
    faultyProdSelection = tk.StringVar()
    faultyProdSelection.set('0')
    dropSelection = tk.StringVar()
    dropSelection.set('0')
    sensorBlackoutSelection = tk.StringVar()
    sensorBlackoutSelection.set('0')
    humanSelection = tk.StringVar()
    humanSelection.set('0')
    mainChallengeLabel = tk.Label(challengeWind, text="Please select the agility challenges you would like to do")
    mainChallengeLabel.pack()
    if len(binProds)>0:
        faultyProductCheckbox = tk.Checkbutton(challengeWind, text='Faulty Product', variable=faultyProdSelection, onvalue='1', offvalue='0')
        faultyProductCheckbox.pack()
    faultyGripperCheckbox = tk.Checkbutton(challengeWind, text='Faulty Gripper', variable=dropSelection, onvalue='1', offvalue='0')
    faultyGripperCheckbox.pack()
    sensorBlackoutCheckbox = tk.Checkbutton(challengeWind, text='Sensor Blackout', variable=sensorBlackoutSelection, onvalue='1', offvalue='0')
    sensorBlackoutCheckbox.pack()
    robotBreakdownCheckbox = tk.Checkbutton(challengeWind, text="Robot Breakdown", variable=robotBreakdownSelection, onvalue='1', offvalue='0')
    robotBreakdownCheckbox.pack()
    if len(kitProds)>0 and len(assembProds)>0:
        humanCheckbox = tk.Checkbutton(challengeWind, text='Human Obstacles', variable=humanSelection, onvalue='1', offvalue='0')
        humanCheckbox.pack()
    challengeNext = tk.Button(challengeWind, text="Next", command=challengeWind.destroy)
    challengeNext.pack(pady=20)
    cancel_challenge_func = partial(cancel_wind, challengeWind, cancelFlag)
    cancelChallenge = tk.Button(challengeWind, text="Cancel and Exit", command=cancel_challenge_func)
    cancelChallenge.pack(pady=20)
    challengeWind.mainloop()
    check_cancel(cancelFlag.get(), pathIncrement, fileName, createdDir)
    # END OF AGILITY CHALLENGE SELECTION
    # -----------------------------------------------------------------------------------
    # BEGINNING OF FAULTY PRODUCTS
    if len(binProds)>0 and faultyProdSelection.get()=='1':
        faultyWind = tk.Tk()
        faultyWind.geometry("850x600")
        faultyWind.title("Faulty Products Menu")
        faultyWindLabel = tk.Label(faultyWind, text="This is needed for the Faulty Product Agility Challenge")
        faultyWindLabel.pack()
        faultyProdFunc=partial(add_faulty_prod, binProds, faultyProdList)
        addProd = tk.Button(faultyWind, text="Add Product", command=faultyProdFunc)
        addProd.pack(pady=20)
        faulty_skip = partial(skip_wind, faultySkipFlag, faultyWind)
        skipFaultyProd = tk.Button(faultyWind, text="Skip", command=faulty_skip)
        skipFaultyProd.pack(pady=20)
        faultyProdNext = tk.Button(faultyWind, text="Next", command=faultyWind.destroy)
        faultyProdNext.pack(pady=20)
        cancel_faulty_products = partial(cancel_wind, faultyWind, cancelFlag)
        cancelFaultyProd = tk.Button(faultyWind, text="Cancel and Exit", command=cancel_faulty_products)
        cancelFaultyProd.pack(pady=20)
        faultyWind.mainloop()
        check_cancel(cancelFlag.get(), pathIncrement, fileName, createdDir)
    # END OF FAULTY PRODUCTS
    # --------------------------------------------------------------------------
    # BEGINNING OF DROPS
    if dropSelection.get()=='1':
        dropsWind = tk.Tk()
        dropsWind.title("Drops Menu")
        dropsWind.geometry("850x600")
        dropsWindLabel = tk.Label(dropsWind, text="This is needed for the Faulty Gripper Agility Challenge")
        dropsWindLabel.pack()
        dropRegionFunc=partial(add_drop_region, dropsInfo)
        addDrop = tk.Button(dropsWind, text="Add New Drop Region", command=dropRegionFunc)
        addDrop.pack()
        drops_skip = partial(skip_wind, dropsSkipFlag, dropsWind)
        skipDrops = tk.Button(dropsWind, text="Skip", command=drops_skip)
        skipDrops.pack(pady=20)
        dropsNext = tk.Button(dropsWind, text="Next", command=dropsWind.destroy)
        dropsNext.pack(pady=20)
        cancel_drops = partial(cancel_wind, dropsWind, cancelFlag)
        cancelDrops = tk.Button(dropsWind, text="Cancel and Exit", command=cancel_drops)
        cancelDrops.pack(pady=20)
        dropsWind.mainloop()
        check_cancel(cancelFlag.get(), pathIncrement, fileName, createdDir)
    # END OF DROPS
    # --------------------------------------------------------------------------
    # BEGINNING OF SENSOR BLACKOUT
    if sensorBlackoutSelection.get()=='1':
        sensorBlackoutWind = tk.Tk()
        sensorBlackoutWind.title("Sensor Blackout")
        sensorBlackoutWind.geometry("850x600")
        prodCount = tk.StringVar()
        prodCount.set('0')
        duration = tk.StringVar()
        duration.set('0')
        prodCountLabel = tk.Label(sensorBlackoutWind, text="Enter the product count for the Sensor Blackout Agility Challenge           ")
        prodCountLabel.grid(column=leftColumn)
        prodCountEntry = tk.Entry(sensorBlackoutWind, textvariable=prodCount)
        prodCountEntry.grid(column=leftColumn)
        durationLabel = tk.Label(sensorBlackoutWind, text="Enter the duration of the sensor blackout")
        durationLabel.grid(column=leftColumn)
        durationEntry = tk.Entry(sensorBlackoutWind, textvariable=duration)
        durationEntry.grid(column=leftColumn)
        sensor_blackout_skip = partial(skip_wind, sensor_blackout_skip_flag, sensorBlackoutWind)
        sensorBlackoutSkip = tk.Button(sensorBlackoutWind, text="Skip and Exit", command=sensor_blackout_skip)
        sensorBlackoutSkip.grid(column=leftColumn, pady=20)
        sensorBlackoutSE = tk.Button(sensorBlackoutWind, text="Save and Exit", command=sensorBlackoutWind.destroy)
        sensorBlackoutSE.grid(column=leftColumn, pady=20)
        cancel_sensor_blackout = partial(cancel_wind, sensorBlackoutWind, cancelFlag)
        cancelSensorBlackout = tk.Button(sensorBlackoutWind, text="Cancel and Exit", command=cancel_sensor_blackout)
        cancelSensorBlackout.grid(column=leftColumn, pady=20)
        #end of options and menu | beginning of sample yaml output
        sensorMiddleMargin = tk.Label(sensorBlackoutWind, text=" "*middleColumnWidth)
        sensorMiddleMargin.grid(column=middleColumn, row=0)
        sensor_blackout_header = tk.Label(sensorBlackoutWind, text="sensor_blackout:")
        sensor_blackout_header.grid(column=rightColumn, row=0, sticky=tk.W)
        prod_count_yaml = tk.Label(sensorBlackoutWind, text="  product_count: "+prodCount.get())
        prod_count_yaml.grid(column=rightColumn, row=1, sticky=tk.W)
        duration_yaml = tk.Label(sensorBlackoutWind, text="  duration: "+ duration.get())
        duration_yaml.grid(column=rightColumn, row=2, sticky=tk.W)
        prodCount.trace('w', update_sensor_blackout)
        duration.trace('w', update_sensor_blackout)
        sensorBlackoutWind.mainloop()
        check_cancel(cancelFlag.get(), pathIncrement, fileName, createdDir)
    #END OF SENSOR BLACKOUT
    #-------------------------------------------------------------------------------------------
    #BEGINNING OF ROBOT BREAKDOWN
    if robotBreakdownSelection.get()=='1':
        bdWind = tk.Tk()
        bdWind.title("Breakdown Menu")
        bdWind.geometry("850x600")
        bdWindLabel = tk.Label(bdWind, text="This is needed for the Robot Breakdown Agility Challenge")
        bdWindLabel.pack()
        addRoboFunc=partial(add_robot_breakdown, breakdowns, len(orderCount))
        addBD = tk.Button(bdWind, text="Add New Robot Breakdown", command=addRoboFunc)
        addBD.pack()
        bdNext = tk.Button(bdWind, text="Next", command=bdWind.destroy)
        bdNext.pack(pady=20)
        cancelBDFunc = partial(cancel_wind, bdWind, cancelFlag)
        cancelBD = tk.Button(bdWind, text="Cancel and Exit", command=cancelBDFunc)
        cancelBD.pack(pady=20)
        bdWind.mainloop()
        check_cancel(cancelFlag.get(), pathIncrement, fileName, createdDir)
    #END OF ROBOT BREAKDOWN
    #-------------------------------------------------------------------------------------------
    #BEGINNING OF HUMAN OBSTACLES
    if humanSelection.get()=='1':
        humanWind = tk.Tk()
        human2Wait = tk.StringVar()
        human2Wait.set("")
        human4Wait = tk.StringVar()
        human4Wait.set("")
        humanWind.title("Human Menu")
        humanWind.geometry("850x600")
        humanWindLabel = tk.Label(humanWind, text="This is needed for the Human Obstacles Agility Challenge. Leave blank to not add the human")
        humanWindLabel.grid(column=leftColumn)
        human2Label=tk.Label(humanWind, text="Human at as2")
        human2Label.grid(column=leftColumn)
        human2Entry=tk.Entry(humanWind, textvariable=human2Wait)
        human2Entry.grid(column=leftColumn)
        human4Label=tk.Label(humanWind, text="Human at as4")
        human4Label.grid(column=leftColumn)
        human4Entry=tk.Entry(humanWind, textvariable=human4Wait)
        human4Entry.grid(column=leftColumn)
        humanWindNext = tk.Button(humanWind, text="Next", command=humanWind.destroy)
        humanWindNext.grid(column=leftColumn, pady=20)
        cancelHumanWindFunc = partial(cancel_wind, humanWind, cancelFlag)
        cancelHuman = tk.Button(humanWind, text="Cancel and Exit", command=cancelHumanWindFunc)
        cancelHuman.grid(column=leftColumn, pady=20)
        #end of options and menu | beginning of sample yaml output
        humanMiddleMargin = tk.Label(humanWind, text=" "*middleColumnWidth)
        humanMiddleMargin.grid(column=middleColumn, row=0)   
        human_header=tk.Label(humanWind, text="")
        human_header.grid(column=rightColumn, row=0, sticky=tk.W)
        person1_header = tk.Label(humanWind, text="")
        person1_header.grid(column=rightColumn, row=1, sticky=tk.W)
        person1_location = tk.Label(humanWind, text="")
        person1_location.grid(column=rightColumn, row=2, sticky=tk.W)
        person1_start = tk.Label(humanWind, text="")
        person1_start.grid(column=rightColumn, row=3, sticky=tk.W)
        person1_move = tk.Label(humanWind, text="")
        person1_move.grid(column=rightColumn, row=4, sticky=tk.W)
        person1_wait = tk.Label(humanWind, text="")
        person1_wait.grid(column=rightColumn, row=5, sticky=tk.W)
        person2_header = tk.Label(humanWind, text="")
        person2_header.grid(column=rightColumn, row=6, sticky=tk.W)
        person2_location = tk.Label(humanWind, text="")
        person2_location.grid(column=rightColumn, row=7, sticky=tk.W)
        person2_start = tk.Label(humanWind, text="")
        person2_start.grid(column=rightColumn, row=8, sticky=tk.W)
        person2_move = tk.Label(humanWind, text="")
        person2_move.grid(column=rightColumn, row=9, sticky=tk.W)
        person2_wait = tk.Label(humanWind, text="")
        person2_wait.grid(column=rightColumn, row=10, sticky=tk.W)
        human2Wait.trace('w', update_aisle_layout)
        human4Wait.trace('w', update_aisle_layout)
        humanWind.mainloop()
        check_cancel(cancelFlag.get(), pathIncrement, fileName, createdDir)
    #END OF HUMAN OBSTACLES
    #-------------------------------------------------------------------------------------------
    #BEGINNING OF FILE WRITING
    with open(saveFileName, "a") as o:
        o.write("# yaml-language-server: $schema=yamlSchemaARIAC.json\n")  # implements the yaml schema to check the file
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
    if humanSelection.get()=='1':
        with open(saveFileName, "a") as o:
            if human2Wait.get()!='' or human4Wait.get()!='':
                o.write("\n\n\naisle_layout:\n")
                if human2Wait.get()!='':
                    o.write(" person_1: #located at as2\n")
                    o.write("  location: 3\n")
                    o.write("  start_time: 0.\n")
                    o.write("  move_time: 5.\n")
                    o.write("  wait_time: "+human2Wait.get()+".\n")
                if human4Wait.get()!='':
                    o.write(" person2: #located at as4\n")
                    o.write("  location: -3\n")
                    o.write("  start_time: 16.\n")
                    o.write("  move_time: 5.\n")
                    o.write("  wait_time: "+human4Wait.get()+".\n")
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
                for breakdown in breakdowns:
                    if breakdown.orderID == str(orderID):
                        o.write("  disable_robot: ["+breakdown.robotType+", "+breakdown.location +", "+ breakdown.numberProd+"]\n")
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
                    o.write("   stations: [" + i.assembly[orderInd].stations + ']\n')
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
    if faultySkipFlag.get() == '0' and len(faultyProdList) > 0 and faultyProdSelection.get()=='1':
            faultyProdList.reverse()
            with open(saveFileName, 'a') as o:
                o.write("\nfaulty_products:\n")
                for prod in faultyProdList:
                    o.write(" - "+prod+"\n")
                o.write("\n")
    dropCount = 0
    if dropsSkipFlag.get() == '0' and len(dropsInfo) > 0 and dropSelection.get()=='1':
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
    if sensor_blackout_skip_flag.get() == '0' and sensorBlackoutSelection.get()=='1':
            with open(saveFileName, 'a') as o:
                o.write("\nsensor_blackout:\n")
                o.write(" product_count: "+prodCount.get()+"\n")
                o.write(" duration: "+duration.get()+"\n")
                o.write("\n")
    with open(saveFileName, "r") as yamlFile:
        try:
            outputFile=yaml.full_load(yamlFile)
            validateARIAC.validateAriac(outputFile, schemaFile)
        except yaml.YAMLError as exception:
            raise exception