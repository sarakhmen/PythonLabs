from lab4.part2.dto.ICourse import ICourse


class ITeacher:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

    def teach(self):
        raise NotImplementedError

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('name must be of type str')
        self.__name = value

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, value):
        if not isinstance(value, list):
            raise TypeError('courses must be of type list')
        if not all(isinstance(course, ICourse) for course in value):
            raise TypeError('course must be of type ICourse')
        self.__courses = value
