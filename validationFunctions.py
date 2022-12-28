import tkinter as tk
def validateRotationValue(rotationValue, button, a, b, c):
    """Validates all input for the rpy entries. Activates the save and exit button accordingly"""
    temp_r=rotationValue.get()
    temp_r=temp_r.replace(".","",1)
    pi_flag_r=0
    if temp_r.count("/")==1:
        temp_r_split=temp_r.split("/")
        if temp_r_split[0]=="pi" and temp_r_split[1].isnumeric():
            pi_flag_r=1
    if (pi_flag_r==1 or temp_r.isnumeric()) and button['state']==tk.DISABLED:
        button.config(state=tk.NORMAL)
    elif button['state']==tk.NORMAL:
        button.config(state=tk.DISABLED)
        
def add_quotes(strVar):
    """Formats the rpy values correctly"""
    tempStr=strVar.get()
    tempStr=tempStr.lower()
    if 'pi' in tempStr:
        tempStr=tempStr.replace("\"", "")
        tempStr=tempStr.replace("\'", "")
        if tempStr[0]!="\'":
            tempStr="\'"+tempStr
        if tempStr[len(tempStr)-1]!="\'":
            tempStr=tempStr+"\'"
    strVar.set(tempStr)