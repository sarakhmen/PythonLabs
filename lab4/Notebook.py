import re
from datetime import date
from Person import Person


class Notebook:
    def __init__(self, *args):
        self.notes = list(args)

    @property
    def notes(self):
        return self.__notes

    @notes.setter
    def notes(self, notes):
        if not isinstance(notes, list):
            raise TypeError('notes must be of type list')
        if not all(isinstance(note, Person) for note in notes):
            raise TypeError('note must be of type Person')
        self.__notes = notes

    def __iadd__(self, other):
        if not isinstance(other, Person):
            raise TypeError('other must be of type Person')
        self.notes.append(other)
        return self

    def __isub__(self, other):
        if not isinstance(other, Person):
            raise TypeError('other must be of type Person')
        self.notes.remove(other)
        return self

    def __mul__(self, field):
        result = list()
        pattern = re.compile("^\\+[0-9]{3}\\((\\d{2})\\)-\\d{3}-\\d{2}-\\d{2}")
        if pattern.match(field):
            for note in self.notes:
                if note.telephone == field:
                    result.append(note)
        elif isinstance(field, str):
            for note in self.notes:
                if note.name == field or note.surname == field or note.telephone == field:
                    result.append(note)
        elif isinstance(field, date):
            for note in self.notes:
                if note.birthday == field:
                    result.append(note)
        return result
