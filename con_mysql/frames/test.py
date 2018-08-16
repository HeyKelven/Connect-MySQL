from tkinter import *

root = Tk()

root.geometry('300x300+20+20')

global currentpage
global pagecount
currentpage = 1
pagecount = 5

v = StringVar()
Label(root, textvariable=v).place(x=20, y=10)
v.set(str(currentpage))


def page_up():
    """
    subtract 1 from displayed number,
    disable Btn1 button when currentpage reaches 1
    """
    global currentpage, pagecount

    currentpage -= 1

    if currentpage == 1:
        Btn1.config(state=DISABLED)

    if Btn2["state"] != "normal":
        Btn2.config(state=NORMAL)  # button to page down is enabled

    v.set(str(currentpage))


def page_down():
    """
    add 1 to displayed number,
    disable Btn2 button when currentpage reaches pagecount
    """
    global currentpage, pagecount

    currentpage += 1

    if currentpage >= pagecount:
        Btn2.config(state=DISABLED)

    if Btn1["state"] != "normal":
        Btn1.config(state=NORMAL)  # button to page up is enabled

    v.set(str(currentpage))


Btn1 = Button(text="Page Up", padx=16, pady=8, command=page_up)
Btn1.pack()
Btn1.place(x=60, y=10)
Btn1.config(state=DISABLED)

Btn2 = Button(text="Page Down", padx=8, pady=6, command=page_down)
Btn2.pack()
Btn2.place(x=60, y=60)

root.mainloop()