from tkinter import *

class GroceryItems:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class DigiMartGUI:
    def __init__(self, parent):
        self.grocery_list = []
        self.grocery_list.append(GroceryItems("apple", 0))
            
        label_digi_mart = Label(parent, text = "Welcome to DigiMart")
        label_food = Label(parent, text = "how many " + self.grocery_list[0].name + "s would you like?")
        self.label_test = Label(parent, text = "text")

        button_confirm_quantity = Button(parent, text = "confirm", command = self.confirm_quantity)
        self.entry = Entry(parent, text = "How much would you like")

        label_digi_mart.grid(row = 0, columnspan = 3)
        label_food.grid(row = 1, column = 0)
        self.label_test.grid(row = 2, column = 3)

        button_confirm_quantity.grid(row = 1, column = 3)
        self.entry.grid(row = 1, column = 2)
    
    def confirm_quantity(self):
        self.quantity = int(self.entry.get())
        self.label_test.configure(text = int(self.entry.get()))



if __name__ == "__main__":
    root = Tk()
    root.title("DigiMart")
    window = DigiMartGUI(root)
    root.mainloop()