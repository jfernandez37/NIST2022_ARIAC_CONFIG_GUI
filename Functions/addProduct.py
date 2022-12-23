import tkinter as tk
from Functions.checkCancel import cancel_func
from Functions.validationFunc import *
from Functions.allClasses import Products
from functools import partial
prodList = ["assembly_battery_red", "assembly_battery_green",
            "assembly_battery_blue", "assembly_pump_red", "assembly_pump_green",
            "assembly_pump_blue", "assembly_regulator_red",
            "assembly_regulator_green", "assembly_regulator_blue", "assembly_sensor_red",
            "assembly_sensor_green", "assembly_sensor_blue"]  # list of all parts
def add_product(agv1Prods, agv2Prods, agv3Prods, agv4Prods):  # adds a product in agv_infos
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
    product_info.geometry("850x600")
    cancel_prod_func = partial(cancel_func, product_info, add_product_cancel_flag)
    cancel_prod_button = tk.Button(product_info, text="Cancel", command=cancel_prod_func)
    cancel_prod_button.pack()
    prod_save = tk.Button(product_info, text="Save and Exit", command=product_info.destroy)
    prod_save.pack(pady=20)
    x_val_num_func=partial(require_num, x_val)
    x_val.trace('w', x_val_num_func)
    y_val_num_func=partial(require_num, y_val)
    y_val.trace('w', y_val_num_func)
    z_val_num_func=partial(require_num, z_val)
    z_val.trace('w', z_val_num_func)
    check_rpy = partial(rpy_validation, r_val, p_val, y_rpy_val, prod_save)
    r_val.trace('w', check_rpy)
    p_val.trace('w', check_rpy)
    y_rpy_val.trace('w', check_rpy)
    product_info.mainloop()
    add_quotes(r_val)
    add_quotes(p_val)
    add_quotes(y_rpy_val)
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