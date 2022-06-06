import tkinter as tk
import os.path
from os import path
from functools import partial

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
trayTypes = ["[movable_tray_dark_wood]", "[movable_tray_light_wood]",
             "[movable_tray_metal_rusty]", "[movable_tray_metal_shiny]"]  # list of all tray types
modelsOverBinsInfo = []  # holds the information from the models over bins function
modelsOverStationsInfo = []  # holds all the information from the models over stations function
beltCycleInfo = []  # holds all the information from the belt cycle function


def tf():  # cycles through the true or false button for the over bins option
    if tfOverBins.config('text')[-1] == 'True':
        tfOverBins.config(text='False')
        overBins.set("false")
    elif tfOverBins.config('text')[-1] == 'None':
        tfOverBins.config(text='True')
        overBins.set("true")
    else:
        tfOverBins.config(text='None')
        overBins.set("none")


def tf2():  # cycles through the true or false button for the over stations option
    if tfOverStations.config('text')[-1] == 'True':
        tfOverStations.config(text='False')
        overStations.set("false")
    elif tfOverStations.config('text')[-1] == 'None':
        tfOverStations.config(text='True')
        overStations.set("true")
    else:
        tfOverStations.config(text='None')
        overStations.set("none")


def tf3():  # cycles through the true or false button for the gazebo state logging option
    if tfStateLogging.config('text')[-1] == 'True':
        tfStateLogging.config(text='False')
        stateLogging.set("false")
    elif tfStateLogging.config('text')[-1] == 'None':
        tfStateLogging.config(text='True')
        stateLogging.set("true")
    else:
        tfStateLogging.config(text='None')
        stateLogging.set("none")


def cgt():  # cycles through the options for the current gripper type option
    if gripperTypeButton.config('text')[-1] == 'Gripper Tray':
        gripperTypeButton.config(text='Gripper Part')
        gripperType.set("gripper_part")
    else:
        gripperTypeButton.config(text='Gripper Tray')
        gripperType.set("gripper_tray")


def tl():  # cycles through the options for the time limit option
    if timeLimitButton.config('text')[-1] == '500':
        timeLimitButton.config(text='-1')
        timeLimit.set("-1")
    else:
        timeLimitButton.config(text='500')
        timeLimit.set("500")


def tray_skip():  # skips the tray menu
    skipFlag.set("1")
    trayInfo.destroy()


def get_file_name_next():  # checks to see if the file name the user selects exists or is empty
    if fileName.get() == "" and reqFlag.get() == "0":
        req_label = tk.Label(getFileName, text="This field is required. Please enter a non-empty file name")
        req_label.pack()
        reqFlag.set('1')
    if (path.exists(fileName.get()) or path.exists(fileName.get() + '.yaml')) and existFlag.get() == '0':
        exist_label = tk.Label(getFileName,
                               text="A file with this name already exists. Please enter another file name.")
        exist_label.pack()
        existFlag.set('1')
    elif fileName.get() != '':
        getFileName.destroy()


def add_product():  # adds a product in agv_infos
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
    agv_id.set("agv1")
    product_menu_label = tk.Label(product_info, text="Choose the agv for the product:")
    product_menu_label.pack()
    product_menu = tk.OptionMenu(product_info, agv_id, "agv1", "agv2", "agv3", "agv4")
    product_menu.pack()
    product_type = tk.StringVar(product_info)
    product_type.set("assembly_battery_red")
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
        agv1ProdTypes.set(agv1ProdTypes.get() + ' ' + product_type.get())
        agv1Coords.set(agv1Coords.get() + ' ' + "[" + x_val.get() + ',' + y_val.get() + ',' + z_val.get() + "]")
        agv1Rot.set(agv1Rot.get() + ' ' + '[' + r_x_val.get() + ',' + r_y_val.get() + ',' + r_z_val.get() + ']')
    if agv_id.get() == 'agv2':
        agv2ProdTypes.set(agv2ProdTypes.get() + ' ' + product_type.get())
        agv2Coords.set(agv2Coords.get() + ' ' + "[" + x_val.get() + ',' + y_val.get() + ',' + z_val.get() + "]")
        agv2Rot.set(agv2Rot.get() + ' ' + '[' + r_x_val.get() + ',' + r_y_val.get() + ',' + r_z_val.get() + ']')
    if agv_id.get() == 'agv3':
        agv3ProdTypes.set(agv3ProdTypes.get() + ' ' + product_type.get())
        agv3Coords.set(agv3Coords.get() + ' ' + "[" + x_val.get() + ',' + y_val.get() + ',' + z_val.get() + "]")
        agv3Rot.set(agv3Rot.get() + ' ' + '[' + r_x_val.get() + ',' + r_y_val.get() + ',' + r_z_val.get() + ']')
    if agv_id.get() == 'agv4':
        agv4ProdTypes.set(agv4ProdTypes.get() + ' ' + product_type.get())
        agv4Coords.set(agv4Coords.get() + ' ' + "[" + x_val.get() + ',' + y_val.get() + ',' + z_val.get() + "]")
        agv4Rot.set(agv4Rot.get() + ' ' + '[' + r_x_val.get() + ',' + r_y_val.get() + ',' + r_z_val.get() + ']')


def new_order():  # this menu pops up to make a new order for the user
    orderCount.append(0)
    print(len(orderCount))
    add_order = tk.Toplevel()
    temp_priority = tk.StringVar()
    temp_priority.set('1')
    temp_k_health = tk.StringVar()
    temp_k_health.set('1')
    temp_a_health = tk.StringVar()
    temp_a_health.set('1')
    temp_announcement_cond = tk.StringVar()
    temp_announcement_cond.set('time')
    temp_ann_val = tk.StringVar()
    temp_ann_val.set('0')
    if len(orderCount) > 1:
        get_priority_label = tk.Label(add_order, text="Enter the priority of the order")
        get_priority_label.pack()
        get_priority = tk.Entry(add_order, textvariable=temp_priority)
        get_priority.pack()
    get_k_health_label = tk.Label(add_order, text="Select the kitting health of the order")
    get_k_health_label.pack()
    get_k_health = tk.OptionMenu(add_order, temp_k_health, "0", "1")
    get_k_health.pack()
    get_a_health_label = tk.Label(add_order, text="Select the assembly health of the order")
    get_a_health_label.pack()
    get_a_health = tk.OptionMenu(add_order, temp_a_health, "0", "1")
    get_a_health.pack()
    if len(orderCount) > 1:
        get_announcement_condition_label = tk.Label(add_order, text="Enter the announcement condition of the order")
        get_announcement_condition_label.pack()
        get_announcement_condition = tk.Entry(add_order, textvariable=temp_announcement_cond)
        get_announcement_condition.pack()
    get_ann_val_label = tk.Label(add_order, text="Enter the announcement value of the order")
    get_ann_val_label.pack()
    get_ann_val = tk.Entry(add_order, textvariable=temp_ann_val)
    get_ann_val.pack()
    order_kitting = tk.Button(add_order, text="Kitting", command=kitting)
    order_kitting.pack(pady=20)
    order_assembly = tk.Button(add_order, text="Assembly", command=assembly)
    order_assembly.pack(pady=20)
    order_save = tk.Button(add_order, text="Save and Exit", command=add_order.destroy)
    order_save.pack(pady=20)
    add_order.mainloop()
    if len(orderCount) == 1:
        allOrders.append(Order('1', temp_k_health.get(), temp_a_health.get(),
                               "time", temp_ann_val.get(), tempKits, tempAssemb))
    else:
        allOrders.append(Order(temp_priority.get(), temp_k_health.get(), temp_a_health.get(),
                               temp_announcement_cond.get(), temp_ann_val.get(), tempKits, tempAssemb))
    if len(tempKits) != 0:  # checks if there are products present to avoid errors
        kProdInd.append(len(tempKits[len(allOrders)-1].products)-1)
    if len(tempAssemb) != 0:
        aProdInd.append(len(tempAssemb[len(allOrders)-1].products)-1)


def update_dest(a, b, c, d, e, f):  # switches the options present based off of the agv selected
    menu = a['menu']
    menu.delete(0, 'end')
    if b.get() == '[agv1]':
        c.set(kAgv1List[0])
        for dest in kAgv1List:
            menu.add_command(label=dest, command=lambda dest=dest: c.set(dest))
    elif b.get() == '[agv2]':
        c.set(kAgv2List[0])
        for dest in kAgv2List:
            menu.add_command(label=dest, command=lambda dest=dest: c.set(dest))
    elif b.get() == '[agv3]':
        c.set(kAgv3List[0])
        for dest in kAgv3List:
            menu.add_command(label=dest, command=lambda dest=dest: c.set(dest))
    else:
        c.set(kAgv4List[0])
        for dest in kAgv4List:
            menu.add_command(label=dest, command=lambda dest=dest: c.set(dest))


def kitting():  # allows the user to add kitting to an order
    kitting_wind = tk.Toplevel()
    ship_count = tk.StringVar()
    ship_count.set('1')
    trays = tk.StringVar()
    trays.set('[movable_tray_metal_rusty]')
    k_agv = tk.StringVar()
    k_agv.set('[agv1]')
    k_destination = tk.StringVar()
    k_destination.set('[ks1]')  # list of as choices
    k_ship_count = tk.Label(kitting_wind, text="Enter the shipping count")
    k_ship_count.pack()
    ship_count_menu = tk.OptionMenu(kitting_wind, ship_count, "1", "2")
    ship_count_menu.pack()
    k_trays = tk.Label(kitting_wind, text="Kitting Trays")
    k_trays.pack()
    get_tray = tk.OptionMenu(kitting_wind, trays, *trayTypes)
    get_tray.pack()
    k_agv_label = tk.Label(kitting_wind, text="Enter the Kitting agv")
    k_agv_label.pack()
    get_agv = tk.OptionMenu(kitting_wind, k_agv, "[agv1]", "[agv2]", "[agv3]", "[agv4]")
    get_agv.pack()
    k_dest_label = tk.Label(kitting_wind, text="Enter the Kitting destination")
    k_dest_label.pack()
    get_k_dest = tk.OptionMenu(kitting_wind, k_destination, *agv1List)
    get_k_dest.pack()
    add_k_products = tk.Button(kitting_wind, text="Add Product", command=get_k_products)
    add_k_products.pack(pady=20)
    order_kitting = tk.Button(kitting_wind, text="Save and Exit", command=kitting_wind.destroy)
    order_kitting.pack(pady=20)
    update_with_arg = partial(update_dest, get_k_dest, k_agv, k_destination)
    k_agv.trace('w', update_with_arg)
    kitting_wind.mainloop()
    tempKits.append(Kitting(ship_count.get(), trays.get(), k_agv.get(), k_destination.get(), kitProds))


def get_k_products():  # adds a product to kitting
    temp_pid = "part_100"
    k_products = tk.Toplevel()
    x_val_k = tk.StringVar()
    x_val_k.set('0')
    y_val_k = tk.StringVar()
    y_val_k.set('0')
    z_val_k = tk.StringVar()
    z_val_k.set('0')
    r_x_val_k = tk.StringVar()
    r_x_val_k.set('0')
    r_y_val_k = tk.StringVar()
    r_y_val_k.set('0')
    r_z_val_k = tk.StringVar()
    r_z_val_k.set('0')
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
    r_x_val_k_label = tk.Label(k_products, text="Enter the x rotation value")
    r_x_val_k_label.pack()
    r_x_val_k_entry = tk.Entry(k_products, textvariable=r_x_val_k)
    r_x_val_k_entry.pack()
    r_y_val_k_label = tk.Label(k_products, text="Enter the y rotation value")
    r_y_val_k_label.pack()
    r_y_val_k_entry = tk.Entry(k_products, textvariable=r_y_val_k)
    r_y_val_k_entry.pack()
    r_z_val_k_label = tk.Label(k_products, text="Enter the z rotation value")
    r_z_val_k_label.pack()
    r_z_val_k_entry = tk.Entry(k_products, textvariable=r_z_val_k)
    r_z_val_k_entry.pack()
    kitting_prod_exit = tk.Button(k_products, text="Save and Exit", command=k_products.destroy)
    kitting_prod_exit.pack(pady=20)
    k_products.mainloop()
    kitProds.append(Products(temp_pid, k_product_info.get(),
                             str("["+x_val_k.get()+", "+y_val_k.get()+', '+z_val_k.get()+"]"),
                             str("["+r_x_val_k.get()+", "+r_y_val_k.get()+", "+z_val_k.get()+"]")))


def assembly():  # adds assembly to an order
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
    order_assemb = tk.Button(assemb_wind, text="Save and Exit", command=assemb_wind.destroy)
    order_assemb.pack(pady=20)
    assemb_wind.mainloop()
    tempAssemb.append(Assembly(a_ship_count.get(), a_stations.get(), assembProds))


def get_a_products():  # adds a product to assembly
    temp_pid = "part_100"
    a_products = tk.Toplevel()
    x_val_a = tk.StringVar()
    x_val_a.set('0')
    y_val_a = tk.StringVar()
    y_val_a.set('0')
    z_val_a = tk.StringVar()
    z_val_a.set('0')
    r_x_val_a = tk.StringVar()
    r_x_val_a.set('0')
    r_y_val_a = tk.StringVar()
    r_y_val_a.set('0')
    r_z_val_a = tk.StringVar()
    r_z_val_a.set('0')
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
    r_x_val_a_label = tk.Label(a_products, text="Enter the x rotation value")
    r_x_val_a_label.pack()
    r_x_val_a_entry = tk.Entry(a_products, textvariable=r_x_val_a)
    r_x_val_a_entry.pack()
    r_y_val_a_label = tk.Label(a_products, text="Enter the y rotation value")
    r_y_val_a_label.pack()
    r_y_val_a_entry = tk.Entry(a_products, textvariable=r_y_val_a)
    r_y_val_a_entry.pack()
    r_z_val_a_label = tk.Label(a_products, text="Enter the z rotation value")
    r_z_val_a_label.pack()
    r_z_val_a_entry = tk.Entry(a_products, textvariable=r_z_val_a)
    r_z_val_a_entry.pack()
    assemb_prod_exit = tk.Button(a_products, text="Save and Exit", command=a_products.destroy)
    assemb_prod_exit.pack(pady=20)
    a_products.mainloop()
    assembProds.append(Products(temp_pid, a_product_info.get(),
                       str("[" + x_val_a.get() + ", " + y_val_a.get() + ', ' + z_val_a.get() + "]"),
                       str("[" + r_x_val_a.get() + ", " + r_y_val_a.get() + ", " + z_val_a.get() + "]")))


def add_bin():  # adds a bin for models over bins
    add_bin_wind = tk.Toplevel()
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
    r_x_val_b = tk.StringVar()
    r_x_val_b.set('0')
    r_y_val_b = tk.StringVar()
    r_y_val_b.set('0')
    r_z_val_b = tk.StringVar()
    r_z_val_b.set('0')
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
    r_x_val_b_label = tk.Label(add_bin_wind, text="Enter the x rotation value")
    r_x_val_b_label.pack()
    r_x_val_b_entry = tk.Entry(add_bin_wind, textvariable=r_x_val_b)
    r_x_val_b_entry.pack()
    r_y_val_b_label = tk.Label(add_bin_wind, text="Enter the y rotation value")
    r_y_val_b_label.pack()
    r_y_val_b_entry = tk.Entry(add_bin_wind, textvariable=r_y_val_b)
    r_y_val_b_entry.pack()
    r_z_val_b_label = tk.Label(add_bin_wind, text="Enter the z rotation value")
    r_z_val_b_label.pack()
    r_z_val_b_entry = tk.Entry(add_bin_wind, textvariable=r_z_val_b)
    r_z_val_b_entry.pack()
    b_dim_label = tk.Label(add_bin_wind, text="Select the dimensions for the bin")
    b_dim_label.pack()
    b_dim_menu = tk.OptionMenu(add_bin_wind, dim, '2x2', '3x3')
    b_dim_menu.pack()
    add_bin_exit = tk.Button(add_bin_wind, text="Save and Exit", command=add_bin_wind.destroy)
    add_bin_exit.pack(pady=20)
    add_bin_wind.mainloop()
    width = '2'
    if dim.get() == '3x3':
        width = '3'
    modelsOverBinsInfo.append(ModelOverBin(bin_num.get(), bin_prod.get(),
                                           str("["+x_val_s.get()+", "+y_val_s.get()+", "+z_val_s.get()+"]"),
                                           str("["+x_val_e.get()+", "+y_val_e.get()+", "+z_val_e.get()+"]"),
                                           str("["+r_x_val_b.get()+", "+r_y_val_b.get()+", "+r_z_val_b.get()+"]"),
                                           width, width))


def add_station():  # adds a station to models over stations
    add_station_wind = tk.Toplevel()
    x_val_stat = tk.StringVar()
    x_val_stat.set('0')
    y_val_stat = tk.StringVar()
    y_val_stat.set('0')
    z_val_stat = tk.StringVar()
    z_val_stat.set('0')
    r_x_val_stat = tk.StringVar()
    r_x_val_stat.set('0')
    r_y_val_stat = tk.StringVar()
    r_y_val_stat.set('0')
    r_z_val_stat = tk.StringVar()
    r_z_val_stat.set('0')
    station = tk.StringVar()
    station.set(allStations[0])
    stat_prod = tk.StringVar()
    stat_prod.set(prodList[0])
    station_label = tk.Label(add_station_wind, text="Select the statijon")
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
    r_x_val_stat_label = tk.Label(add_station_wind, text="Enter the x rotation value")
    r_x_val_stat_label.pack()
    r_x_val_stat_entry = tk.Entry(add_station_wind, textvariable=r_x_val_stat)
    r_x_val_stat_entry.pack()
    r_y_val_stat_label = tk.Label(add_station_wind, text="Enter the y rotation value")
    r_y_val_stat_label.pack()
    r_y_val_stat_entry = tk.Entry(add_station_wind, textvariable=r_y_val_stat)
    r_y_val_stat_entry.pack()
    r_z_val_stat_label = tk.Label(add_station_wind, text="Enter the z rotation value")
    r_z_val_stat_label.pack()
    r_z_val_stat_entry = tk.Entry(add_station_wind, textvariable=r_z_val_stat)
    r_z_val_stat_entry.pack()
    add_stat_exit = tk.Button(add_station_wind, text="Save and Exit", command=add_station_wind.destroy)
    add_stat_exit.pack(pady=20)
    add_station_wind.mainloop()
    modelsOverStationsInfo.append(ModelOverStation(station.get(), stat_prod.get(),
                                                   str("["+x_val_stat.get()+", "+y_val_stat.get() +
                                                       ", "+z_val_stat.get()+"]"),
                                                   str("["+r_x_val_stat.get()+", "+r_y_val_stat.get() +
                                                       ", "+r_z_val_stat.get()+"]")))


def add_belt():  # adds a belt to belt models
    add_belt_wind = tk.Toplevel()
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
    r_x_val_belt = tk.StringVar()
    r_x_val_belt.set('0')
    r_y_val_belt = tk.StringVar()
    r_y_val_belt.set('0')
    r_z_val_belt = tk.StringVar()
    r_z_val_belt.set('0')
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
    r_x_val_belt_label = tk.Label(add_belt_wind, text="Enter the x rotation value")
    r_x_val_belt_label.pack()
    r_x_val_belt_entry = tk.Entry(add_belt_wind, textvariable=r_x_val_belt)
    r_x_val_belt_entry.pack()
    r_y_val_belt_label = tk.Label(add_belt_wind, text="Enter the y rotation value")
    r_y_val_belt_label.pack()
    r_y_val_belt_entry = tk.Entry(add_belt_wind, textvariable=r_y_val_belt)
    r_y_val_belt_entry.pack()
    r_z_val_belt_label = tk.Label(add_belt_wind, text="Enter the z rotation value")
    r_z_val_belt_label.pack()
    r_z_val_belt_entry = tk.Entry(add_belt_wind, textvariable=r_z_val_belt)
    r_z_val_belt_entry.pack()
    belt_save = tk.Button(add_belt_wind, text="Save and Exit", command=add_belt_wind.destroy)
    belt_save.pack(pady=20)
    add_belt_wind.mainloop()
    beltCycleInfo.append(BeltCycle(belt_prod.get(), belt_time.get(),
                                   str("["+x_val_belt.get()+", "+y_val_belt.get()+", "+z_val_belt.get()+"]"),
                                   str("["+r_x_val_belt.get()+", "+r_y_val_belt.get()+", "+r_z_val_belt.get()+"]")))


def cancel_file():  # cancels the program from the file name menu
    cancelFlag.set('1')
    getFileName.destroy()


def cancel_options():  # cancels the program from the options menu
    cancelFlag.set('1')
    options.destroy()


def cancel_tray():  # cancels the program from the table tray menu
    cancelFlag.set('1')
    trayInfo.destroy()


def cancel_agv():  # cancels the program from the agv menu
    cancelFlag.set('1')
    agvInfo.destroy()


def cancel_orders():  # cancels the program from the orders menu
    cancelFlag.set('1')
    ordersInfo.destroy()


def cancel_over_bins():  # cancels the program from the models over bins menu
    cancelFlag.set('1')
    overBinsWind.destroy()


def cancel_over_stations():  # cancels the program from the models over stations menu
    cancelFlag.set('1')
    overStationsWind.destroy()


def cancel_belt_cycles():  # cancels the program from the belt models menu
    cancelFlag.set('1')
    beltCyclesWind.destroy()


class Order:  # for organizing the data from the order menu
    def __init__(self, priority, k_health, a_health, an_cond, cond_val, kit_info, assem_info):
        self.priority = priority
        self.kittingHealth = k_health
        self.assemblyHealth = a_health
        self.announcementCondition = an_cond
        self.conditionValue = cond_val
        self.kitting = kit_info
        self.assembly = assem_info


class Kitting:  # for organizing the data from the kitting menu
    def __init__(self, ship_count, trays, agvs, destinations, products):
        self.shipmentCount = ship_count
        self.trays = trays
        self.agvs = agvs
        self.destinations = destinations
        self.products = products


class Assembly:  # for organizing the data from the assembly menu
    def __init__(self, ship_count, stations, products):
        self.shipmentCount = ship_count
        self.stations = stations
        self.products = products


class Products:  # for organizing the data for all products
    def __init__(self, pid, p_type, xyz, rpy):
        self.id = pid
        self.pType = p_type
        self.xyz = xyz
        self.rpy = rpy


class ModelOverBin:  # for organizing the data from the models over bins menu
    def __init__(self, bin_num, prod, start, end, rpy, num_mod_x, num_mod_y):
        self.binNum = bin_num
        self.product = prod
        self.xyz_start = start
        self.xyz_end = end
        self.rpy = rpy
        self.num_mod_x = num_mod_x
        self.num_mod_y = num_mod_y


class ModelOverStation:  # for organizing the data from the models over stations menu
    def __init__(self, station, part, xyz, rpy):
        self.station = station
        self.part = part
        self.xyz = xyz
        self.rpy = rpy


class BeltCycle:  # for organizing the data from the belt models menu
    def __init__(self, part, time, xyz, rpy):
        self.part = part
        self.time = time
        self.xyz = xyz
        self.rpy = rpy


if __name__ == "__main__":
    getFileName = tk.Tk()
    cancelFlag = tk.StringVar()
    cancelFlag.set('0')
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
    cancelFile = tk.Button(getFileName, text="Cancel", command=cancel_file)
    cancelFile.pack(pady=20)
    getFileName.mainloop()
    if cancelFlag.get() == '1':
        quit()
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
    beltCycles = tk.StringVar()
    beltCycles.set("0")
    popCycleLabel = tk.Label(options, text="Enter the belt population cycles (enter none to skip):")
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
    cancelOptions = tk.Button(options, text="Cancel", command=cancel_options)
    cancelOptions.pack(pady=20)
    options.mainloop()
    saveFileName = fileName.get()
    if '.yaml' not in saveFileName:
        saveFileName += '.yaml'
    with open(saveFileName, "a") as o:
        o.write("options:\n")
        if overBins.get() != 'none':
            o.write("\tinsert_models_over_bins: " + overBins.get() + "\n")
        if beltCycles.get() != 'none':
            o.write("\tbelt_population_cycles: " + beltCycles.get() + "\n")
        if overStations.get() != 'none':
            o.write("\tinsert_models_over_stations: " + overStations.get() + "\n")
        if stateLogging.get() != 'none':
            o.write("\tgazebo_state_logging: " + stateLogging.get() + "\n")
        o.write("\t# mandatory: gripper_tray or gripper_part\n")
        o.write("\tcurrent_gripper_type: " + gripperType.get() + "\n")
        o.write("time_limit: " + timeLimit.get() + "\n")
    if cancelFlag.get() == '1':
        if path.exists(fileName.get()):
            os.remove(fileName.get())
        elif path.exists(fileName.get() + '.yaml'):
            os.remove(fileName.get() + '.yaml')
        quit()
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
    skipFlag = tk.StringVar()
    skipFlag.set("0")
    skipButton = tk.Button(trayInfo, text="Skip", command=tray_skip)
    skipButton.pack()
    cancelTray = tk.Button(trayInfo, text="Cancel", command=cancel_tray)
    cancelTray.pack()
    trayInfo.mainloop()
    if skipFlag.get() == "0":
        with open(saveFileName, "a") as o:
            if (table1.get() != "" and table1q.get() != "") or (table2.get() != "" and table2q.get() != ""):
                o.write("\n\n\ntable_tray_infos:\n")
            if table1.get() != "" and table1q.get() != "":
                o.write("\ttable_1:\n")
                o.write("\t\ttray_model: " + table1.get() + "\n")
                o.write("\t\tquantity: " + table1q.get() + "\n")
            if table2.get() != "" and table2q.get() != "":
                o.write("\ttable_2:\n")
                o.write("\t\ttray_model: " + table2.get() + "\n")
                o.write("\t\tquantity: " + table2q.get() + "\n")
    if cancelFlag.get() == '1':
        if path.exists(fileName.get()):
            os.remove(fileName.get())
        elif path.exists(fileName.get() + '.yaml'):
            os.remove(fileName.get() + '.yaml')
        quit()
    # END OF TABLE MENUS
    # -----------------------------------------------------------------------------------
    # BEGINNING OF GETTING AGV_INFOS
    agvInfo = tk.Tk()
    agvInfo.title("AGV Information")
    agv1 = tk.StringVar()
    agv1.set("ks1")
    agv1Label = tk.Label(agvInfo, text="AGV1 Location:")
    agv1Label.pack()
    agv1Menu = tk.OptionMenu(agvInfo, agv1, *agv1List)
    agv1Menu.pack()
    agv1ProdTypes = tk.StringVar()
    agv1ProdTypes.set('')
    agv1Coords = tk.StringVar()
    agv1Coords.set('')
    agv1Rot = tk.StringVar()
    agv1Rot.set('')
    agv2 = tk.StringVar()
    agv2.set("ks2")
    agv2Label = tk.Label(agvInfo, text="AGV2 Location:")
    agv2Label.pack()
    agv2Menu = tk.OptionMenu(agvInfo, agv2, *agv2List)
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
    agv3Menu = tk.OptionMenu(agvInfo, agv3, *agv3List)
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
    agv4Menu = tk.OptionMenu(agvInfo, agv4, *agv4List)
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
    cancelAgv = tk.Button(agvInfo, text="Cancel", command=cancel_agv)
    cancelAgv.pack(pady=20)
    agvInfo.mainloop()
    partID = 0
    index = 0
    agv1Prod = []
    agv2Prod = []
    agv3Prod = []
    agv4Prod = []
    agv1CArr = agv1Coords.get().split(" ")
    agv2CArr = agv2Coords.get().split(" ")
    agv3CArr = agv3Coords.get().split(" ")
    agv4CArr = agv4Coords.get().split(" ")
    agv1CArr.reverse()
    agv2CArr.reverse()
    agv3CArr.reverse()
    agv4CArr.reverse()
    agv1RArr = agv1Rot.get().split(' ')
    agv2RArr = agv2Rot.get().split(' ')
    agv3RArr = agv3Rot.get().split(' ')
    agv4RArr = agv4Rot.get().split(' ')
    agv1RArr.reverse()
    agv2RArr.reverse()
    agv3RArr.reverse()
    agv4RArr.reverse()
    agv1Types = agv1ProdTypes.get().split(' ')
    agv2Types = agv2ProdTypes.get().split(' ')
    agv3Types = agv3ProdTypes.get().split(' ')
    agv4Types = agv4ProdTypes.get().split(' ')
    agv1Types.reverse()
    agv2Types.reverse()
    agv3Types.reverse()
    agv4Types.reverse()
    with open(saveFileName, "a") as o:
        o.write("\n\nagv_infos:\n")
        o.write("\tagv1:\n")
        o.write("\t\tlocation: " + agv1.get() + "\n")
        if len(agv1ProdTypes.get()) != 0:
            o.write("\t\tproducts:\n")
            for i in agv1Types:
                if i != '':
                    o.write("\t\t\tpart_" + str(partID) + ":\n")
                    tempID = "part_" + str(partID)
                    o.write("\t\t\t\ttype: " + i + "\n")
                    o.write("\t\t\t\tpose: \n")
                    o.write("\t\t\t\t\txyz: " + agv1CArr[index] + "\n")
                    o.write("\t\t\t\t\trpy: " + agv1RArr[index] + "\n")
                    partID += 1
                    agv1Prod.append(Products(tempID, i, agv1CArr[index], agv1RArr[index]))
                    index += 1
        index = 0
        o.write("\tagv2:\n")
        o.write("\t\tlocation: " + agv2.get() + "\n")
        if len(agv2ProdTypes.get()) != 0:
            o.write("\t\tproducts:\n")
            for i in agv2Types:
                if i != '':
                    o.write("\t\t\tpart_" + str(partID) + ":\n")
                    tempID = "part_" + str(partID)
                    o.write("\t\t\t\ttype: " + i + "\n")
                    o.write("\t\t\t\tpose: \n")
                    o.write("\t\t\t\t\txyz: " + agv2CArr[index] + "\n")
                    o.write("\t\t\t\t\trpy: " + agv2RArr[index] + "\n")
                    partID += 1
                    agv2Prod.append(Products(tempID, i, agv2CArr[index], agv2RArr[index]))
                    index += 1
        index = 0
        o.write("\tagv3:\n")
        o.write("\t\tlocation: " + agv3.get() + "\n")
        if len(agv3ProdTypes.get()) != 0:
            o.write("\t\tproducts:\n")
            for i in agv3Types:
                if i != '':
                    o.write("\t\t\tpart_" + str(partID) + ":\n")
                    tempID = "part_" + str(partID)
                    o.write("\t\t\t\ttype: " + i + "\n")
                    o.write("\t\t\t\tpose: \n")
                    o.write("\t\t\t\t\txyz: " + agv3CArr[index] + "\n")
                    o.write("\t\t\t\t\trpy: " + agv3RArr[index] + "\n")
                    partID += 1
                    agv3Prod.append(Products(tempID, i, agv3CArr[index], agv3RArr[index]))
                    index += 1
        index = 0
        o.write("\tagv4:\n")
        o.write("\t\tlocation: " + agv4.get() + "\n")
        if len(agv4ProdTypes.get()) != 0:
            o.write("\t\tproducts:\n")
            for i in agv4Types:
                if i != '':
                    o.write("\t\t\tpart_" + str(partID) + ":\n")
                    tempID = "part_" + str(partID)
                    o.write("\t\t\t\ttype: " + i + "\n")
                    o.write("\t\t\t\tpose: \n")
                    o.write("\t\t\t\t\txyz: " + agv4CArr[index] + "\n")
                    o.write("\t\t\t\t\trpy: " + agv4RArr[index] + "\n")
                    partID += 1
                    agv4Prod.append(Products(tempID, i, agv4CArr[index], agv4RArr[index]))
                    index += 1
    if cancelFlag.get() == '1':
        if path.exists(fileName.get()):
            os.remove(fileName.get())
        elif path.exists(fileName.get() + '.yaml'):
            os.remove(fileName.get() + '.yaml')
        quit()
    allProd = []
    for i in agv1Prod:
        allProd.append(i)
    for i in agv2Prod:
        allProd.append(i)
    for i in agv3Prod:
        allProd.append(i)
    for i in agv4Prod:
        allProd.append(i)
    # END OF AGV OPTIONS
    # ----------------------------------------------------------------------------------------------------------------------
    # BEGINNING OF ORDERS
    orderID = 0
    ordersInfo = tk.Tk()
    allOrders = []
    ordersInfo.title("Orders Information")
    newOrder = tk.Button(ordersInfo, text="New Order", command=new_order)
    newOrder.pack(pady=20)
    ordersNext = tk.Button(ordersInfo, text="Next", command=ordersInfo.destroy)
    ordersNext.pack(pady=20)
    cancelOrders = tk.Button(ordersInfo, text="Cancel", command=cancel_orders)
    cancelOrders.pack(pady=20)
    ordersInfo.mainloop()
    allOrders.reverse()
    partC = 0
    if cancelFlag.get() == '1':
        if path.exists(fileName.get()):
            os.remove(fileName.get())
        elif path.exists(fileName.get() + '.yaml'):
            os.remove(fileName.get() + '.yaml')
        quit()
    with open(saveFileName, "a") as o:
        if len(allOrders) > 0:
            o.write("\n\norders:\n")
            for i in allOrders:
                o.write("\torder_"+str(orderID)+":\n")
                o.write("\t\tpriority: " + i.priority+"\n")
                o.write("\t\tkitting_robot_health: " + i.kittingHealth+"\n")
                o.write("\t\tassembly_robot_health: " + i.assemblyHealth+"\n")
                o.write("\t\tannouncement_condition: " + i.announcementCondition+"\n")
                o.write("\t\tannouncement_condition_value: "+i.conditionValue+"\n")
                if len(i.kitting) != 0:
                    o.write("\t\tkitting:\n")
                    o.write("\t\t\tshipment_count: " + i.kitting[orderInd].shipmentCount + "\n")
                    o.write("\t\t\ttrays: " + i.kitting[orderInd].trays + "\n")
                    o.write("\t\t\tagvs: " + i.kitting[orderInd].agvs + "\n")
                    o.write("\t\t\tdestinations: " + i.kitting[orderInd].destinations + "\n")
                    o.write("\t\t\tproducts:\n")
                    if len(kProdInd)-1 == orderInd:
                        for k in i.kitting[orderInd].products[kProdInd[orderInd]:]:
                            o.write("\t\t\t\tpart_" + str(partC) + ":\n")
                            partC += 1
                            o.write("\t\t\t\t\ttype: " + k.pType + "\n")
                            o.write("\t\t\t\t\tpose:\n")
                            o.write("\t\t\t\t\t\txyz: " + k.xyz + "\n")
                            o.write("\t\t\t\t\t\trpy: " + k.rpy + "\n")
                    else:
                        for k in i.kitting[orderInd].products[kProdInd[orderInd]: kProdInd[orderInd + 1]]:
                            o.write("\t\t\t\tpart_" + str(partC) + ":\n")
                            partC += 1
                            o.write("\t\t\t\t\ttype: " + k.pType + "\n")
                            o.write("\t\t\t\t\tpose:\n")
                            o.write("\t\t\t\t\t\txyz: " + k.xyz + "\n")
                            o.write("\t\t\t\t\t\trpy: " + k.rpy + "\n")
                if len(i.assembly) != 0:
                    o.write("\t\tassembly:\n")
                    o.write("\t\t\tshipment_count: " + i.assembly[orderInd].shipmentCount + '\n')
                    o.write("\t\t\tstations: " + i.assembly[orderInd].stations + '\n')
                    o.write("\t\t\tproducts:\n")
                    if len(aProdInd)-1 == orderInd:
                        for k in i.assembly[orderInd].products[aProdInd[orderInd]:]:
                            o.write("\t\t\t\t part_" + str(partC) + ":\n")
                            partC += 1
                            o.write("\t\t\t\t\ttype: " + k.pType + "\n")
                            o.write("\t\t\t\t\tpose:\n")
                            o.write("\t\t\t\t\t\txyz: " + k.xyz + "\n")
                            o.write("\t\t\t\t\t\trpy: " + k.rpy + "\n")
                    else:
                        for k in i.assembly[orderInd].products[aProdInd[orderInd]: aProdInd[orderInd+1]]:
                            o.write("\t\t\t\tpart_" + str(partC) + ":\n")
                            partC += 1
                            o.write("\t\t\t\t\ttype: " + k.pType + "\n")
                            o.write("\t\t\t\t\tpose:\n")
                            o.write("\t\t\t\t\t\txyz: " + k.xyz + "\n")
                            o.write("\t\t\t\t\t\trpy: " + k.rpy + "\n")
                orderID += 1
            o.write("\n")
    # END OF ORDERS
    # ----------------------------------------------------------------------------------------------------------------------
    # BEGINNING OF MODELS OVER BINS
    if overBins.get() == 'true':
        overBinsWind = tk.Tk()
        addBinButton = tk.Button(overBinsWind, text="Add bin", command=add_bin)
        addBinButton.pack(pady=20)
        overBinsNext = tk.Button(overBinsWind, text="Next", command=overBinsWind.destroy)
        overBinsNext.pack(pady=20)
        cancelOverBins = tk.Button(overBinsWind, text="Cancel", command=cancel_over_bins)
        cancelOverBins.pack(pady=20)
        overBinsWind.mainloop()
        if cancelFlag.get() == '1':
            if path.exists(fileName.get()):
                os.remove(fileName.get())
            elif path.exists(fileName.get() + '.yaml'):
                os.remove(fileName.get() + '.yaml')
            quit()
        if len(modelsOverBinsInfo) > 0:
            modelsOverBinsInfo.reverse()
            with open(saveFileName, "a") as o:
                o.write("\nmodels_over_bins:\n")
                for i in modelsOverBinsInfo:
                    o.write("\t"+i.binNum+":\n")
                    o.write("\t\tmodels:\n")
                    o.write("\t\t\t"+i.product+":\n")
                    o.write("\t\t\t\txyz_start: "+i.xyz_start+"\n")
                    o.write("\t\t\t\txyz_end: "+i.xyz_end+"\n")
                    o.write("\t\t\t\trpy: "+i.rpy+"\n")
                    o.write("\t\t\t\tnum_models_x: "+i.num_mod_x+"\n")
                    o.write("\t\t\t\tnum_models_y: "+i.num_mod_y+"\n")
                o.write("\n")
    # END OF MODELS OVER BINS
    # ----------------------------------------------------------------------------------------------------------------------
    # BEGINNING OF MODELS OVER STATIONS
    if overStations.get() == 'true':
        overStationsWind = tk.Tk()
        addStationButton = tk.Button(overStationsWind, text="Add station", command=add_station)
        addStationButton.pack(pady=20)
        overStationsNext = tk.Button(overStationsWind, text="Next", command=overStationsWind.destroy)
        overStationsNext.pack(pady=20)
        cancelOverStations = tk.Button(overStationsWind, text="Cancel", command=cancel_over_stations)
        cancelOverStations.pack(pady=20)
        overStationsWind.mainloop()
        if cancelFlag.get() == '1':
            if path.exists(fileName.get()):
                os.remove(fileName.get())
            elif path.exists(fileName.get() + '.yaml'):
                os.remove(fileName.get() + '.yaml')
            quit()
        if len(modelsOverStationsInfo) > 0:
            modelsOverStationsInfo.reverse()
            with open(saveFileName, "a") as o:
                o.write("\nmodels_over_stations:\n")
                for i in modelsOverStationsInfo:
                    o.write("\t"+i.station+":\n")
                    o.write("\t\tmodels:\n")
                    o.write("\t\t\t"+i.part+":\n")
                    o.write("\t\t\t\txyz: "+i.xyz+"\n")
                    o.write("\t\t\t\trpy: "+i.rpy+"\n")
                o.write("\n")
    # END OF MODELS OVER STATIONS
    # ----------------------------------------------------------------------------------------------------------------------
    # BEGINNING OF BELT MODELS
    if beltCycles.get() != '0':
        beltCyclesWind = tk.Tk()
        addBeltCycle = tk.Button(beltCyclesWind, text="Add belt cycle", command=add_belt)
        addBeltCycle.pack(pady=20)
        beltCycleNext = tk.Button(beltCyclesWind, text="Next", command=beltCyclesWind.destroy)
        beltCycleNext.pack(pady=20)
        cancelBeltCycle = tk.Button(beltCyclesWind, text="Cancel", command=cancel_belt_cycles)
        cancelBeltCycle.pack(pady=20)
        beltCyclesWind.mainloop()
        if cancelFlag.get() == '1':
            if path.exists(fileName.get()):
                os.remove(fileName.get())
            elif path.exists(fileName.get() + '.yaml'):
                os.remove(fileName.get() + '.yaml')
            quit()
        if len(beltCycleInfo) > 0:
            beltCycleInfo.reverse()
            with open(saveFileName, "a") as o:
                o.write("\nbelt_models:\n")
                for i in beltCycleInfo:
                    o.write("\t"+i.part+":\n")
                    o.write("\t\t"+i.time+":\n")
                    o.write("\t\t\tpose:\n")
                    o.write("\t\t\t\txyz: "+i.xyz+"\n")
                    o.write("\t\t\t\trpy: "+i.rpy+"\n")
                o.write("\n")
