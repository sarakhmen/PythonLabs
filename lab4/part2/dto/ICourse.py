class ICourse:
    def __init__(self, name, teachers, topics):
        self.name = name
        self.teachers = teachers
        self.topics = topics

    def start(self):
        raise NotImplementedError

    def end(self):
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
    def teachers(self):
        return self.__teachers

    @teachers.setter
    def teachers(self, value):
        from lab4.part2.dto.ITeacher import ITeacher
        if not isinstance(value, list):
            raise TypeError('teachers must be of type list')
        if not all(isinstance(teacher, ITeacher) for teacher in value):
            raise TypeError('teacher must be of type ITeacher')
        self.__teachers = value

