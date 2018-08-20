import con_mysql.conn as connected
from tkinter import *
from win32api import GetSystemMetrics
from con_mysql.frames.btn_class import BtnIngre

app_width = 1000
app_height = 330

root = Tk()
root.title('MaxiDesk')
root.geometry(str(app_width) + 'x' + str(app_height) + '+' + str(int(GetSystemMetrics(0)/2 - 500)) + '+' + str(int(GetSystemMetrics(1)/2 - 250)))
root.resizable(False, False)

relative_fram = Frame(root, height=app_height)
relative_fram.pack(fill=BOTH)

can = Canvas(relative_fram, bg='red', height=40, width=50)
can.pack()


'''
second_frame = Frame(can, bg='blue', height=50)
second_frame.pack(fill=BOTH)
'''

root.mainloop()