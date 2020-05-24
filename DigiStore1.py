#imports tkinter class so I can make use of it feature allowing me to easily build a GUI
from tkinter import *

#Support class defines properties of the object fruit and will later be expanded to include all the diffrent properties of items in a groccer
class GroceryItems:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

#defines GUI, needed to display the options so the USER can interact with it. responsible for the diffrent properties
class DigiMartGUI:
    def __init__(self, parent):
        #creates the grocery list, houses all the diffrent food objects
        self.grocery_list = []

        #adds food objects to the grocery list
        self.grocery_list.append(GroceryItems("apple", 0))
        self.grocery_list.append(GroceryItems("orange", 0))
        self.grocery_list.append(GroceryItems("mango", 0))
        self.grocery_list.append(GroceryItems("pear", 0))
        self.grocery_list.append(GroceryItems("berry", 0))
        #labels that display on the GUI, helps the USER understand what is going on
        label_digi_mart = Label(parent, text = "Welcome to DigiMart")
        label_food = Label(parent, text = "how many " + self.grocery_list[0].name + "s would you like?")
        self.label_test = Label(parent, text = "text")

        #Allows the USER to interact with the program by being able o input intergers and pressing a button to confirm. 
        #A label on line 18 is configured to change and display the result entered into the entry widget
        button_confirm_quantity = Button(parent, text = "confirm", command = self.confirm_quantity)
        self.entry = Entry(parent, text = "How much would you like")

        #Configures the position of the labels in the program
        label_digi_mart.grid(row = 0, columnspan = 3)
        label_food.grid(row = 1, column = 0)
        self.label_test.grid(row = 2, column = 3)

        #Configures the position of the buttons and entry widgets in the program
        button_confirm_quantity.grid(row = 1, column = 3)
        self.entry.grid(row = 1, column = 2)



    #method that defines what the button does when pressed
    def confirm_quantity(self):
        try:
            #defines quantity as the interger typed into the the entry widget when the button is pressed
            self.quantity = int(self.entry.get())

            #configures the test label to allow USER check that entry widget/button works as intended, not intended to be a part of final release
            self.label_test.configure(text = int(self.entry.get()))

            #clears entry widget after data has been stored
            self.entry.delete(0, 'end')
        except:
            self.label_test.configure(text = "please enter a valid interger")
#creates GUI window
if __name__ == "__main__":
    root = Tk()
    root.title("DigiMart")
    window = DigiMartGUI(root)
    root.mainloop()