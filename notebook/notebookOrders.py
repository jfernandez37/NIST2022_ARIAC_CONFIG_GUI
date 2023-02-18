import random
import string
import tkinter as tk
from functools import partial
orderTypes=["kitting", "assembly", "combined"]
quadrants=["1","2","3","4"]
agvOptions=["1","2","3","4"]
kittingDestinations=["warehouse", "assembly_front","assembly_back","kitting"]
assemblyStations=["as1","as2","as3","as4"]
kittingTrayIDs=[]
for i in range(10):
    kittingTrayIDs.append(str(i))
currentQuadMenu=[]
orderCategories=["time-based","during kitting", "during assembly","after kitting", "after assembly"]
taskPresentFlag=[]
allProdTypes=["sensor", "pump", "regulator", "battery"]
allProdColors=['green', 'red', 'purple','blue','orange']
conditionTypes=['time','partPlace','submission']
def showNewOrderMenu(orderWidgetsArr, orderValsArr):
    orderValsArr[0].set(orderCategories[0])
    orderValsArr[1].set(orderTypes[0])
    orderValsArr[2].set('0')
    orderValsArr[3].set(conditionTypes[0])
    orderValsArr[4].set('0')
    orderValsArr[5].set("")
    orderValsArr[6].set("")
    orderValsArr[7].set("")
    orderValsArr[8].set("")
    orderValsArr[9].set(agvOptions[0])
    orderValsArr[10].set(kittingTrayIDs[0])
    orderValsArr[11].set(kittingDestinations[0])
    orderValsArr[12].set("")
    orderWidgetsArr[0].grid(column=2, row=0)
    orderWidgetsArr[1].grid(column=2, row=1)
    orderWidgetsArr[2].grid(column=2, row=2)
    orderWidgetsArr[3].grid(column=2, row=3)
    orderWidgetsArr[4].grid(column=2, row=4)
    orderWidgetsArr[5].grid(column=2, row=5)
    orderWidgetsArr[6].grid(column=2, row=6)
    orderWidgetsArr[7].grid(column=2, row=7)
    orderWidgetsArr[8].grid(column=2, row=8)
    orderWidgetsArr[17].grid(column=2, row=14)
    orderWidgetsArr[18].grid(column=2, row=15)
    orderWidgetsArr[19].grid(column=2, row=16)
    orderWidgetsArr[20].grid(column=2, row=17)
    orderWidgetsArr[21].grid(column=2, row=18)
    orderWidgetsArr[22].grid(column=2, row=19)
    orderWidgetsArr[23].grid(column=2, row=20)
    orderWidgetsArr[24].grid(column=2, row=21)
    

def showCorrectMenu(orderValsArr, orderWidgetsArr,tempIDs,a,b,c):
    if orderValsArr[3].get()=="":
        orderValsArr[4].set('')#time
        orderValsArr[5].set('')#agv
        orderValsArr[6].set('')#partType
        orderValsArr[7].set('')#partColor
        orderValsArr[8].set('')#annId
        orderWidgetsArr[7].grid_forget()#timeLabel
        orderWidgetsArr[8].grid_forget()#timeEntry
        orderWidgetsArr[9].grid_forget()#agvLabel
        orderWidgetsArr[10].grid_forget()#agvMenu
        orderWidgetsArr[11].grid_forget()#partTypeLabel
        orderWidgetsArr[12].grid_forget()#partTypeMenu
        orderWidgetsArr[13].grid_forget()#partColorLabel
        orderWidgetsArr[14].grid_forget()#partColorMenu
        orderWidgetsArr[15].grid_forget()#annIDLabel
        orderWidgetsArr[16].grid_forget()#annIDMenu
    elif orderValsArr[3].get()==conditionTypes[1]:
        orderWidgetsArr[7].grid(column=2, row=7)
        orderWidgetsArr[8].grid(column=2, row=8)
        orderValsArr[4].set('0')
        orderValsArr[5].set('')
        orderValsArr[6].set('')
        orderValsArr[7].set('')
        orderValsArr[8].set('')
        orderWidgetsArr[9].grid_forget()
        orderWidgetsArr[10].grid_forget()
        orderWidgetsArr[11].grid_forget()
        orderWidgetsArr[12].grid_forget()
        orderWidgetsArr[13].grid_forget()
        orderWidgetsArr[14].grid_forget()
        orderWidgetsArr[15].grid_forget()
        orderWidgetsArr[16].grid_forget()
    elif orderValsArr[3].get()==conditionTypes[2]:
        orderWidgetsArr[9].grid(column=2, row=7)
        orderWidgetsArr[10].grid(column=2, row=8)
        orderValsArr[5].set(agvOptions[0])
        orderWidgetsArr[11].grid(column=2, row=9)
        orderWidgetsArr[12].grid(column=2, row=10)
        orderWidgetsArr[13].grid(column=2, row=11)
        orderWidgetsArr[14].grid(column=2, row=12)
        orderValsArr[6].set(allProdTypes[0])
        orderValsArr[7].set(allProdColors[0])
        orderValsArr[4].set('')
        orderWidgetsArr[7].grid_forget()
        orderWidgetsArr[8].grid_forget()
        orderValsArr[8].set('')
        orderWidgetsArr[15].grid_forget()
        orderWidgetsArr[16].grid_forget()
    else:
        orderWidgetsArr[15].grid(after=7)
        orderWidgetsArr[16].grid(after=8)
        orderValsArr[8].set(tempIDs[0])
        orderValsArr[4].set('')
        orderValsArr[5].set('')
        orderValsArr[6].set('')
        orderValsArr[7].set('')
        orderWidgetsArr[7].grid_forget()
        orderWidgetsArr[8].grid_forget()
        orderWidgetsArr[9].grid_forget()
        orderWidgetsArr[10].grid_forget()
        orderWidgetsArr[11].grid_forget()
        orderWidgetsArr[12].grid_forget()
        orderWidgetsArr[13].grid_forget()
        orderWidgetsArr[14].grid_forget()

def typeOfProdSelect(kittingParts, assemblyParts, orderType):
    '''Runs the correct function based on the order type'''
    if orderType.get()=="kitting":
        addKittingProduct(kittingParts)
    else:
        addAssembProduct(assemblyParts)

def updateTaskOptions(orderType, kitTrayId, taskAgvMenu,kitTrayIdLabel, kitTrayIdMenu, kittingDestination, kittingDestinationLabel, kittingDestinationMenu, assemblyStation, assemblyStationLabel, assemblyStationMenu,a,b,c):
    '''Shows the correct options for different types of orders'''
    if orderType.get()=="kitting" and len(taskPresentFlag)>0:
        taskPresentFlag.clear()
        kitTrayId.set(kittingTrayIDs[0])
        kittingDestination.set(kittingDestinations[0])
        assemblyStation.set("")
        kitTrayIdLabel.grid(after=taskAgvMenu)
        kitTrayIdMenu.grid(after=kitTrayIdLabel)
        kittingDestinationLabel.grid(after=kitTrayIdMenu)
        kittingDestinationMenu.grid(after=kittingDestinationLabel)
        assemblyStationLabel.grid_forget()
        assemblyStationMenu.grid_forget()
    elif orderType.get()!="kitting" and len(taskPresentFlag)==0:
        taskPresentFlag.append(0)
        kitTrayId.set("")
        kittingDestination.set("")
        assemblyStation.set(assemblyStations[0])
        kitTrayIdLabel.grid_forget()
        kitTrayIdMenu.grid_forget()
        kittingDestinationLabel.grid_forget()
        kittingDestinationMenu.grid_forget()
        assemblyStationLabel.grid(after=taskAgvMenu)
        assemblyStationMenu.grid(after=assemblyStationLabel)

def generateOrderId(usedId):
    '''Generates a unique id for each order'''
    newId=''.join(random.choices(string.ascii_uppercase+string.digits,k=8))
    if newId in usedId:
        while newId in usedId:
            newId=''.join(random.choices(string.ascii_uppercase+string.digits,k=8))
    usedId.append(newId)
    return newId

def orderWidgets(orderFrame, orderMSGS,orderConditions, orderCounter, usedIDs, kittingParts, assemblyParts):
    #generate the order id
    tempIDs=[]
    orderWidgetsArr=[]
    orderValsArr=[]
    for id in usedIDs:
        tempIDs.append(id)
    orderID=generateOrderId(usedIDs)

    orderCategory=tk.StringVar()
    orderCategory.set(orderCategories[0])
    orderCategoryLabel=tk.Label(orderFrame, text="Select the category of the order")
    orderCategoryLabel.grid_forget()
    orderCategoryMenu=tk.OptionMenu(orderFrame, orderCategory, *orderCategories)
    orderCategoryMenu.grid_forget()
    orderValsArr.append(orderCategory)
    orderWidgetsArr.append(orderCategoryLabel)
    orderWidgetsArr.append(orderCategoryMenu)
    #order type
    orderType=tk.StringVar()
    orderType.set(orderTypes[0])
    orderTypeSelectionLabel=tk.Label(orderFrame, text="Select the type of order")
    orderTypeSelectionLabel.grid_forget()
    orderTypeSelectionMenu=tk.OptionMenu(orderFrame, orderType, *orderTypes)
    orderTypeSelectionMenu.grid_forget()
    orderValsArr.append(orderType)
    orderWidgetsArr.append(orderTypeSelectionLabel)
    orderWidgetsArr.append(orderTypeSelectionMenu)
    #Priority
    orderPriority=tk.StringVar()
    orderPriority.set('0')
    orderPriorityCheckBox=tk.Checkbutton(orderFrame, text="Priority", variable=orderPriority, onvalue="1", offvalue="0", height=1, width=20)
    orderPriorityCheckBox.grid_forget()
    orderValsArr.append(orderPriority)
    orderWidgetsArr.append(orderPriorityCheckBox)
    #announcement
    condition=tk.StringVar()
    condition.set(conditionTypes[0])
    conditionLabel=tk.Label(orderFrame, text="Select a condition for the order")
    conditionLabel.grid_forget()
    conditionMenu=tk.OptionMenu(orderFrame, condition, *conditionTypes)
    conditionMenu.grid_forget()
    orderValsArr.append(condition)
    orderWidgetsArr.append(conditionLabel)
    orderWidgetsArr.append(conditionMenu)
    time=tk.StringVar()
    time.set('0')
    timeLabel=tk.Label(orderFrame, text="Enter the time")
    timeLabel.grid_forget()
    timeEntry=tk.Entry(orderFrame, textvariable=time)
    timeEntry.grid_forget()
    orderValsArr.append(time)
    orderWidgetsArr.append(timeLabel)
    orderWidgetsArr.append(timeEntry)
    agv=tk.StringVar()
    agv.set("")
    agvLabel=tk.Label(orderFrame, text="Choose the agv")
    agvLabel.grid_forget()
    agvMenu=tk.OptionMenu(orderFrame, agv, *agvOptions)
    agvMenu.grid_forget()
    orderValsArr.append(agv)
    orderWidgetsArr.append(agvLabel)
    orderWidgetsArr.append(agvMenu)
    partType=tk.StringVar()
    partType.set("")
    partTypeLabel=tk.Label(orderFrame, text="Select the type of part")
    partTypeLabel.grid_forget()
    partTypeMenu=tk.OptionMenu(orderFrame, partType, *allProdTypes)
    partTypeMenu.grid_forget()
    orderValsArr.append(partType)
    orderWidgetsArr.append(partTypeLabel)
    orderWidgetsArr.append(partTypeMenu)
    partColor=tk.StringVar()
    partColor.set("")
    partColorLabel=tk.Label(orderFrame, text="Select the color of the part")
    partColorLabel.grid_forget()
    partColorMenu=tk.OptionMenu(orderFrame, partColor, *allProdColors)
    partColorMenu.grid_forget()
    orderValsArr.append(partColor)
    orderWidgetsArr.append(partColorLabel)
    orderWidgetsArr.append(partColorMenu)
    annID=tk.StringVar()
    annID.set("")
    annIDLabel=tk.Label(orderFrame, text="Select the order ID")
    annIDLabel.grid_forget()
    annIDMenu=tk.OptionMenu(orderFrame, annID, *tempIDs)
    annIDMenu.grid_forget()
    orderValsArr.append(annID)
    orderWidgetsArr.append(annIDLabel)
    orderWidgetsArr.append(annIDMenu)
    #Task options
    bufferLabel=tk.Label(orderFrame, text="")
    bufferLabel.grid(pady=5)
    taskAGV=tk.StringVar()
    taskAGV.set(agvOptions[0])
    taskAGVLabel=tk.Label(orderFrame, text="Select the agv for the task")
    taskAGVLabel.grid_forget()
    taskAgvMenu=tk.OptionMenu(orderFrame, taskAGV, *agvOptions)
    taskAgvMenu.grid_forget()
    orderValsArr.append(taskAGV)
    orderWidgetsArr.append(taskAGVLabel)
    orderWidgetsArr.append(taskAgvMenu)
    kitTrayId=tk.StringVar()
    kitTrayId.set(kittingTrayIDs[0])
    kitTrayIdLabel=tk.Label(orderFrame, text="Select the tray ID for the kitting task")
    kitTrayIdLabel.grid_forget()
    kitTrayIdMenu=tk.OptionMenu(orderFrame, kitTrayId, *kittingTrayIDs)
    kitTrayIdMenu.grid_forget()
    orderValsArr.append(kitTrayId)
    orderWidgetsArr.append(kitTrayIdLabel)
    orderWidgetsArr.append(kitTrayIdMenu)
    kittingDestination=tk.StringVar()
    kittingDestination.set(kittingDestinations[0])
    kittingDestinationLabel=tk.Label(orderFrame, text="Select the destination for kitting")
    kittingDestinationLabel.grid_forget()
    kittingDestinationMenu=tk.OptionMenu(orderFrame, kittingDestination, *kittingDestinations)
    kittingDestinationMenu.grid_forget()
    orderValsArr.append(kittingDestination)
    orderWidgetsArr.append(kittingDestinationLabel)
    orderWidgetsArr.append(kittingDestinationMenu)
    assemblyStation=tk.StringVar()
    assemblyStation.set("")
    assemblyStationLabel=tk.Label(orderFrame, text="Select the station for assembly")
    assemblyStationLabel.grid_forget()
    assemblyStationMenu=tk.OptionMenu(orderFrame, assemblyStation, *assemblyStations)
    assemblyStationMenu.grid_forget()
    orderValsArr.append(assemblyStation)
    orderWidgetsArr.append(assemblyStationLabel)
    orderWidgetsArr.append(assemblyStationMenu)
    #Add order button
    addOrderButton=tk.Button(orderFrame, text="Add order", command=)
    addOrderButton.grid(column=1, row=5)
    #add product button
    type_of_prod_select=partial(typeOfProdSelect, kittingParts, assemblyParts, orderType)
    addProdButton=tk.Button(orderFrame, text="Add product", command=type_of_prod_select)
    addProdButton.grid()
    #save and cancel buttons
    saveOrdButton=tk.Button(orderFrame, text="Save order", command=)
    saveOrdButton.grid()
    #update menu functions
    update_task_options=partial(updateTaskOptions, orderType, kitTrayId, taskAgvMenu,kitTrayIdLabel, kitTrayIdMenu, kittingDestination, kittingDestinationLabel, kittingDestinationMenu, assemblyStation, assemblyStationLabel, assemblyStationMenu)
    orderType.trace('w', update_task_options)
    updateConditionMenu=partial(showCorrectMenu,condition, conditionMenu, time, timeLabel, timeEntry, agv, agvLabel, agvMenu, partType, partTypeLabel, partTypeMenu, partColor, partColorLabel, partColorMenu, annID, annIDLabel, annIDMenu,tempIDs)
    condition.trace('w', updateConditionMenu)