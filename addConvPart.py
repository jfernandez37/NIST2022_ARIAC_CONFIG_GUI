import tkinter as tk
from Functions.checkCancel import *
from functools import partial
from newFunctions.validationFunctions import *
from newFunctions.newClasses import *

acceptedNum = "0123456789.-"  # for requiring number input for offset value
partTypes=["sensor", "pump", "regulator", "battery"]
partColors=['green', 'red', 'purple','blue','orange']

def validateOffset(offsetVal, a,b,c):
    perFlag=0
    negFlag=0
    tempStr=offsetVal.get()
    for i in tempStr:
        if i not in acceptedNum:
            tempStr=tempStr.replace(i, "")
    if tempStr.count('.')>0:
        for i in range(len(tempStr)):
            if tempStr[i]=='.' and perFlag==0:
                perFlag=1
            elif tempStr[i]=='.':
                tempStr=tempStr[:i]+tempStr[i+1:]
                break
    if tempStr.count('-')>0:
        for i in range(len(tempStr)):
            if tempStr[i]=='-' and negFlag==0:
                negFlag=1
            elif tempStr[i]=='-':
                tempStr=tempStr[:i]+tempStr[i+1:]
                break
    if float(tempStr)>1:
        tempStr="1"
    elif float(tempStr)<-1:
        tempStr="-1"
    offsetVal.set(tempStr)

def addPartConv(convParts):
    partConvWind=tk.Tk()
    #part type
    partType=tk.StringVar()
    partType.set(partTypes[0])
    partTypeSelectLabel=tk.Label(partConvWind, text="Select the type of part")
    partTypeSelectLabel.pack()
    partTypeSelectMenu=tk.OptionMenu(partConvWind, partType, *partTypes)
    partTypeSelectMenu.pack()
    #part color selection
    partColor=tk.StringVar()
    partColor.set(partColors[0])
    partColorSelectLabel=tk.Label(partConvWind, text="Select the color of the part")
    partColorSelectLabel.pack()
    partColorSelectMenu=tk.OptionMenu(partConvWind, partColor, *partColors)
    partColorSelectMenu.pack()
    #number
    number=tk.StringVar()
    number.set('0')
    numberLabel=tk.Label(partConvWind, text="Enter the number of parts")
    numberLabel.pack()
    numberEntry=tk.Entry(partConvWind, textvariable=number)
    numberEntry.pack()
    #offset
    offset=tk.StringVar()
    offset.set('0')
    offsetLabel=tk.Label(partConvWind, text="Enter the offset for the part")
    offsetLabel.pack()
    offsetEntry=tk.Entry(partConvWind, textvariable=offset)
    offsetEntry.pack()
    #rotation entry
    partRotation=tk.StringVar()
    partRotation.set('0')
    partRotationLabel=tk.Label(partConvWind, text="Enter the rotation of the part")
    partRotationLabel.pack()
    partRotationEntry=tk.Entry(partConvWind, textvariable=partRotation)
    partRotationEntry.pack()
    #save and cancel buttons
    saveConvButton=tk.Button(partConvWind, text="Save and Exit", command=partConvWind.destroy)
    saveConvButton.pack()
    convPartCancelFlag=tk.StringVar()
    convPartCancelFlag.set('0')
    cancel_new_conv_part=partial(cancel_func, partConvWind, convPartCancelFlag)
    cancelNewPartButton=tk.Button(partConvWind, text="Cancel", command=cancel_new_conv_part)
    cancelNewPartButton.pack(pady=20)
    #entry validation
    validate_rotation=partial(validateRotationValue, partRotation, saveConvButton)
    partRotation.trace('w', validate_rotation)
    validate_offset=partial(validateOffset, offset)
    offset.trace('w', validate_offset)
    partConvWind.mainloop()
    convParts.append(PartConv(partType.get(), partColor.get(),number.get(),offset.get(), partRotation.get()))