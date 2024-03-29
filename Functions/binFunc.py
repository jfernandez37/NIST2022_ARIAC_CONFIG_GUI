import tkinter as tk
from functools import partial
from Functions.allClasses import ModelOverBin,PresentProducts
from Functions.checkCancel import cancel_func
from Functions.validationFunc import *
prodList = ["assembly_battery_red", "assembly_battery_green",
            "assembly_battery_blue", "assembly_pump_red", "assembly_pump_green",
            "assembly_pump_blue", "assembly_regulator_red",
            "assembly_regulator_green", "assembly_regulator_blue", "assembly_sensor_red",
            "assembly_sensor_green", "assembly_sensor_blue"]  # list of all parts
def add_bin(modelsOverBinsInfo, binProds):  # adds a bin for models over bins
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