### Assignment 4: Wizard Inventory Program
### Author: Niyati Jain
#!/usr/bin/env python3

#function to display the title
def display_title():
    print("The Wizard Inventory Program")
#function to display command menu
def display_command_menu():
    print("COMMAND MENU")
    print("show - Show all items")
    print("grab - Grab an item")
    print("drop - Drop an item")
    print("exit - Exit program")

#function to show inventory
def show(inventory):
    print(inventory)

#function to add item to the inventory
def grab(inventory):
    item = input("Enter the item name:")
    if(len(inventory) == 4):
        print("Max item reached. Please drop something")
    else:
        inventory.append(item)
        print(item," was added")
        
#function to remove item from the inventory
def drop(inventory):
    item=input("Enter the item number: ")
    if(int(item)<1 or int(item)>len(inventory)):
        print("Invalid item number")
    else:
        print(inventory[int(item) - 1],"was dropped" )
        inventory.pop(int(item) - 1)

#main function
def main():
    inventory = ["sorting hat", "invisible cloak", "wand"]
    display_title()
    display_command_menu()
    while True:
        command = input("COMMAND:")
        if(command.lower() == "show"):
            show(inventory)
        if(command.lower() == "grab"):
            grab(inventory)
        if(command.lower() == "drop"):
            drop(inventory)
        if(command.lower() == "exit"):
            break
    
if __name__ == "__main__":
    main()
