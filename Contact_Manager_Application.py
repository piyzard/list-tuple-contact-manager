contacts = []


def addContact(name, phone, email):
    for contact in contacts:
        if contact[0] == name:
            print("\nName already exists.")
            return
    contacts.append((name, phone, email))
    print("\nContact added.")

def viewContacts():
    if not contacts:
        print("\nNo contacts found.")
        return
    print("\nList of Contacts:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact[0]} - {contact[1]} - {contact[2]}")

def searchContact(name):
    for contact in contacts:
        if contact[0] == name:
            print(f"\nContact Found: {contact[0]} - {contact[1]} - {contact[2]}")
            return
    print("\nContact not found.")

def updateContact(name, newPhone):
    for i, contact in enumerate(contacts):
        if contact[0] == name:
            contacts[i] = contact([0], newPhone, contact[2])
            print("\nContact updated successfully.")
            return
    print("\nContact not found.")

def deleteContact(name):
    for i, contact in enumerate(contacts):
        if contact[0] == name:
            contacts.pop(i)
            print("\nContact deleted successfully.")
            return
    print("\nContact not found")

def contactManager():
    while True:
        print("""
            Welcome to Contact Manager.
            1. Add Contact
            2. View Contacts
            3. Search Contact
            4. Update Contact
            5. Delete Contact
            6. Exit
        """)

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            name = input("\nEnter Name: ")
            phone = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            addContact(name, phone, email)
        elif choice == 2:
            viewContacts()
        elif choice == 3:
            name = input("\nEnter name to search: ")
            searchContact(name)
        elif choice == 4:
            name = input("\nEnter name to update: ")
            new_phone = input("Enter new phone number: ")
            updateContact(name, new_phone)
        elif choice == 5:
            name = input("\nEnter name to delete: ")
            deleteContact(name)
        elif choice == 6:
            print("\nExiting Contact Manager.")
            break
        else:
            print("\nInvalid choice. Please try again.")


contactManager()