import json
from datetime import datetime
from Arbeidskrav_1_Emne_5_Tkinter.Contact import Contact
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

    def get_all_contacts(self):
        return [
            (
                contact.first_name,
                contact.last_name,
                contact.phone,
                contact.birthday.strftime('%d.%m.%Y') if isinstance(contact.birthday, datetime) else contact.birthday,
                contact.street,
                contact.city
            )
            for contact in self.contacts if contact
        ]

    def search_contact(self, name):
        search_input = name.lower()
        return [
            (
                contact.first_name,
                contact.last_name,
                contact.phone,
                contact.birthday.strftime('%d.%m.%Y') if isinstance(contact.birthday, datetime) else contact.birthday,
                contact.street,
                contact.city
            )
            for contact in self.contacts if contact and any(search_input in s.lower() for s in (
                contact.first_name, contact.last_name, contact.phone,
                contact.birthday.strftime('%d.%m.%Y') if isinstance(contact.birthday, datetime) else contact.birthday,
                contact.street, contact.city))
        ]

    def sort_contacts(self, sort_by, asc_desc):
        sort_options = {
            'firstname': 'first_name',
            'lastname': 'last_name',
            'phone': 'phone',
            'street': 'street',
            'city': 'city',
            'birthday': 'birthday'
        }

        if sort_by in sort_options:
            sort_key = sort_options[sort_by]
            reverse = asc_desc == 'desc'
            self.contacts = [contact for contact in self.contacts if contact is not None]
            self.contacts.sort(key=lambda contact: getattr(contact, sort_key), reverse=reverse)
            return True
        else:
            print(f"Invalid sort option: {sort_by}. Please choose from {list(sort_options.keys())}.")
            return False

    def import_contacts_from_jsonl_file(self, filename):
        try:
            contacts_added = 0
            with open(filename, "r") as f:
                for line in f:
                    contact_data = json.loads(line)
                    if 'birthday' in contact_data and contact_data['birthday']:
                        contact_data['birthday'] = datetime.strptime(contact_data['birthday'], '%Y-%m-%d')
                    contact = Contact(**contact_data)
                    if self.add_contact(contact):
                        contacts_added += 1
            print(f"Contacts imported successfully ({contacts_added}).\n")
        except FileNotFoundError:
            print("File not found.")