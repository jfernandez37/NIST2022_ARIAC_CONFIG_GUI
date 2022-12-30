import random
import string
import tkinter as tk
from Functions.checkCancel import *
from functools import partial
from newFunctions.validationFunctions import *
from newFunctions.newClasses import *
orderTypes=["kitting", "assembly", "combined"]
def generateOrderId(usedId):
    newId=''.join(random.choices(string.ascii_uppercase+string.digits,k=8))
    if newId in usedId:
        while newId in usedId:
            newId=''.join(random.choices(string.ascii_uppercase+string.digits,k=8))
    usedId.append(newId)
    return newId

def addNewOrder(orderCounter):
    orderCounter.append(0)
    newOrderWind=tk.Tk()
    #order type
    orderType=tk.StringVar()
    orderType.set(orderTypes[0])
    orderTypeSelectionLabel=tk.Label(newOrderWind, text="Select the type of order")
    orderTypeSelectionLabel.pack()
    orderTypeSelectionMenu=tk.OptionMenu(newOrderWind, orderType, *orderTypes)
    orderTypeSelectionMenu.pack()
    #announcement
    timeCondition=tk.StringVar()
    timeCondition.set('0')
    timeConditionEntryLabel=tk.Label(newOrderWind, text="Enter the announcement time_condition")
    timeConditionEntryLabel.pack()
    timeConditionEntry=tk.Label(newOrderWind, textvariable=timeCondition)
    timeConditionEntry.pack()
    #order condition
    '''
    
    Filler for order_condition
    
    
    '''
    #Priority
    orderPriority=tk.StringVar()
    orderPriority.set('1')
    orderPriorityCheckBox=tk.Checkbutton(newOrderWind, text="Priority", variable=orderPriority, onvalue="1", offvalue="0", height=1, width=20)
    orderPriorityCheckBox.pack()
    #order challenges
    '''
    
    Challenges
    
    
    '''
    #choose the tasks
    '''
    
    
    kitting or assembly task
    
    
    '''
    #save and cancel buttons
    saveOrdButton=tk.Button(newOrderWind, text="Save and Exit", command=newOrderWind.destroy)
    saveOrdButton.pack()
    ordCancelFlag=tk.StringVar()
    ordCancelFlag.set('0')
    cancel_new_ord_part=partial(cancel_func, newOrderWind, ordCancelFlag)
    cancelNewOrdButton=tk.Button(newOrderWind, text="Cancel", command=cancel_new_ord_part)
    cancelNewOrdButton.pack(pady=20)
    newOrderWind.mainloop()
    if ordCancelFlag.get()=="1":
        orderCounter.remove(0)