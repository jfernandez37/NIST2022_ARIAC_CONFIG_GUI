import tkinter as tk
from functools import partial
from Functions.allClasses import *
from Functions.buttonFuncs import *
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
def assembly(orderFlag,assembProdsFlag,assembFlag, assembProds, tempAssemb, tempKits):  # adds assembly to an order
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
    Id=0
    if len(tempKits)+len(tempAssemb)!=0:
        Id=1
    tempAssemb.append(Assembly(a_ship_count.get(), a_stations.get(), assembProds, Id))


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