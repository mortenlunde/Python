from datetime import datetime

class Contact:
    def __init__(self, FirstName, LastName, Phone, Birthday, Street, City):
        self._first_name = FirstName
        self._last_name = LastName
        self._phone = Phone
        self._birthday = Birthday
        self._street = Street
        self._city = City

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
        return self._birthday

    @property
    def street(self):
        return self._street

    @property
    def city(self):
        return self._city

    def display(self):
        if isinstance(self._birthday, datetime):
            birthday_str = self._birthday.strftime('%d.%m.%Y')
        else:
            birthday_str = "Not valid"
        return (f"Name: {self.first_name} {self.last_name}, "
                f"Phone: {self.phone}, Birthday: {birthday_str}, "
                f"Address: {self.street}, {self.city}")