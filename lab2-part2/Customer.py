import re


class Customer:
    """
    This class represents a customer entity

    """
    def __init__(self, surname='Unknown', name='Unknown', patronymic='Unknown', mobile_phone='+380(00)-000-00-00'):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.mobile_phone = mobile_phone

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("Surname must be a string")
        self.__surname = surname

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        self.__name = name

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, patronymic):
        if not isinstance(patronymic, str):
            raise TypeError("Patronymic must be a string")
        self.__patronymic = patronymic

    @property
    def mobile_phone(self):
        return self.__mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        pattern = re.compile("^\\+[0-9]{3}\\((\\d{2})\\)-\\d{3}-\\d{2}-\\d{2}")
        if not pattern.match(mobile_phone):
            raise ValueError
        self.__mobile_phone = mobile_phone

    def __str__(self):
        return f'Customer [surname = {self.surname}, name = {self.name}, patronymic = {self.patronymic}, ' \
               f'mobile_phone = {self.mobile_phone}]'
