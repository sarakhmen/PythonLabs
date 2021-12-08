from datetime import date
import re


class Person:
    def __init__(self, name='Unknown', surname='Unknown', telephone='+380(00)-000-00-00', birthday=date.today()):
        self.name = name
        self.surname = surname
        self.telephone = telephone
        self.birthday = birthday

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
    def telephone(self):
        return self.__telephone

    @telephone.setter
    def telephone(self, telephone):
        pattern = re.compile("^\\+[0-9]{3}\\((\\d{2})\\)-\\d{3}-\\d{2}-\\d{2}")
        if not pattern.match(telephone):
            raise ValueError('telephone template: +380(00)-000-00-00')
        self.__telephone = telephone

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday):
        if not isinstance(birthday, date):
            raise TypeError('birthday must be of type date')
        self.__birthday = birthday

    def __eq__(self, other):
        if not isinstance(other, Person):
            raise TypeError('other must be of type Person')
        return (self.name, self.surname, self.telephone, self.birthday) ==\
               (other.name, other.surname, other.telephone, other.birthday)

    def __str__(self):
        return f'User [name = {self.name}, surname = {self.surname}, telephone = {self.telephone}, ' \
               f'birthday = {self.birthday}]'
