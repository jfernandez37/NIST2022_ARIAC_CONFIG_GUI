import tkinter as tk
from functools import partial

def updateLabel(label, vals, a,b,c):
    currText=label.cget("text")
    newText=currText+" "+str(vals[-1])
    label.config(text=newText)

def updateVals(vals):
    vals.append(vals[-1]+1)
    valsFlag.set(vals[-1]+1)

if __name__=="__main__":
    vals=[0]
    root=tk.Tk()
    valsFlag=tk.StringVar()
    valsFlag.set('0')
    mainLabel=tk.Label(root, text=str(vals[0]))
    mainLabel.pack()
    update_vals=partial(updateVals, vals)
    valsButton=tk.Button(root, text="Add value to vals", command=update_vals)
    valsButton.pack()
    update_label=partial(updateLabel, mainLabel,vals)
    valsFlag.trace('w', update_label)
    root.mainloop()