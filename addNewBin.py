import tkinter as tk
from Functions.checkCancel import *
from functools import partial
from newFunctions.validationFunctions import *
from newClasses import *
partTypes=["sensor", "pump", "regulator", "battery"]
partColors=['green', 'red', 'purple','blue','orange']
allBins=[]
checkBoxes=[]
for i in range(8):
    allBins.append('bin'+str(i+1))

def runSlotChecks(addBinWind, currentBin,slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9, presentChecks,bin1Slots,bin2Slots,bin3Slots,bin4Slots,bin5Slots,bin6Slots,bin7Slots,bin8Slots,a,b,c):
    if currentBin.get()=="bin1":
        slotChecks(bin1Slots, addBinWind, slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9, presentChecks)
    elif currentBin.get()=="bin2":
        slotChecks(bin2Slots, addBinWind, slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9, presentChecks)
    elif currentBin.get()=="bin3":
        slotChecks(bin3Slots, addBinWind, slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9, presentChecks)
    elif currentBin.get()=="bin4":
        slotChecks(bin4Slots, addBinWind, slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9, presentChecks)
    elif currentBin.get()=="bin5":
        slotChecks(bin5Slots, addBinWind, slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9, presentChecks)
    elif currentBin.get()=="bin6":
        slotChecks(bin6Slots, addBinWind, slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9, presentChecks)
    elif currentBin.get()=="bin7":
        slotChecks(bin7Slots, addBinWind, slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9, presentChecks)
    elif currentBin.get()=="bin8":
        slotChecks(bin8Slots, addBinWind, slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9, presentChecks)

def slotChecks(arr, addBinWind, slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9, presentChecks):
    for i in presentChecks:
        i.destroy()
    slot1.set("0")
    slot2.set("0")
    slot3.set("0")
    slot4.set("0")
    slot5.set("0")
    slot6.set("0")
    slot7.set("0")
    slot8.set("0")
    slot9.set("0")
    if "1" in arr:
        slot1Check=tk.Checkbutton(addBinWind, text="Slot 1", variable=slot1, onvalue="1", offvalue="0", height=2, width=20)
        slot1Check.pack()
        presentChecks.append(slot1Check)
    if "2" in arr:
        slot2Check=tk.Checkbutton(addBinWind, text="Slot 2", variable=slot2, onvalue="1", offvalue="0", height=2, width=20)
        slot2Check.pack()
        presentChecks.append(slot2Check)
    if "3" in arr:
        slot3Check=tk.Checkbutton(addBinWind, text="Slot 3", variable=slot3, onvalue="1", offvalue="0", height=2, width=20)
        slot3Check.pack()
        presentChecks.append(slot3Check)
    if "4" in arr:
        slot4Check=tk.Checkbutton(addBinWind, text="Slot 4", variable=slot4, onvalue="1", offvalue="0", height=2, width=20)
        slot4Check.pack()
        presentChecks.append(slot4Check)
    if "5" in arr:
        slot5Check=tk.Checkbutton(addBinWind, text="Slot 5", variable=slot5, onvalue="1", offvalue="0", height=2, width=20)
        slot5Check.pack()
        presentChecks.append(slot5Check)
    if "6" in arr:
        slot6Check=tk.Checkbutton(addBinWind, text="Slot 6", variable=slot6, onvalue="1", offvalue="0", height=2, width=20)
        slot6Check.pack()
        presentChecks.append(slot6Check)
    if "7" in arr:
        slot7Check=tk.Checkbutton(addBinWind, text="Slot 7", variable=slot7, onvalue="1", offvalue="0", height=2, width=20)
        slot7Check.pack()
        presentChecks.append(slot7Check)
    if "8" in arr:
        slot8Check=tk.Checkbutton(addBinWind, text="Slot 8", variable=slot8, onvalue="1", offvalue="0", height=2, width=20)
        slot8Check.pack()
        presentChecks.append(slot8Check)
    if "9" in arr:
        slot9Check=tk.Checkbutton(addBinWind, text="Slot 9", variable=slot9, onvalue="1", offvalue="0", height=2, width=20)
        slot9Check.pack()
        presentChecks.append(slot9Check)

def updateAvailableSlots(currentBin, bin1Slots,bin2Slots,bin3Slots,bin4Slots,bin5Slots,bin6Slots,bin7Slots,bin8Slots, slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9,window):
    allSlots=[slot1.get(),slot2.get(),slot3.get(),slot4.get(),slot5.get(),slot6.get(),slot7.get(),slot8.get(),slot9.get()]
    counter=1
    if currentBin.get()=="bin1":
        for i in allSlots:
            if i=="1":
                bin1Slots.remove(str(counter))
            counter+=1
    elif currentBin.get()=="bin2":
        for i in allSlots:
            if i=="1":
                bin2Slots.remove(str(counter))
            counter+=1
    elif currentBin.get()=="bin3":
        for i in allSlots:
            if i=="1":
                bin3Slots.remove(str(counter))
            counter+=1
    elif currentBin.get()=="bin4":
        for i in allSlots:
            if i=="1":
                bin4Slots.remove(str(counter))
            counter+=1
    elif currentBin.get()=="bin5":
        for i in allSlots:
            if i=="1":
                bin5Slots.remove(str(counter))
            counter+=1
    elif currentBin.get()=="bin6":
        for i in allSlots:
            if i=="1":
                bin6Slots.remove(str(counter))
            counter+=1
    elif currentBin.get()=="bin7":
        for i in allSlots:
            if i=="1":
                bin7Slots.remove(str(counter))
            counter+=1
    elif currentBin.get()=="bin8":
        for i in allSlots:
            if i=="1":
                bin8Slots.remove(str(counter))
            counter+=1
    else:
        print("Error")
    window.destroy()

def addBin(bins,bin1Slots,bin2Slots,bin3Slots,bin4Slots,bin5Slots,bin6Slots,bin7Slots,bin8Slots):
    addBinWind=tk.Toplevel()
    #choose bin
    binID=tk.StringVar()
    binID.set(allBins[0])
    binSelectLabel=tk.Label(addBinWind, text="Select the bin")
    binSelectLabel.pack()
    binSelectMenu=tk.OptionMenu(addBinWind, binID, *allBins)
    binSelectMenu.pack()
    #part type
    partType=tk.StringVar()
    partType.set(partTypes[0])
    partTypeLabel=tk.Label(addBinWind, text="Select the type of part")
    partTypeLabel.pack()
    partTypeMenu=tk.OptionMenu(addBinWind, partType, *partTypes)
    partTypeMenu.pack()
    #part color
    partColor=tk.StringVar()
    partColor.set(partColors[0])
    partColorSelectLabel=tk.Label(addBinWind, text="Select the color of the part")
    partColorSelectLabel.pack()
    partColorSelectMenu=tk.OptionMenu(addBinWind, partColor, *partColors)
    partColorSelectMenu.pack()
    #slots
    slot1=tk.StringVar()
    slot2=tk.StringVar()
    slot3=tk.StringVar()
    slot4=tk.StringVar()
    slot5=tk.StringVar()
    slot6=tk.StringVar()
    slot7=tk.StringVar()
    slot8=tk.StringVar()
    slot9=tk.StringVar()
    slot1.set("0")
    slot2.set("0")
    slot3.set("0")
    slot4.set("0")
    slot5.set("0")
    slot6.set("0")
    slot7.set("0")
    slot8.set("0")
    slot9.set("0")
    slotChecks(bin1Slots, addBinWind, slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9, checkBoxes)
    #rotation
    partRotation=tk.StringVar()
    partRotation.set('0')
    partRotationLabel=tk.Label(addBinWind, text="Enter the rotation of the part")
    partRotationLabel.pack()
    partRotationEntry=tk.Entry(addBinWind, textvariable=partRotation)
    partRotationEntry.pack()
    #flipped
    flippedFlag=tk.StringVar()
    flippedFlag.set('0')
    flippedCheck=tk.Checkbutton(addBinWind, text="Flipped", variable=flippedFlag, onvalue="1", offvalue="0", height=5, width=20)
    flippedCheck.pack()
    #save and cancel buttons
    save_new_bin=partial(updateAvailableSlots, binID, bin1Slots,bin2Slots,bin3Slots,bin4Slots,bin5Slots,bin6Slots,bin7Slots,bin8Slots, slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9,addBinWind)
    saveNewPartButton=tk.Button(addBinWind, text="Save", command=save_new_bin)
    saveNewPartButton.pack(pady=20)
    newPartCancelFlag=tk.StringVar()
    newPartCancelFlag.set("0")
    cancel_new_part=partial(cancel_func, addBinWind, newPartCancelFlag)
    cancelNewPartButton=tk.Button(addBinWind, text="Cancel", command=cancel_new_part)
    cancelNewPartButton.pack(pady=20)
    #trace functions
    validate_rotation=partial(validateRotationValue, partRotation, saveNewPartButton)
    partRotation.trace('w', validate_rotation)
    update_checkboxes=partial(runSlotChecks,addBinWind, binID,slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9, checkBoxes,bin1Slots,bin2Slots,bin3Slots,bin4Slots,bin5Slots,bin6Slots,bin7Slots,bin8Slots)
    binID.trace('w', update_checkboxes)
    addBinWind.mainloop()
    selectedSlots=[]
    allSlots=[slot1.get(),slot2.get(),slot3.get(),slot4.get(),slot5.get(),slot6.get(),slot7.get(),slot8.get(),slot9.get()]
    counter=1
    for i in allSlots:
        if i=="1":
            selectedSlots.append(str(counter))
    slotsString=",".join(selectedSlots)
    bins.append(Bin(binID.get(),partType.get(), partColor.get(),"["+slotsString+"]",partRotation.get(), flippedFlag.get()))

