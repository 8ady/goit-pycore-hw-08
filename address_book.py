import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __repr__(self):
        return f"Person(name='{self.name}', email='{self.email}', phone='{self.phone}', favorite={self.favorite})"


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, person: Person):
        self.contacts.append(person)

    def remove_contact(self, person: Person):
        self.contacts.remove(person)

    def find_contact_by_name(self, name: str):
        return [contact for contact in self.contacts if name.lower() in contact.name.lower()]

    def __repr__(self):
        return f"AddressBook(contacts={self.contacts})"

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  

def main():

    book = load_data()

    book.add_contact(Person("Allen Raymond", "nulla.ante@vestibul.co.uk", "(992) 914-3792", False))
    book.add_contact(Person("Chaim Lewis", "dui.in@egetlacus.ca", "(294) 840-6685", False))
    book.add_contact(Person("Kennedy Lane", "mattis.Cras@nonenimMauris.net", "(542) 451-7038", True))

    
    print("Контакти в адресній книзі:")
    for contact in book.contacts:
        print(contact)

    name_to_search = "Kennedy"
    found_contacts = book.find_contact_by_name(name_to_search)
    print(f"\nКонтакти, які містять '{name_to_search}':")
    for contact in found_contacts:
        print(contact)

    save_data(book)
    print("\nСтан адресної книги збережено!")


if __name__ == "__main__":
    main()
