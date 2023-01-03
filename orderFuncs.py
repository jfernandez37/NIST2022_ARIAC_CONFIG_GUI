import random
import string
import tkinter as tk
from Functions.checkCancel import *
from functools import partial
from newFunctions.validationFunctions import *
from newFunctions.newClasses import *
orderTypes=["kitting", "assembly", "combined"]
quadrants=["0","1","2","3"]
currentQuadMenu=[]

def generateOrderId(usedId):
    newId=''.join(random.choices(string.ascii_uppercase+string.digits,k=8))
    if newId in usedId:
        while newId in usedId:
            newId=''.join(random.choices(string.ascii_uppercase+string.digits,k=8))
    usedId.append(newId)
    return newId

def updateQuadMenu(orderNum, orderQuadrant, orderQuadMenu, orderPriorityCheckBox, orderQuadLabel, a,b,c):
    if orderNum.get()!=" " and len(currentQuadMenu)==0:
        orderQuadrant.set('0')
        orderQuadMenu.pack(before=orderPriorityCheckBox)
        orderQuadLabel.pack(before=orderQuadMenu)
        currentQuadMenu.append(0)
    elif orderNum.get()==" ":
        orderQuadrant.set(' ')
        orderQuadMenu.pack_forget()
        orderQuadLabel.pack_forget()
        for i in currentQuadMenu:
            currentQuadMenu.remove(i)


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
    timeConditionEntry=tk.Entry(newOrderWind, textvariable=timeCondition)
    timeConditionEntry.pack()
    #order condition
    orderNum=tk.StringVar()
    orderNum.set(" ")
    orderNums=[" "]
    orderQuadrant=tk.StringVar()
    orderQuadrant.set(" ")
    if len(orderCounter)>1:
        for i in range(len(orderCounter)-1):
            orderNums.append(str(i+1))
        orderNumLabel=tk.Label(newOrderWind, text="Choose the order number for the order_condition announcement. Leave blank to skip.")
        orderNumLabel.pack()
        orderNumMenu=tk.OptionMenu(newOrderWind, orderNum, *orderNums)
        orderNumMenu.pack()
    orderQuadLabel=tk.Label(newOrderWind, text="Choose the quadrant for the order_condition announcement")
    orderQuadLabel.pack_forget()
    orderQuadMenu=tk.OptionMenu(newOrderWind, orderQuadrant, *quadrants)
    orderQuadMenu.pack_forget()
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
    order_quad_func=partial(updateQuadMenu, orderNum, orderQuadrant, orderQuadMenu, orderPriorityCheckBox, orderQuadLabel)
    orderNum.trace('w',order_quad_func)
    newOrderWind.mainloop()
    if ordCancelFlag.get()=="1":
        orderCounter.remove(0)