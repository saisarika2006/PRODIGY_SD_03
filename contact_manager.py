print("Program started")

import json
import os

FILE_NAME = "contacts.json"

def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })

    save_contacts(contacts)
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    for i, c in enumerate(contacts, start=1):
        print(f"\n{i}. {c['name']} | {c['phone']} | {c['email']}")

def main():
    contacts = load_contacts()

    while True:
        print("\n📞 Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
