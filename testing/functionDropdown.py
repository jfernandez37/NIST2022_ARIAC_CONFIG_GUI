import tkinter as tk
from functools import partial
def updateVal(var, val,a,b,c):
    var.set(val.get())

def runOptionsGui(options, optionVal, option2Val):
    optionWind=tk.Tk()
    option=tk.StringVar()
    option.set(optionVal)
    option2=tk.StringVar()
    option2.set(option2Val)
    menu=tk.OptionMenu(optionWind, option, *options)
    menu.grid(column=1)
    menu2=tk.OptionMenu(optionWind, option2, *options)
    menu2.grid(column=1)
    exit=tk.Button(optionWind, text="Exit", command=optionWind.destroy)
    exit.grid(column=1)
    optionWind.mainloop()
    optionVal=option.get()
    option2Val=option2.get()
    return optionVal, option2Val

def runGui():
    options=[]
    for i in range(5):
        options.append(str(i))
    optionVal=options[0]
    option2Val=options[0]
    while True:
        optionVal,option2Val=runOptionsGui(options,optionVal, option2Val)

if __name__=="__main__":
    runGui()
