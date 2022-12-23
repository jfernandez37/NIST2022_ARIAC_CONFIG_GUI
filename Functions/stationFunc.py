import tkinter as tk
from Functions.allClasses import ModelOverStation
from Functions.validationFunc import *
from functools import partial
from Functions.checkCancel import cancel_func
prodList = ["assembly_battery_red", "assembly_battery_green",
            "assembly_battery_blue", "assembly_pump_red", "assembly_pump_green",
            "assembly_pump_blue", "assembly_regulator_red",
            "assembly_regulator_green", "assembly_regulator_blue", "assembly_sensor_red",
            "assembly_sensor_green", "assembly_sensor_blue"]  # list of all parts
allStations = ['ks1', 'ks2', 'ks3', 'ks4', 'as1', 'as2', 'as3', 'as4']  # list of all locations
def add_station(modelsOverStationsInfo):  # adds a station to models over stations
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
    x_val_stat_num_func=partial(require_num, x_val_stat)
    x_val_stat.trace('w', x_val_stat_num_func)
    y_val_stat_num_func=partial(require_num, y_val_stat)
    y_val_stat.trace('w', y_val_stat_num_func)
    z_val_stat_num_func=partial(require_num, z_val_stat)
    z_val_stat.trace('w', z_val_stat_num_func)
    check_rpy = partial(rpy_validation, r_val_stat, p_val_stat, y_rpy_val_stat, add_stat_exit)
    r_val_stat.trace('w', check_rpy)
    p_val_stat.trace('w', check_rpy)
    y_rpy_val_stat.trace('w', check_rpy)
    add_station_wind.mainloop()
    add_quotes(r_val_stat)
    add_quotes(p_val_stat)
    add_quotes(y_rpy_val_stat)
    if cancel_station_flag.get()=="0":
        modelsOverStationsInfo.append(ModelOverStation(station.get(), stat_prod.get(),
                                                    str("["+x_val_stat.get()+", "+y_val_stat.get() +
                                                        ", "+z_val_stat.get()+"]"),
                                                    str("["+r_val_stat.get()+", "+p_val_stat.get() +
                                                        ", "+y_rpy_val_stat.get()+"]")))