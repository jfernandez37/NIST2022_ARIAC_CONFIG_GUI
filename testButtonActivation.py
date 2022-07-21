import tkinter as tk
from functools import partial

arr = []

def increaseArr(arrFlag):
    arr.append(0)
    print(arr)
    if len(arr)%5==0:
        arrFlag.set('1')
    else:
        arrFlag.set('0')

def activateButton(button, parFlag, c, d, e):
    if parFlag.get() == '1':
        button.config(state=tk.NORMAL)
    else:
        button.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    arrFlag = tk.StringVar()
    arrFlag.set('0')
    increaseMainFunc = partial(increaseArr, arrFlag)
    increaseArrButton = tk.Button(root, text = "Increase Arr", command=increaseMainFunc)
    increaseArrButton.pack()
    saveButton = tk.Button(root, text = "Save and Exit", command = root.destroy, state=tk.DISABLED)
    saveButton.pack()
    activateButtonFunc = partial(activateButton, saveButton, arrFlag)
    arrFlag.trace('w', activateButtonFunc)
    root.mainloop()
    print("OUT OF LOOP. Final Arr length: "+ str(len(arr)))
