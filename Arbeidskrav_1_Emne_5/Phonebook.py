import json
from datetime import datetime
from prettytable import PrettyTable
from Arbeidskrav_1_Emne_5.Contact import Contact

class Phonebook:
    def __init__(self):
        self.contacts = [None] * 100
        self.count = 0
        self.max_size = 100

    def __getitem__(self, index):
        if 0 <= index < len(self.contacts):
            return self.contacts[index]
        else:
            raise IndexError("Index out of range.")

    def add_contact(self, contact):
        if self.count < self.max_size:
            self.contacts[self.count] = contact
            self.count += 1
            return True
        else:
            print(f"Phonebook is full. {contact.first_name} {contact.last_name} was NOT added!")
            return False

    def display_all_contacts(self):
        t = PrettyTable(["First Name", "Last Name", "Phone", "Birthday", "Street", "City"])
        for contact in self.contacts:
            if contact is None:
                continue
            t.add_row([contact.first_name, contact.last_name, contact.phone, contact.birthday, contact.street, contact.city])
        t.align = 'l'
        return t

    def search_contact(self, query):
        if not isinstance(query, str):
            print("Query must be a string.")
            return False
        found = False
        results = []
        search_input = query.lower()
        for contact in self.contacts:
            if contact is None:
                continue
            contact_properties = [contact.first_name, contact.last_name, contact.phone, contact.birthday, contact.street, contact.city]
            if any(search_input in s.lower() for s in contact_properties):
                results.append(contact.display())
                found = True

        if not found:
            print(f"No results in phonebook with query '{query}'.")

        return '\n'.join(results)

    def sort_contacts(self, sort_by, asc_desc):
        valid_sortby = False
        sort_options = {
            'firstname': 'first_name',
            'lastname': 'last_name',
            'phone': 'phone',
            'street': 'street',
            'city': 'city',
            'birthday': '_birthday'
        }

        if sort_by in sort_options:
            valid_sortby = True
            sort_key = sort_options[sort_by]

            sort_order = asc_desc == 'desc'
            self.contacts = [ contact for contact in self.contacts if contact is not None ]
            self.contacts.sort(key=lambda contact: getattr(contact, sort_key), reverse=sort_order)

            order = "descending" if sort_order else "ascending"
            print(f"Contacts sorted {order} by {sort_by}:")
        else:
            print(f"Invalid sort option: {sort_by}. Please choose from {list(sort_options.keys())}.")

        return valid_sortby

    def import_contacts_from_jsonl_file(self, filename):
        try:
            contacts_added = 0
            contacts_failed = 0
            with open(filename, "r") as f:
                for line in f:
                    contact_data = json.loads(line)
                    if contact_data['birthday']:
                        contact_data['birthday'] = datetime.strptime(contact_data['birthday'], '%Y-%m-%d')
                    contact = Contact(**contact_data)
                    if self.add_contact(contact):
                        contacts_added += 1
                    else:
                        contacts_failed += 1
            print(f"{contacts_added} contacts imported successfully. Failed: {contacts_failed}\n")
        except FileNotFoundError:
            print("File not found.")