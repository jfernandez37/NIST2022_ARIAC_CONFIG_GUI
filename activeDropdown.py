import tkinter as tk
from functools import partial

from matplotlib.pyplot import text
arr1 = ['1', '2', '3']
arr2 = ['4', '5', '6']


def app():
    root = tk.Tk()
    testString = tk.StringVar()
    testString.set('')
    arrAns = tk.StringVar()
    arrChoice = tk.StringVar()
    arrChoice.set('0')
    arrChoiceMenu = tk.OptionMenu(root, arrChoice, '0', '1')
    arrChoiceMenu.pack()
    print(arrChoice.get())
    printTestString = partial(printStr, testString)
    testEntry = tk.Entry(root, textvariable=testString)
    testEntry.pack()
    if arrChoice.get() == '0':
        arrAns.set(arr1[0])
        mainDropDown = tk.OptionMenu(root, arrAns, *arr1)
        mainDropDown.configure(state='active')
    else:
        arrAns.set(arr2[0])
        mainDropDown = tk.OptionMenu(root, arrAns, *arr2)
        mainDropDown.configure(state='active')
    mainDropDown.pack()
    action_with_arg = partial(change_menu, mainDropDown, arrChoice, arrAns)
    arrChoice.trace('w', action_with_arg)
    testString.trace('w', printTestString)
    root.mainloop()


def change_menu(a, b, c, d, e, f):
    menu = a['menu']
    menu.delete(0, 'end')
    if b.get() == '0':
        c.set(arr1[0])
        for i in arr1:
            menu.add_command(label=i, command=lambda i=i: c.set(i))
    else:
        c.set(arr2[0])
        for i in arr2:
            menu.add_command(label=i, command=lambda i=i: c.set(i))


def printStr(stringTemp, a, b, c):
    tempStr = stringTemp.get()
    for character in tempStr:
        if character == 't':
            tempStr=tempStr.replace('t', '')
    print(tempStr)
    stringTemp.set(tempStr)


if __name__ == '__main__':
    app()
