from tkinter import *

class GroceryItems:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class DigiMartGUI:
    def __init__(self, parent):
        self.grocery_list = []
        self.grocery_list.append(GroceryItems("apple", 0))

        quantity = StringVar()

        label_digi_mart = Label(parent, text = "Welcome to DigiMart")
        label_food = Label(parent, text = "how many " + self.grocery_list[0].name + " would you like?")
        entry = Entry(parent, text = "How much would you like")

        label_digi_mart.grid(row = 0, columnspan = 3)
        label_food.grid(row = 1, column = 0)
        entry.grid(row = 1, column = 2)

if __name__ == "__main__":
    root = Tk()
    root.title("DigiMart")
    window = DigiMartGUI(root)
    root.mainloop()