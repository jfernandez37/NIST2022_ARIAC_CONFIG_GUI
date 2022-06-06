import tkinter as tk

arr1 = ['1', '2', '3']
arr2 = ['4', '5', '6']


def change_menu(a, b, c):
    menu = mainDropDown['menu']
    menu.delete(0, 'end')
    if arrChoice.get() == '0':
        arrAns.set(arr1[0])
        for i in arr1:
            menu.add_command(label=i, command=lambda i=i: arrAns.set(i))
    else:
        arrAns.set(arr2[0])
        for i in arr2:
            menu.add_command(label=i, command=lambda i=i: arrAns.set(i))


if __name__ == '__main__':
    root = tk.Tk()
    arrAns = tk.StringVar()
    arrChoice = tk.StringVar()
    arrChoice.set('0')
    arrChoiceMenu = tk.OptionMenu(root, arrChoice, '0', '1')
    arrChoiceMenu.pack()
    arrChoice.trace('w', change_menu)
    print(arrChoice.get())
    if arrChoice.get() == '0':
        arrAns.set(arr1[0])
        mainDropDown = tk.OptionMenu(root, arrAns, *arr1)
        mainDropDown.configure(state='active')
    else:
        arrAns.set(arr2[0])
        mainDropDown = tk.OptionMenu(root, arrAns, *arr2)
        mainDropDown.configure(state='active')
    mainDropDown.pack()
    root.mainloop()
