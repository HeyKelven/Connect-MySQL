from tkinter import *


class BtnIngre():

    def __init__(self, name_ingre, id_ingre):
        self.__name = name_ingre
        self.__id = id_ingre

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def put_there(self, ko, id_pizza):
        ko.set(ko.get()[: -1] + " (" + str(self.get_id()) + ", " + str(id_pizza.get()) + "),;")

    def create_btn(self, relative_frame, ind, ind2, the_string, id_pizza):
        x = Button(relative_frame, text=self.get_name(), state=NORMAL, width=15, command=lambda: [self.put_there(the_string, id_pizza), x.config(state=DISABLED)])
        x.grid(row=ind, column=ind2, padx=(0, 7), pady=(3, 3))
        return x