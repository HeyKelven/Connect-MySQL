import con_mysql.conn as connected
from tkinter import *
from win32api import GetSystemMetrics
from con_mysql.frames.btn_class import BtnIngre

app_width = 1000
app_height = GetSystemMetrics(1)


def down(event):
    principal_canvas.configure(scrollregion=principal_canvas.bbox("all"), width=1000, height=300)


def enable_list(list):
    for unit in list:
        unit.config(state=NORMAL)


root = Tk()
root.title('MaxiDesk')
root.geometry(str(app_width) + 'x' + str(app_height) + '+' + str(int(GetSystemMetrics(0)/2 - 500)) + '+0')
root.resizable(TRUE, TRUE)


labelText = StringVar()
labelText.set("INSERT INTO montagem (id_ingre, id) VALUES ;")

relative_frame = Frame(root, bg='blue', height=60)
relative_frame.pack(fill=BOTH)

relative_canvas = Canvas(relative_frame, bg='red', width=app_width)
relative_canvas.pack(side=LEFT)

# Pizzaria
child_relative_canvas = Frame(relative_canvas, bg='yellow', height=200, width=app_width/2)
child_relative_canvas.grid(row=0, column=0, sticky=NW)
child_relative_canvas.pack_propagate(FALSE)

label_name = Label(child_relative_canvas, text="Nome da pizzaria para adicionar").pack()
name_pizzaria = Entry(child_relative_canvas, width=40, font=("arial", 14))
name_pizzaria.pack()

create_pizzaria = Button(child_relative_canvas, text="Create", command=lambda: [connected.create_new_pizzaria(name_pizzaria.get(), voss)])
create_pizzaria.pack()

voss = StringVar()
label_result = Label(child_relative_canvas, textvariable=voss).pack(pady=20)

voss.set("12")


# Pizzas
child_relative_canvas2 = Frame(relative_canvas, bg='purple', height=80, width=app_width/2)
child_relative_canvas2.grid(row=0, column=1)
child_relative_canvas2.pack_propagate(FALSE)

label_pizza = Label(child_relative_canvas2, text="Nome").grid(row=0, column=0)
name_sabor = Entry(child_relative_canvas2, width=40, font=("arial", 14))
name_sabor.grid(row=0, column=1)

label_type = Label(child_relative_canvas2, text="Tipo").grid(row=1, column=0)
set_type = Entry(child_relative_canvas2, width=40, font=("arial", 14))
set_type.insert(END, 'Carnívora')
set_type.grid(row=1, column=1)

label_heigth = Label(child_relative_canvas2, text="Tamanho").grid(row=2, column=0)
set_heigth = Entry(child_relative_canvas2, width=40, font=("arial", 14))
set_heigth.insert(END, 'Grande')
set_heigth.grid(row=2, column=1)

label_price = Label(child_relative_canvas2, text="Preço").grid(row=3, column=0)
set_price = Entry(child_relative_canvas2, width=40, font=("arial", 14))
set_price.grid(row=3, column=1)

label_time = Label(child_relative_canvas2, text="Tempo").grid(row=4, column=0)
set_time = Entry(child_relative_canvas2, width=40, font=("arial", 14))
set_time.grid(row=4, column=1)

name_pizza = StringVar()

resul_lab = Label(child_relative_canvas2, textvariable=name_pizza).grid(row=5, column=1)

create_pizza = Button(child_relative_canvas2, text="Search", command=lambda: [
    connected.create_new_pizza(name_sabor.get(), set_type.get(), set_heigth.get(),
                               set_price.get(), set_time.get(),voss.get(), name_pizza), enable_list(list)])
create_pizza.grid(row=5, column=0)

name_pizza.set("Id Pizzaria")


principal_frame = Frame(root).pack(fill=BOTH)
principal_canvas = Canvas(principal_frame)
second_frame = Frame(principal_canvas)

ind2 = 0
list = []
for ind, row in enumerate(connected.get_ingredients()):
    if ind == ind2 * 8 + 8:
        ind2 += 1
    op = BtnIngre(row[1], row[0])
    op_btn = op.create_btn(second_frame, ind2, ind - ind2 * 8, labelText, name_pizza)
    list.append(op_btn)

scroll = Scrollbar(principal_frame, orient='vertical', command=principal_canvas.yview)
principal_canvas.configure(yscrollcommand=scroll.set)
scroll.pack(side='right', fill=Y)
principal_canvas.pack()
principal_canvas.create_window((0, 0), window=second_frame)
second_frame.bind('<Configure>', down)

final_frame = Frame(root, height=20, width=app_width)
final_frame.pack()

k = Label(final_frame, textvariable=labelText, font=("Helvetica", 14), wraplength=900)
k.pack(anchor='w')

Button(final_frame, text="Insert this pizza", font=("Helvetica", 16), command=lambda: connected.insert_montagem(labelText)).pack(anchor='s')

root.mainloop()