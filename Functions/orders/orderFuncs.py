import tkinter as tk
from functools import partial
from Functions.allClasses import *
from Functions.buttonFuncs import *
from Functions.validationFunc import *
from Functions.checkCancel import exitAndFlag
from Functions.orders.kittingFuncs import kitting
from Functions.orders.assembFuncs import assembly
trayTypes = ["movable_tray_dark_wood", "movable_tray_light_wood",
             "movable_tray_metal_rusty", "movable_tray_metal_shiny"]  # list of all tray types
kAgv1List = ['[ks1]', '[as1]', '[as2]']  # all possible locations for agv1 in the kitting format
prodList = ["assembly_battery_red", "assembly_battery_green",
            "assembly_battery_blue", "assembly_pump_red", "assembly_pump_green",
            "assembly_pump_blue", "assembly_regulator_red",
            "assembly_regulator_green", "assembly_regulator_blue", "assembly_sensor_red",
            "assembly_sensor_green", "assembly_sensor_blue"]  # list of all parts
agv1List = ['ks1', 'as1', 'as2']  # all possible locations for agv1
def new_order(orderCount, secondOrderFlag, kittingFlag, orderNextFlag, orderFlag, assembFlag, allOrders, firstLengths,kittingShipTempInput,assembProdsFlag,assembProds,kitProdsFlag,kitProds, tempKits, tempAssemb):  # this menu pops up to make a new order for the user
    """Adds a new order. Returns the order using the all orders array. Different values are returned for the first order
    different components of the menu are present for the second order selection"""
    if len(orderCount)>=1:
        secondOrderFlag.set('1')
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
    kittingFunc=partial(kitting, kittingShipTempInput, orderFlag, kitProdsFlag,kittingFlag, kitProds,tempKits, tempAssemb)
    order_kitting = tk.Button(add_order, text="Kitting", command=kittingFunc, state=tk.NORMAL)
    order_kitting.pack(pady=20)
    assemblyFunc=partial(assembly,orderFlag,assembProdsFlag,assembFlag, assembProds, tempAssemb, tempKits)
    order_assembly = tk.Button(add_order, text="Assembly", command=assemblyFunc, state=tk.NORMAL)
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