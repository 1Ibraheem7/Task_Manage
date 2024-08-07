# Define a class for the contact book
class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        print("\nContact List:")
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")
        print()

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts
                          if search_term.lower() in contact['name'].lower() or
                             search_term in contact['phone']]
        if not found_contacts:
            print("No contacts found.")
        else:
            print("\nSearch Results:")
            for contact in found_contacts:
                self.display_contact(contact)

    def update_contact(self, name):
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                print("Enter new details (leave blank to keep existing):")
                new_name = input("Name: ").strip() or contact['name']
                new_phone = input("Phone: ").strip() or contact['phone']
                new_email = input("Email: ").strip() or contact['email']
                new_address = input("Address: ").strip() or contact['address']
                
                contact.update({
                    "name": new_name,
                    "phone": new_phone,
                    "email": new_email,
                    "address": new_address
                })
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

    def display_contact(self, contact):
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}\n")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            name = input("Enter name: ").strip()
            phone = input("Enter phone number: ").strip()
            email = input("Enter email: ").strip()
            address = input("Enter address: ").strip()
            contact_book.add_contact(name, phone, email, address)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ").strip()
            contact_book.search_contact(search_term)

        elif choice == '4':
            name = input("Enter the name of the contact to update: ").strip()
            contact_book.update_contact(name)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ").strip()
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
