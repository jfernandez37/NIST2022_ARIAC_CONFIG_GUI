import tkinter as tk
from functools import partial
from Functions.allClasses import *
from Functions.buttonFuncs import *
from Functions.updateRanges import update_dest
from Functions.validationFunc import *
from Functions.checkCancel import exitAndFlag
kAgv1List = ['[ks1]', '[as1]', '[as2]']  # all possible locations for agv1 in the kitting format
prodList = ["assembly_battery_red", "assembly_battery_green",
            "assembly_battery_blue", "assembly_pump_red", "assembly_pump_green",
            "assembly_pump_blue", "assembly_regulator_red",
            "assembly_regulator_green", "assembly_regulator_blue", "assembly_sensor_red",
            "assembly_sensor_green", "assembly_sensor_blue"]  # list of all parts
trayTypes = ["movable_tray_dark_wood", "movable_tray_light_wood",
             "movable_tray_metal_rusty", "movable_tray_metal_shiny"]  # list of all tray types
fkAgv1List = ['[ks1]', '[as1]', '[as2]']  # all possible locations for agv1 in the kitting format
agv1List = ['ks1', 'as1', 'as2']  # all possible locations for agv1
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