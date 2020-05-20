from tkinter import *

class GroceryItems:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class DigiMartGUI:
    def __init__(self, parent):
        self.grocery_list = []
        self.grocery_list.append(GroceryItems("apple", 0))

        def confirm_quantity():
            self.quantity = int(entry.get())
            
        label_digi_mart = Label(parent, text = "Welcome to DigiMart")
        label_food = Label(parent, text = "how many " + self.grocery_list[0].name + "s would you like?")
        label_test = Label(parent, text = "test")

        button_confirm_quantity = Button(parent, text = "confirm", command = confirm_quantity)
        entry = Entry(parent, text = "How much would you like")

        label_digi_mart.grid(row = 0, columnspan = 3)
        label_food.grid(row = 1, column = 0)
        label_test.grid(row = 2, column = 3)

        button_confirm_quantity.grid(row = 1, column = 3)
        entry.grid(row = 1, column = 2)



if __name__ == "__main__":
    root = Tk()
    root.title("DigiMart")
    window = DigiMartGUI(root)
    root.mainloop()