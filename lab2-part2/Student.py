class Student:
    """
    This class represents a student entity
    """

    __record_book_id = 0

    def __init__(self, name='Unknown', surname='Unknown', grades=None):
        Student.__record_book_id += 1
        self.__id = Student.__record_book_id
        self.name = name
        self.surname = surname
        self.grades = dict(grades)

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('name must be of type str')
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError('name must be of type str')
        self.__surname = surname

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, grades):
        if not isinstance(grades, dict):
            raise TypeError('grades must be of type dict')
        if any(not isinstance(key, str) for key in grades.keys()):
            raise TypeError('grade\'s key must be of type str')
        if any(not isinstance(value, int) for value in grades.values()):
            raise TypeError('grade\'s value must be of type int')
        if any(value < 0 or value > 100 for value in grades.values()):
            raise ValueError('grade must be in range(0, 101)')
        self.__grades = grades

    def average_grade(self):
        return sum(self.__grades.values()) / len(self.__grades)

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.name == other.name \
                   and self.surname == other.surname
        return False

    def __hash__(self):
        return hash((self.name, self.surname))

    def __str__(self):
        return f'Record book number = {self.id} -> {self.__name} {self.__surname} grades: {self.__grades}'
