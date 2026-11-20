# Program 8: Contact Book Using Lists and Dictionaries

contacts = []

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone number: ").strip()
    email = input("Email (optional): ").strip()
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added.")

def view_contacts():
    if not contacts:
        print("No contacts saved.")
        return
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']} | {contact['phone']} | {contact['email']}")

def search_contact():
    term = input("Enter a name to search: ").strip().lower()
    matches = [c for c in contacts if term in c["name"].lower()]
    if matches:
        for contact in matches:
            print(contact)
    else:
        print("No matching contact found.")

while True:
    print("\n=== Contact Book ===")
    print("1. Add contact\n2. View contacts\n3. Search contact\n4. Exit")
    choice = input("Choose: ").strip()
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
