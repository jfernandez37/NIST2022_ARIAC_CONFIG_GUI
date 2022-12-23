import tkinter as tk
from functools import partial
from Functions.allClasses import *
from Functions.buttonFuncs import *
from Functions.updateRanges import update_dest
from Functions.validationFunc import *
from Functions.checkCancel import exitAndFlag
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
    kittingFunc=partial(kitting, kittingShipTempInput, orderFlag, kitProdsFlag,kittingFlag, kitProds,tempKits)
    order_kitting = tk.Button(add_order, text="Kitting", command=kittingFunc, state=tk.NORMAL)
    order_kitting.pack(pady=20)
    assemblyFunc=partial(assembly,orderFlag,assembProdsFlag,assembFlag, assembProds, tempAssemb)
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


def update_kitting_ship(second_tray, second_agv, ship_count, second_dest, window, kittingShipTempInput,d,e,f):  # updates the trays for kitting shipments
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


def kitting(kittingShipTempInput, orderFlag, kitProdsFlag,kittingFlag, kitProds,tempKits):  # allows the user to add kitting to an order
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
    getKProdsFunc=partial(get_k_products,kitProdsFlag, kitProds)
    add_k_products = tk.Button(kitting_wind, text="Add Product", command=getKProdsFunc)
    add_k_products.pack(side=tk.BOTTOM, pady=20)
    update_with_arg = partial(update_dest, get_k_dest, k_agv, k_destination)
    update_ship = partial(update_kitting_ship, second_tray, second_agv, ship_count, second_dest, kitting_wind,kittingShipTempInput)
    kitActButtonFunc = partial(activateButton, order_kitting, kitProdsFlag)
    kitProdsFlag.trace('w', kitActButtonFunc)
    k_agv.trace('w', update_with_arg)
    ship_count.trace('w', update_ship)
    kittingFlag.set('1')
    kitting_wind.mainloop()
    tempKits.append(Kitting(ship_count.get(), trays.get(), second_tray.get(), k_agv.get(),
                            second_agv.get(), k_destination.get(), second_dest.get(), kitProds))


def get_k_products(kitProdsFlag, kitProds):  # adds a product to kitting
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


def assembly(orderFlag,assembProdsFlag,assembFlag, assembProds, tempAssemb):  # adds assembly to an order
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
    getAssembProdFunc=partial(get_a_products,assembProdsFlag, assembProds)
    add_a_products = tk.Button(assemb_wind, text="Add Product", command=getAssembProdFunc)
    add_a_products.pack(pady=20)
    exitAssemb = partial(exitAndFlag, assemb_wind, orderFlag)
    order_assemb = tk.Button(assemb_wind, text="Save and Exit", command=exitAssemb, state=tk.DISABLED)
    order_assemb.pack(pady=20)
    assembActButtonFunc = partial(activateButton, order_assemb, assembProdsFlag)
    assembProdsFlag.trace('w', assembActButtonFunc)
    assembFlag.set('1')
    assemb_wind.mainloop()
    tempAssemb.append(Assembly(a_ship_count.get(), a_stations.get(), assembProds))


def get_a_products(assembProdsFlag, assembProds):  # adds a product to assembly
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