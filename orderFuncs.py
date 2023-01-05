import random
import string
import tkinter as tk
from Functions.checkCancel import *
from functools import partial
from newFunctions.validationFunctions import *
from newFunctions.newClasses import *
orderTypes=["kitting", "assembly", "combined"]
quadrants=["0","1","2","3"]
agvOptions=["1","2","3","4"]
kittingDestinations=["warehouse", "as1", "as2","as3","as4","kitting"]
assemblyStations=["as1","as2","as3","as4"]
kittingTrayIDs=[]
for i in range(10):
    kittingTrayIDs.append(str(i))
currentQuadMenu=[]
challengeList=['flipped_part', 'faulty_part', 'dropped_part', 'sensor_blackout', 'robot_malfunction']
orderCategories=["time-based","during kitting", "during assembly","after kitting", "after assembly"]
taskPresentFlag=[]
def updateTaskOptions(orderType, kitTrayId, taskAgvMenu,kitTrayIdLabel, kitTrayIdMenu, kittingDestination, kittingDestinationLabel, kittingDestinationMenu, assemblyStation, assemblyStationLabel, assemblyStationMenu,a,b,c):
    if orderType.get()=="kitting" and len(taskPresentFlag)==1:
        taskPresentFlag.clear()
        kitTrayId.set(kittingTrayIDs[0])
        kittingDestination.set(kittingDestinations[0])
        assemblyStation.set("")
        kitTrayIdLabel.pack(after=taskAgvMenu)
        kitTrayIdMenu.pack(after=kitTrayIdLabel)
        kittingDestinationLabel.pack(after=kitTrayIdMenu)
        kittingDestinationMenu.pack(after=kittingDestinationLabel)
        assemblyStationLabel.pack_forget()
        assemblyStationMenu.pack_forget()
    elif len(taskPresentFlag)==0:
        taskPresentFlag.append(0)
        kitTrayId.set("")
        kittingDestination.set("")
        assemblyStation.set(assemblyStations[0])
        kitTrayIdLabel.pack_forget()
        kitTrayIdMenu.pack_forget()
        kittingDestinationLabel.pack_forget()
        kittingDestinationMenu.pack_forget()
        assemblyStationLabel.pack(after=taskAgvMenu)
        assemblyStationMenu.pack(after=assemblyStationLabel)

def generateOrderId(usedId):
    newId=''.join(random.choices(string.ascii_uppercase+string.digits,k=8))
    if newId in usedId:
        while newId in usedId:
            newId=''.join(random.choices(string.ascii_uppercase+string.digits,k=8))
    usedId.append(newId)
    return newId

def addOrderChallenge(allOrderChallenges, orderCounter):
    orderChallengeWind=tk.Toplevel()
    orderChallengeType=tk.StringVar()
    orderChallengeType.set(challengeList[0])
    orderChallengeTypeLabel=tk.Label(orderChallengeWind,text="Select the type of challenge")
    orderChallengeTypeLabel.pack()
    orderChallengeTypeMenu=tk.OptionMenu(orderChallengeWind, orderChallengeType, *challengeList)
    orderChallengeTypeMenu.pack()
    orderChallengeQuadrant=tk.StringVar()
    orderChallengeQuadrant.set(quadrants[0])
    orderChallengeQuadLabel=tk.Label(orderChallengeWind, text="Select the quadrant for the challenge")
    orderChallengeQuadLabel.pack()
    orderChallengeQuadMenu=tk.OptionMenu(orderChallengeWind, orderChallengeQuadrant, *quadrants)
    orderChallengeQuadMenu.pack()
    orderChallengeSave=tk.Button(orderChallengeWind, text="Save", command=orderChallengeWind.destroy)
    orderChallengeSave.pack(pady=20)
    orderChallengeCancelFlag=tk.StringVar()
    orderChallengeCancelFlag.set('0')
    cancel_order_challenge=partial(exitAndFlag, orderChallengeWind, orderChallengeCancelFlag)
    orderChallengeCancel=tk.Button(orderChallengeWind, text="Cancel", command=cancel_order_challenge)
    orderChallengeCancel.pack()
    orderChallengeWind.mainloop()
    if orderChallengeCancelFlag.get()=="0":
        allOrderChallenges.append(OrderChallenge(str(len(orderCounter)),orderChallengeType.get(),orderChallengeQuadrant.get()))

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


def addNewOrder(orderCounter, allOrderChallenges):
    orderCounter.append(0)
    newOrderWind=tk.Tk()
    newOrderWind.geometry("850x600")
    #orderCategory
    orderCategory=tk.StringVar()
    orderCategory.set(orderCategories[0])
    orderCategoryLabel=tk.Label(newOrderWind, text="Select the category of the order")
    orderCategoryLabel.pack()
    orderCategoryMenu=tk.OptionMenu(newOrderWind, orderCategory, *orderCategories)
    orderCategoryMenu.pack()
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
    order_challenge_func=partial(addOrderChallenge, allOrderChallenges, orderCounter)
    addOrderChallengeButton=tk.Button(newOrderWind, text="Add challenge", command=order_challenge_func)
    addOrderChallengeButton.pack()
    #Task options
    taskAGV=tk.StringVar()
    taskAGV.set(agvOptions[0])
    taskAGVLabel=tk.Label(newOrderWind, text="Select the agv for the task")
    taskAGVLabel.pack()
    taskAgvMenu=tk.OptionMenu(newOrderWind, taskAGV, *agvOptions)
    taskAgvMenu.pack()
    kitTrayId=tk.StringVar()
    kitTrayId.set(kittingTrayIDs[0])
    kitTrayIdLabel=tk.Label(newOrderWind, text="Select the tray ID for the kitting task")
    kitTrayIdLabel.pack()
    kitTrayIdMenu=tk.OptionMenu(newOrderWind, kitTrayId, *kittingTrayIDs)
    kitTrayIdMenu.pack()
    kittingDestination=tk.StringVar()
    kittingDestination.set(kittingDestinations[0])
    kittingDestinationLabel=tk.Label(newOrderWind, text="Select the destination for kitting")
    kittingDestinationLabel.pack()
    kittingDestinationMenu=tk.OptionMenu(newOrderWind, kittingDestination, *kittingDestinations)
    kittingDestinationMenu.pack()
    assemblyStation=tk.StringVar()
    assemblyStation.set("")
    assemblyStationLabel=tk.Label(newOrderWind, text="Select the station for assembly")
    assemblyStationLabel.pack_forget()
    assemblyStationMenu=tk.OptionMenu(newOrderWind, assemblyStation, *assemblyStations)
    assemblyStationMenu.pack_forget()
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
    update_task_options=partial(updateTaskOptions, orderType, kitTrayId, taskAgvMenu,kitTrayIdLabel, kitTrayIdMenu, kittingDestination, kittingDestinationLabel, kittingDestinationMenu, assemblyStation, assemblyStationLabel, assemblyStationMenu)
    orderType.trace('w', update_task_options)
    newOrderWind.mainloop()
    if ordCancelFlag.get()=="1":
        orderCounter.remove(0)