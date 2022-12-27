import tkinter as tk
acceptedNum = "0123456789"  # for requiring positive numbers for time
def updateTimeInputBox(val, box, a,b,c):
    if val.get()=="1":
        box.configure(state="disabled")
    else:
        box.configure(state="normal")

def validateTime(val,a,b,c):
    tempStr=val.get()
    for i in tempStr:
        if i not in acceptedNum:
            tempStr=tempStr.replace(i, "")
    if tempStr!="":
        numVal=int(tempStr)
        if numVal>500:
            tempStr="500"
        elif numVal<0:
            tempStr="0"
    val.set(tempStr)