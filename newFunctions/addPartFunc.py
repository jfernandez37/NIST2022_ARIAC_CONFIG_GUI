from newFunctions.newClasses import *
import tkinter as tk
from functools import partial
from Functions.checkCancel import *
from newFunctions.validationFunctions import *
from newFunctions.updateAGVFuncs import updateAgvQudrants
agvList=["agv1", "agv2", "agv3", "agv4"]
partTypes=["sensor", "pump", "regulator", "battery"]
partColors=['green', 'red', 'purple','blue','orange']
def addPart(agv1Parts, agv2Parts, agv3Parts, agv4Parts, agv1Quadrants,agv2Quadrants,agv3Quadrants,agv4Quadrants):
    newPartWind=tk.Toplevel()
    newPartWind.geometry("850x600")
    #agv selection
    agvSelection=tk.StringVar()
    agvSelection.set(agvList[0])
    agvSelectLabel=tk.Label(newPartWind, text="Select the agv for the part")
    agvSelectLabel.pack()
    agvSelectMenu=tk.OptionMenu(newPartWind, agvSelection, *agvList)
    agvSelectMenu.pack()
    #part type selection
    partType=tk.StringVar()
    partType.set(partTypes[0])
    partTypeSelectLabel=tk.Label(newPartWind, text="Select the type of part")
    partTypeSelectLabel.pack()
    partTypeSelectMenu=tk.OptionMenu(newPartWind, partType, *partTypes)
    partTypeSelectMenu.pack()
    #part color selection
    partColor=tk.StringVar()
    partColor.set(partColors[0])
    partColorSelectLabel=tk.Label(newPartWind, text="Select the color of the part")
    partColorSelectLabel.pack()
    partColorSelectMenu=tk.OptionMenu(newPartWind, partColor, *partColors)
    partColorSelectMenu.pack()
    #quadrant selection
    partQuadrant=tk.StringVar()
    partQuadrant.set(agv1Quadrants[0])
    partQuadrantSelectLabel=tk.Label(newPartWind, text="Select the quadrant of the tray for the part")
    partQuadrantSelectLabel.pack()
    partQuadrantSelectMenu=tk.OptionMenu(newPartWind, partQuadrant, *agv1Quadrants)
    partQuadrantSelectMenu.pack()
    #rotation entry
    partRotation=tk.StringVar()
    partRotation.set('0')
    partRotationLabel=tk.Label(newPartWind, text="Enter the rotation of the part")
    partRotationLabel.pack()
    partRotationEntry=tk.Entry(newPartWind, textvariable=partRotation)
    partRotationEntry.pack()
    #save and cancel buttons
    save_new_part=partial(updateAgvQudrants,agvSelection, partQuadrantSelectMenu, partQuadrant, agv1Quadrants,agv2Quadrants,agv3Quadrants,agv4Quadrants, newPartWind)
    saveNewPartButton=tk.Button(newPartWind, text="Save", command=save_new_part)
    saveNewPartButton.pack(pady=20)
    newPartCancelFlag=tk.StringVar()
    newPartCancelFlag.set("0")
    cancel_new_part=partial(cancel_func, newPartWind, newPartCancelFlag)
    cancelNewPartButton=tk.Button(newPartWind, text="Cancel", command=cancel_new_part)
    cancelNewPartButton.pack(pady=20)
    #trace functions
    validate_rotation=partial(validateRotationValue, partRotation, saveNewPartButton)
    partRotation.trace('w', validate_rotation)
    newPartWind.mainloop()
    if newPartCancelFlag.get()=="0":
        add_quotes(partType)
        add_quotes(partColor)
        if 'pi' in partRotation.get():
            add_quotes(partRotation.get())
        if agvSelection.get()=='agv1':
            agv1Parts.append(Parts(partType.get(), partColor.get(), partQuadrant.get(), partRotation.get()))
        elif agvSelection.get()=='agv2':
            agv2Parts.append(Parts(partType.get(), partColor.get(), partQuadrant.get(), partRotation.get()))
        elif agvSelection.get()=='agv3':
            agv3Parts.append(Parts(partType.get(), partColor.get(), partQuadrant.get(), partRotation.get()))
        else:
            agv4Parts.append(Parts(partType.get(), partColor.get(), partQuadrant.get(), partRotation.get()))


def writePartsToFile(name, id, partsList, saveFileName):
    with open(saveFileName, "a") as o:
        o.write("    "+name+":\n")
        o.write("      tray_id: "+ id+"\n")
        o.write("      parts:\n")
        for i in partsList:
            o.write("      - type: "+i.pType+"\n")
            o.write("        color: "+i.color+"\n")
            o.write("        quadrant: "+i.quadrant+"\n")
            o.write("        rotation: "+i.rotation+"\n")
        o.write("\n\n")
