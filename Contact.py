class Contact:

    def __init__(self, first_name, last_name, phone_number, *args, **kwargs) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.favorite_contact = False
        self.args = args
        self.email = ''
        self.telegram = ''
        self.additional_information = kwargs
        pass


    def get_name(self) -> str:
        return self.first_name

    def get_surname(self) -> str:
        return self.last_name

    def get_phone_number(self) -> str:
        return self.phone_number


    def get_favorite_contact(self) -> str:
        if self.args == ():
            self.favorite_contact = 'Нет'
        else:
            self.favorite_contact = self.args
        return self.favorite_contact

    def get_email(self) -> str:
        try:
            self.email = self.additional_information['email']
        except KeyError:
            print('Для этого контакта не указан email, исключение KeyError')
        return self.email

    def get_additional_information(self) -> str:
        try:
            self.telegram = self.additional_information['telegram']
        except KeyError:
            print('Нужен новый атрибут для этой соц.сети или указать telegram, исключение KeyError')
            return self.telegram

    def __str__(self):
        return f'Имя: {self.first_name}\n' \
               f'Фамилия: {self.last_name}\n' \
               f'Телефон: {self.phone_number}\n' \
               f'В избранных: {self.favorite_contact}\n' \
               f'Дополнительная информация:\n' \
               f'     telegram: {self.telegram}\n' \
               f'     email: {self.email}'


if __name__ == '__main__':
    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    jhon.get_favorite_contact()
    jhon.get_additional_information()
    print(jhon)
    jane = Contact('jane', 'Smith', '+71234567899', '+71234567809', facebook='@jane', email='jane@smith.com')
    jane.get_favorite_contact()
    jane.get_additional_information()
    print(jane)
