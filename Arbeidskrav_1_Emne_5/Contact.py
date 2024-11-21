from datetime import datetime

class Contact:
    def __init__(self, first_name, last_name, phone, birthday, street, city):
        self._first_name = first_name
        self._last_name = last_name
        self._phone = phone
        self._birthday = birthday if isinstance(birthday, datetime) else datetime.strptime(birthday, '%Y-%m-%d')
        self._street = street
        self._city = city

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def phone(self):
        return self._phone

    @property
    def birthday(self):
        return self._birthday.strftime('%d.%m.%Y') if isinstance(self._birthday, datetime) else "Not valid"

    @property
    def street(self):
        return self._street

    @property
    def city(self):
        return self._city

    def display(self):
        return (f"Name: {self.first_name} {self.last_name}, "
                f"Phone: {self.phone}, Birthday: {self.birthday}, "
                f"Address: {self.street}, {self.city}")