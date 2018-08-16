import con_mysql.conn as connected
from tkinter import *
from win32api import GetSystemMetrics
from con_mysql.frames.btn_class import BtnIngre

app_width = 1000
app_height = 330


def down(event):
    principal_canvas.configure(scrollregion=principal_canvas.bbox("all"), width=1000, height=300)


root = Tk()
root.title('MaxiDesk')
root.geometry(str(app_width) + 'x' + str(app_height) + '+' + str(int(GetSystemMetrics(0)/2 - 500)) + '+' + str(int(GetSystemMetrics(1)/2 - 250)))
root.resizable(False, False)

relative_frame = Frame(root, height=30).pack(fill=BOTH)
labelText = StringVar()
labelText.set("Nenhum;")
k = Label(relative_frame, textvariable=labelText).pack()


principal_frame = Frame(root).pack(fill=BOTH)
principal_canvas = Canvas(principal_frame)
second_frame = Frame(principal_canvas)

ind2 = 0
for ind, row in enumerate(connected.get_ingredients()):
    if ind == ind2 * 8 + 8:
        ind2 += 1
    op = BtnIngre(row[1], row[0])
    op.create_btn(second_frame, ind2, ind - ind2 * 8, labelText)

scroll = Scrollbar(principal_frame, orient='vertical', command=principal_canvas.yview)
principal_canvas.configure(yscrollcommand=scroll.set)
scroll.pack(side='right', fill=Y)
principal_canvas.pack()
principal_canvas.create_window((0, 0), window=second_frame)
second_frame.bind('<Configure>', down)

root.mainloop()