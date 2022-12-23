import tkinter as tk
from Functions.checkCancel import *
from functools import partial
from Functions.updateRanges import update_id_range
def add_faulty_prod(binProds, faultyProdList):  # adds a faulty product for the faulty product challenge
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
    update_id_with_arg = partial(update_id_range, prod_id_menu, temp_prod, prod_id, binProds)
    temp_prod.trace('w', update_id_with_arg)
    faulty_prod_window.mainloop()
    if cancel_faulty_flag.get()=="0":
        faultyProdList.append(str(temp_prod.get()+"_"+prod_id.get()))