#Q3. Create a program that a user can use to manage the primary email address and phone number for a contact.

#a.multi-dimensional list to store the contacts
contacts = [
    ["John", "john@example.com", "123-456-7890"],
    ["Jane", "jane@example.com", "098-765-4321"],
    ["Johny", "johny@example.com", "111-222-3333"],
    ["Jack", "jack@example.com", "444-555-6666"],
    ["James", "james@example.com", "777-888-9999"]
]
 #Functionality to display a menu and let user select a command.
def display_menu():
    print("Commands:")
    print("list    - Display all contacts")
    print("view - View a contact")
    print("add   - Add a contact")
    print("del    - Delete a contact")
    print("exit   - Exit program")

def list_names():
    for i, contact in enumerate(contacts):
        print(f"{i+1}. {contacts[i][0]}")

def view_contacts():
        for i, contact in enumerate(contacts):
            print(f"\n Name: {contact[0]} Email: {contact[1]} Phone: {contact[2]}" )

def add_contacts():
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    contacts.append([name, email, phone])
    print(f"Contact {name} was added.")

def del_contact(index):
    name = contacts[index][0]
    del contacts[index]
    print(f"Contact {name} deleted.")
    return

def main():
    display_menu()
    while True: 
        command = input("Enter command: ")
        if command == "list":
            list_names()
        elif command == "view":
            view_contacts()
        elif command == "add":
            add_contacts()
        elif command == "del":
            print("Eneter the number of contact to delete: ")
            index = int(input())
            if index <= len(contacts):
                del_contact(index - 1)
            else:
                print("Invalid number.")
        elif command == "exit":
            print("Bye.")
            break
        else:
            print("Invalid command. Please try again.")

main()

    
#b.  For the view and del commands, display an error message if the user enters an invalid contact number.

#c. When you exit the program, all changes that you made to the contact list are lost.