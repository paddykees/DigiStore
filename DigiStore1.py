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

        #dropdown menu list, cant use grocery list since item list needs only strings to work and grocery list is objects
        item_list = []

        #Adds the name from the objects of the grocery list to the item list
        for i in  range(len(self.grocery_list)):
            item_list.append(self.grocery_list[i].name)

        self.shopping_list = []
        #labels that display on the GUI, helps the USER understand what is going on
        label_digi_mart = Label(parent, text = "Welcome to DigiMart")
        self.label_food = Label(parent, text = "please pick an option from the dropdown menu")
        self.label_test = Label(parent, text = "text")

        #Allows the USER to interact with the program by being able o input intergers and pressing a button to confirm. 
        #A label on line 18 is configured to change and display the result entered into the entry widget
        button_confirm_quantity = Button(parent, text = "confirm", command = self.confirm_quantity)
        self.entry = Entry(parent, text = "How much would you like")

        self.fruit = StringVar()

        menu_fruit = OptionMenu(parent, self.fruit, *item_list, command = self.update_label_food)

        #Configures the position of the labels in the program
        label_digi_mart.grid(row = 0, columnspan = 4)
        self.label_food.grid(row = 1, column = 2)
        self.label_test.grid(row = 3, column = 3)

        #Configures the position of the buttons, dropdown menus and entry widgets in the program
        button_confirm_quantity.grid(row = 1, column = 4)
        self.entry.grid(row = 1, column = 3)
        menu_fruit.grid(row = 1, column = 1)

        #sets the defualt dropdown text when the program first loads
        self.fruit.set("please select an option")

    #method that defines what the button does when pressed
    def confirm_quantity(self):
        try:
            #defines quantity as the interger typed into the the entry widget when the button is pressed
            self.quantity = int(self.entry.get())

            #configures the test label to allow USER check that entry widget/button works as intended, not intended to be a part of final release
            self.label_test.configure(text = int(self.entry.get()))

            self.shopping_list.append(GroceryItems(self.fruit.get(), self.entry.get()))

            #clears entry widget after data has been stored
            self.entry.delete(0, 'end')
        except:
            self.label_test.configure(text = "please enter a valid interger")
    
    def update_label_food(self, name):
        self.label_food.configure(text = "how many " + self.fruit.get() + "s would you like?")


#creates GUI window
if __name__ == "__main__":
    root = Tk()
    root.title("DigiMart")
    window = DigiMartGUI(root)
    root.mainloop()