from tkinter import *

class GroceryItems:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class DigiMartGUI:
    def __init__(self, parent):
        pass
        print("hello world")

if __name__ == "__main__":
    root = Tk()
    root.title("DigiMart")
    window = DigiMartGUI(root)
    root.mainloop()