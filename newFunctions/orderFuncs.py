import random
import string
import tkinter as tk
from Functions.checkCancel import *
from functools import partial
from newFunctions.validationFunctions import *
from newFunctions.newClasses import *
from newFunctions.timeFunctions import *
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
allProdTypes=["sensor", "pump", "regulator", "battery"]
allProdColors=['green', 'red', 'purple','blue','orange']

def typeOfProdSelect(orderType,orderKittingParts, orderAssembParts, currentOrderID):
    '''Runs the correct function based on the order type'''
    if orderType.get()=="kitting":
        addKittingProduct(orderKittingParts, currentOrderID)
    else:
        addAssembProduct(orderAssembParts, currentOrderID)
    

def updateTaskOptions(orderType, kitTrayId, taskAgvMenu,kitTrayIdLabel, kitTrayIdMenu, kittingDestination, kittingDestinationLabel, kittingDestinationMenu, assemblyStation, assemblyStationLabel, assemblyStationMenu,a,b,c):
    '''Shows the correct options for different types of orders'''
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
    elif orderType.get()!="kitting" and len(taskPresentFlag)==0:
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
    '''Generates a unique id for each order'''
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

def addKittingProduct(orderKittingParts, currentOrderID):
    '''Adds a product to a kitting order'''
    kitProdWind=tk.Toplevel()
    #type of product
    prodType=tk.StringVar()
    prodType.set(allProdTypes[0])
    prodTypeLabel=tk.Label(kitProdWind, text="Select the type of product for the kitting task")
    prodTypeLabel.pack()
    prodTypeMenu=tk.OptionMenu(kitProdWind, prodType, *allProdTypes)
    prodTypeMenu.pack()
    #product color
    prodColor=tk.StringVar()
    prodColor.set(allProdColors[0])
    prodColorLabel=tk.Label(kitProdWind, text="Select the color of the product for the kitting task")
    prodColorLabel.pack()
    prodColorMenu=tk.OptionMenu(kitProdWind, prodColor, *allProdColors)
    prodColorMenu.pack()
    #product quadrant
    prodQuad=tk.StringVar()
    prodQuad.set(quadrants[0])
    prodQuadLabel=tk.Label(kitProdWind, text="Select the quadrant for the product")
    prodQuadLabel.pack()
    prodQuadMenu=tk.OptionMenu(kitProdWind, prodQuad, *quadrants)
    prodQuadMenu.pack()
    #save and cancel buttons
    kitProdCancelFlag=tk.StringVar()
    kitProdCancelFlag.set("0")
    saveKitProdButton=tk.Button(kitProdWind, text="Save and Exit", command=kitProdWind.destroy)
    saveKitProdButton.pack(pady=20)
    cancel_new_kit_prod=partial(cancel_func, kitProdWind, kitProdCancelFlag)
    cancelNewKitProdButton=tk.Button(kitProdWind, text="Cancel", command=cancel_new_kit_prod)
    cancelNewKitProdButton.pack(pady=20)
    kitProdWind.mainloop()
    if kitProdCancelFlag.get()=="0":
        orderKittingParts.append(KittingProds(currentOrderID,prodType.get(),prodColor.get(), prodQuad.get()))

def addAssembProduct(orderAssembParts, currentOrderID):
    '''Adds a product to an assembly or combined order'''
    assembProdWind=tk.Toplevel()
    #product type
    prodType=tk.StringVar()
    prodType.set(allProdTypes[0])
    prodTypeLabel=tk.Label(assembProdWind, text="Select the type of product for the assembly task")
    prodTypeLabel.pack()
    prodTypeMenu=tk.OptionMenu(assembProdWind, prodType, *allProdTypes)
    prodTypeMenu.pack()
    #product color
    prodColor=tk.StringVar()
    prodColor.set(allProdColors[0])
    prodColorLabel=tk.Label(assembProdWind, text="Select the color of the product for the assembly task")
    prodColorLabel.pack()
    prodColorMenu=tk.OptionMenu(assembProdWind, prodColor, *allProdColors)
    prodColorMenu.pack()
    #XYZ and RPY variable declarations
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
    #XYZ and RPY entry boxes
    x_val_label = tk.Label(assembProdWind, text="Enter the x value")
    x_val_label.pack()
    x_val_entry = tk.Entry(assembProdWind, textvariable=x_val)
    x_val_entry.pack()
    y_val_label = tk.Label(assembProdWind, text="Enter the y value")
    y_val_label.pack()
    y_val_entry = tk.Entry(assembProdWind, textvariable=y_val)
    y_val_entry.pack()
    z_val_label = tk.Label(assembProdWind, text="Enter the z value")
    z_val_label.pack()
    z_val_entry = tk.Entry(assembProdWind, textvariable=z_val)
    z_val_entry.pack()
    r_val_label = tk.Label(assembProdWind, text="Enter the r value")
    r_val_label.pack()
    r_val_entry = tk.Entry(assembProdWind, textvariable=r_val)
    r_val_entry.pack()
    p_val_label = tk.Label(assembProdWind, text="Enter the p value")
    p_val_label.pack()
    p_val_entry = tk.Entry(assembProdWind, textvariable=p_val)
    p_val_entry.pack()
    y_rpy_val_label = tk.Label(assembProdWind, text="Enter the y (rpy) value")
    y_rpy_val_label.pack()
    y_rpy_val_entry = tk.Entry(assembProdWind, textvariable=y_rpy_val)
    y_rpy_val_entry.pack()
    #assembly direction declarations
    x_dir=tk.StringVar()
    x_dir.set("0")
    y_dir=tk.StringVar()
    y_dir.set("0")
    z_dir=tk.StringVar()
    z_dir.set("0")
    #assembly direction entry boxes
    x_dir_label = tk.Label(assembProdWind, text="Enter the x value for the assembly direction")
    x_dir_label.pack()
    x_dir_entry = tk.Entry(assembProdWind, textvariable=x_dir)
    x_dir_entry.pack()
    y_dir_label = tk.Label(assembProdWind, text="Enter the y value for the assembly direction")
    y_dir_label.pack()
    y_dir_entry = tk.Entry(assembProdWind, textvariable=y_dir)
    y_dir_entry.pack()
    z_dir_label = tk.Label(assembProdWind, text="Enter the z value for the assembly direction")
    z_dir_label.pack()
    z_dir_entry = tk.Entry(assembProdWind, textvariable=z_dir)
    z_dir_entry.pack()
    #save and cancel buttons
    assembProdCancelFlag=tk.StringVar()
    assembProdCancelFlag.set("0")
    saveAssembProdButton=tk.Button(assembProdWind, text="Save and Exit", command=assembProdWind.destroy)
    saveAssembProdButton.pack(pady=20)
    cancel_new_assemb_prod=partial(cancel_func, assembProdWind, assembProdCancelFlag)
    cancelNewAssembProdButton=tk.Button(assembProdWind, text="Cancel", command=cancel_new_assemb_prod)
    cancelNewAssembProdButton.pack(pady=20)
    assembProdWind.mainloop()
    if assembProdCancelFlag.get()=="0":
        orderAssembParts.append(AssemblyProds(currentOrderID, prodType.get(), prodColor.get(), str("["+x_val.get()+", "+y_val.get()+", "+z_val.get()+"]"),
                                    str("["+r_val.get()+", "+p_val.get()+", "+y_rpy_val.get()+"]"), str("["+x_dir.get()+", "+y_dir.get()+", "+z_dir.get()+"]")))

def updateQuadMenu(orderNum, orderQuadrant, orderQuadMenu, orderPriorityCheckBox, orderQuadLabel, a,b,c):
    '''Updates the quadrant menu'''
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

def showAGVMenu(agvShow,agvShowCB, agvMenu, agvLabel, agv,quadLabel, quadMenu, quad, a,b,c):
    if agvShow.get()=="1":
        agvLabel.pack(after=agvShowCB)
        agvMenu.pack(after=agvLabel)
        quadLabel.pack(after=agvMenu)
        quadMenu.pack(after=quadLabel)
        agv.set(agvOptions[0])
        quad.set(quadrants[0])
    else:
        agvLabel.pack_forget()
        agvMenu.pack_forget()
        quadLabel.pack_forget()
        quadMenu.pack_forget()
        agv.set('')
        quad.set('')

def showTimeMenu(timeShow, timeShowCB, timeEntry, timeLabel, time, a,b,c):
    if timeShow.get()=="1":
        timeLabel.pack(after=timeShowCB)
        timeEntry.pack(after=timeLabel)
        time.set('0')
    else:
        timeLabel.pack_forget()
        timeEntry.pack_forget()
        time.set('')

def showPartMenu(partShow, partShowCB, partTypeLabel, partTypeMenu, partColorLabel, partColorMenu,partType, partColor,a,b,c):
    if partShow.get()=="1":
        partTypeLabel.pack(after=partShowCB)
        partTypeMenu.pack(after=partTypeLabel)
        partColorLabel.pack(after=partTypeMenu)
        partColorMenu.pack(after=partColorLabel)
        partType.set(allProdTypes[0])
        partColor.set(allProdColors[0])
    else:
        partTypeLabel.pack_forget()
        partTypeMenu.pack_forget()
        partColorLabel.pack_forget()
        partColorMenu.pack_forget()
        partType.set("")
        partColor.set("")

def showAnnIDMenu(annIDShow, annIDShowCB, annIDLabel, annIDMenu, annID, tempIDs, a,b,c):
    if annIDShow.get()=="1":
        annIDLabel.pack(after=annIDShowCB)
        annIDMenu.pack(after=annIDLabel)
        annID.set(tempIDs[0])
    else:
        annIDLabel.pack_forget()
        annIDMenu.pack_forget()
        annID.set("")

def addNewOrder(allOrders, orderCounter, allOrderChallenges, orderKittingParts,orderAssembParts, usedIDs):
    '''Window for adding a new order'''
    orderCounter.append(0)
    tempIDs=[]
    for id in usedIDs:
        tempIDs.append(id)
    orderID=generateOrderId(usedIDs)
    newOrderWind=tk.Toplevel()
    newOrderWind.geometry("850x800")
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
    '''order_challenge_func=partial(addOrderChallenge, allOrderChallenges, orderCounter)
    addOrderChallengeButton=tk.Button(newOrderWind, text="Add challenge", command=order_challenge_func)
    addOrderChallengeButton.pack()'''
    #announcement
    announcementLabel=tk.Label(newOrderWind, text="Announcement options")
    announcementLabel.pack()
    timeShow=tk.StringVar()
    timeShow.set('0')
    timeShowCB=tk.Checkbutton(newOrderWind, text="Time", variable=timeShow, onvalue="1", offvalue='0', height=1, width=20)
    timeShowCB.pack()
    time=tk.StringVar()
    time.set('')
    timeLabel=tk.Label(newOrderWind, text="Enter the time")
    timeLabel.pack_forget()
    timeEntry=tk.Entry(newOrderWind, textvariable=time)
    timeEntry.pack_forget()
    agvShow=tk.StringVar()
    agvShow.set('0')
    agvShowCB=tk.Checkbutton(newOrderWind, text="AGV", variable=agvShow, onvalue="1", offvalue='0', height=1, width=20)
    agvShowCB.pack()
    agv=tk.StringVar()
    agv.set("")
    agvLabel=tk.Label(newOrderWind, text="Choose the agv")
    agvLabel.pack_forget()
    agvMenu=tk.OptionMenu(newOrderWind, agv, *agvOptions)
    agvMenu.pack_forget()
    quadrant=tk.StringVar()
    quadrant.set("")
    quadLabel=tk.Label(newOrderWind, text="Select the quadrant")
    quadLabel.pack_forget()
    quadMenu=tk.OptionMenu(newOrderWind, quadrant, *quadrants)
    quadMenu.pack_forget()
    partShow=tk.StringVar()
    partShow.set('0')
    partShowCB=tk.Checkbutton(newOrderWind, text="Part", variable=partShow, onvalue="1", offvalue='0', height=1, width=20)
    partShowCB.pack()
    partType=tk.StringVar()
    partType.set("")
    partTypeLabel=tk.Label(newOrderWind, text="Select the type of part")
    partTypeLabel.pack_forget()
    partTypeMenu=tk.OptionMenu(newOrderWind, partType, *allProdTypes)
    partTypeMenu.pack_forget()
    partColor=tk.StringVar()
    partColor.set("")
    partColorLabel=tk.Label(newOrderWind, text="Select the color of the part")
    partColorLabel.pack_forget()
    partColorMenu=tk.OptionMenu(newOrderWind, partColor, *allProdColors)
    partColorMenu.pack_forget()
    if len(tempIDs)>0:
        annIDShow=tk.StringVar()
        annIDShow.set('0')
        annIDShowCB=tk.Checkbutton(newOrderWind, text="Order ID", variable=annIDShow, onvalue="1", offvalue='0', height=1, width=20)
        annIDShowCB.pack()
        annID=tk.StringVar()
        annID.set("")
        annIDLabel=tk.Label(newOrderWind, text="Select the order ID")
        annIDLabel.pack_forget()
        annIDMenu=tk.OptionMenu(newOrderWind, annID, *tempIDs)
        annIDMenu.pack_forget()
    #Task options
    bufferLabel=tk.Label(newOrderWind, text="")
    bufferLabel.pack(pady=5)
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
    #add product button
    type_of_prod_select=partial(typeOfProdSelect, orderType,orderKittingParts, orderAssembParts, orderID)
    addProdButton=tk.Button(newOrderWind, text="Add product", command=type_of_prod_select)
    addProdButton.pack()
    #save and cancel buttons
    saveOrdButton=tk.Button(newOrderWind, text="Save and Exit", command=newOrderWind.destroy)
    saveOrdButton.pack()
    ordCancelFlag=tk.StringVar()
    ordCancelFlag.set('0')
    cancel_new_ord_part=partial(cancel_func, newOrderWind, ordCancelFlag)
    cancelNewOrdButton=tk.Button(newOrderWind, text="Cancel", command=cancel_new_ord_part)
    cancelNewOrdButton.pack(pady=20)
    #update menu functions
    order_quad_func=partial(updateQuadMenu, orderNum, orderQuadrant, orderQuadMenu, orderPriorityCheckBox, orderQuadLabel)
    orderNum.trace('w',order_quad_func)
    update_task_options=partial(updateTaskOptions, orderType, kitTrayId, taskAgvMenu,kitTrayIdLabel, kitTrayIdMenu, kittingDestination, kittingDestinationLabel, kittingDestinationMenu, assemblyStation, assemblyStationLabel, assemblyStationMenu)
    orderType.trace('w', update_task_options)
    show_time_menu=partial(showTimeMenu, timeShow, timeShowCB, timeEntry, timeLabel, time)
    timeShow.trace('w', show_time_menu)
    validate_time=partial(validateTime, time)
    time.trace('w', validate_time)
    show_agv_menu=partial(showAGVMenu, agvShow,agvShowCB, agvMenu, agvLabel, agv,quadLabel, quadMenu, quadrant)
    agvShow.trace('w', show_agv_menu)
    show_part_menu=partial(showPartMenu, partShow, partShowCB, partTypeLabel, partTypeMenu, partColorLabel, partColorMenu,partType, partColor)
    partShow.trace('w', show_part_menu)
    if len(tempIDs)>0:
        show_annID_menu=partial(showAnnIDMenu,annIDShow, annIDShowCB, annIDLabel, annIDMenu, annID, tempIDs)
        annIDShow.trace('w', show_annID_menu)
    newOrderWind.mainloop()
    if ordCancelFlag.get()=="1":
        orderCounter.remove(0)
    else:
        if len(tempIDs)>0:
            announcementID=annID.get()
        else:
            announcementID=""
        if orderPriority.get()=="0":
            ordP="false"
        else:
            ordP="true"
        allOrders.append(Order(str(orderCategories.index(orderCategory.get())),orderID,orderType.get(),ordP, taskAGV.get(), kitTrayId.get(), kittingDestination.get(), assemblyStation.get(), time.get(), agv.get(), quadrant.get(), announcementID, partType.get(), partColor.get()))