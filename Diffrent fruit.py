from tkinter import *

class GroceryItems:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class DigiMartGUI:
    def __init__(self, parent):
        self.grocery_list = []

        self.grocery_list.append(GroceryItems("apple", 0))
        self.grocery_list.append(GroceryItems("orange", 0))
        self.grocery_list.append(GroceryItems("mango", 0))
        self.grocery_list.append(GroceryItems("pear", 0))
        self.grocery_list.append(GroceryItems("berry", 0))

        item_list = []

        for i in  range(len(self.grocery_list)):
            item_list.append(self.grocery_list[i].name)

        self.fruit = StringVar()

        menu_fruit = OptionMenu(parent, self.fruit, *item_list, command = self.label_update)
        menu_fruit.pack()

        self.fruit.set("please select an option")

        self.label = Label(parent, text = "fruit")
        self.label.pack()
    
    def label_update(self, name):
        self.label.configure(text = self.fruit.get())






if __name__ == "__main__":
    root = Tk()
    root.title("DigiMart")
    window = DigiMartGUI(root)
    root.mainloop()