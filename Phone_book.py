from Contact import Contact


class PhoneBook:

    def __init__(self, name) -> None:
        self.name = name
        self.contacts = []


    def add_contact(self, contact) -> dict:
        self.contacts.append(contact)
        pass

    def get_contacts_list(self) -> str:
        for contact in self.contacts:
            contact.get_favorite_contact()
            contact.get_email()
            contact.get_additional_information()
            print(contact)
        pass

    def get_all_favorite_contacts(self) -> str:
        for contact in self.contacts:
            contact.get_favorite_contact()
            if contact.__dict__['favorite_contact'] != 'Нет':
                print(contact.__dict__['favorite_contact'])
        pass

    def get_contact_first_last_name(self, firstname, lastname) -> str:
        for contact in self.contacts:
            if firstname in contact.__dict__['first_name'] and lastname in contact.__dict__['last_name']:
                contact.get_favorite_contact()
                contact.get_email()
                contact.get_additional_information()
                print(contact)
        pass

    def delete_cotact(self, phone) -> None:
        for contact in self.contacts:
            if phone in contact.__dict__['phone_number']:
                name_del = contact.__dict__['first_name']
                lasname_del = contact.__dict__['last_name']
                print(f'Контакт {name_del} {lasname_del} удален')
                del(contact)
        pass


if __name__ == '__main__':
    phone_book = PhoneBook('Телефонная книга')
    phone_book.add_contact(Contact('Иван', 'Иванов', '+79250111111', '+71234567899', telegram='@Ivan', email='Ivan@Ivanov.com'))
    phone_book.add_contact(Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com'))
    phone_book.add_contact(Contact('Лена', 'Иванова', '+71234567899', '+79250111111'))
    #phone_book.get_contacts_list()
    #phone_book.get_all_favorite_contacts()
    #phone_book.delete_cotact('+71234567809')
    #phone_book.get_contact_first_last_name('Jhon', 'Smith')
