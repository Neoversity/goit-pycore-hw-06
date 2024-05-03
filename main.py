from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)



class Name(Field):
    def __init__(self, value):
        super().__init__(value)




class Phone(Field):
    def __init__(self, value):
        try:
            self.validate(value)
        except ValueError as e:
            print(e)  # Вивести повідомлення про помилку
            # Можливо, захочете виконати інші дії, якщо виникає помилка
        super().__init__(value)

    @staticmethod
    def validate(value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must be 10 digits and contain only digits")
       


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        try:
            Phone.validate(phone)
            self.phones.append(Phone(phone))
        except ValueError as e:
            print(e)

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != phone]

    def edit_phone(self, old_phone, new_phone):
        try:
            Phone.validate(new_phone)
            for phone in self.phones:
                if str(phone) == old_phone:
                    phone.value = new_phone
                    return
            print(f"Phone number {old_phone} not found.")
        except ValueError as e:
            print(e)

    def find_phone(self, phone):
        for p in self.phones:
            if str(p) == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"





class AddressBook(UserDict):
    def add_record(self, record):
        if not isinstance(record, Record):
            raise ValueError("Only Record objects can be added to AddressBook")
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]







# Створення нової адресної книги
book = AddressBook()


# Створення запису для My
my_record = Record("My")
my_record.add_phone("123456789011")
my_record.add_phone("5555555555")
my_record.edit_phone("5555555555", "555555555511")

# Додавання запису My до адресної книги
book.add_record(my_record)


# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")

