class ICourse:
    """
    A class to represent an interface of the training course

    Attributes
    ----------
    name : str
        name of the course
    teachers: ITeacher
        list of course teachers
    topics: ITopic
        list of topics being studied on the course

    """

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
        from lab4.part2.dto.teacher import ITeacher
        if not isinstance(value, list):
            raise TypeError('teachers must be of type list')
        if not all(isinstance(teacher, ITeacher) for teacher in value):
            raise TypeError('teacher must be of type ITeacher')
        self.__teachers = value


class ILocalCourse(ICourse):
    """
    A class to represent an interface of the local training course

    Attributes
    ----------
    name : str
        name of the course
    location: str
        course location
    teachers: ITeacher
        list of course teachers
    topics: ITopic
        list of topics being studied on the course

    """

    def __init__(self, name, location, teachers, topics):
        super().__init__(name, teachers, topics)
        self.location = location

    def local_course_feature(self):
        """Represents a local course feature functionality"""
        raise NotImplementedError

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        if not isinstance(value, str):
            raise TypeError('location must be of type str')
        self.__location = value


class IOffsiteCourse(ICourse):
    """
    A class to represent an interface of the offsite training course

    Attributes
    ----------
    name : str
        name of the course
    location: str
        course location
    teachers: ITeacher
        list of course teachers
    topics: ITopic
        list of topics being studied on the course

    """

    def __init__(self, name, location, teachers, topics):
        super().__init__(name, teachers, topics)
        self.location = location

    def offsite_course_feature(self):
        """Represents a local course feature functionality"""
        raise NotImplementedError

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        if not isinstance(value, str):
            raise TypeError('location must be of type str')
        self.__location


class LocalCourse(ILocalCourse):
    """
    A class to represent a local training course entity

    Attributes
    ----------
    name : str
        name of the course
    teachers: ITeacher
        list of course teachers
    topics: ITopic
        list of topics being studied on the course

    """

    def __init__(self, name, teachers, topics):
        if teachers is None:
            teachers = list()
        if topics is None:
            topics = list()
        super().__init__(name, 'local', teachers, topics)

    def start(self):
        """Prints string that notifies about course start"""
        print(f'start {self.name} local course')

    def end(self):
        """Prints string that notifies about course end"""
        print(f'end {self.name} local course')

    def local_course_feature(self):
        """Represents a local course feature stub"""
        print('stub')

    def __str__(self):
        teachers = ',\n\t'.join(map(lambda x: x.name, self.teachers))
        topics = ',\n\t'.join(map(lambda x: x.name, self.topics))
        return f'Local course: name={self.name}, \n\tteachers={teachers},\n\ttopics={topics}\n'


class OffsiteCourse(IOffsiteCourse):
    """
    A class to represent an offsite training course entity

    Attributes
    ----------
    name : str
        name of the course
    teachers: ITeacher
        list of course teachers
    topics: ITopic
        list of topics being studied on the course

    """

    def __init__(self, name, teachers, topics):
        if teachers is None:
            teachers = list()
        if topics is None:
            topics = list()
        super().__init__(name, 'offsite', teachers, topics)

    def start(self):
        """Prints string that notifies about course start"""
        print(f'start {self.name} offsite course')

    def end(self):
        """Prints string that notifies about course end"""
        print(f'end {self.name} offsite course')

    def offsite_course_feature(self):
        """Represents an offsite course feature stub"""
        print('stub')

    def __str__(self):
        teachers = ',\n\t'.join(map(lambda x: x.name, self.teachers))
        topics = ',\n\t'.join(map(lambda x: x.name, self.topics))
        return f'Offsite course: name={self.name}, \n\tteachers={teachers},\n\ttopics={topics}\n'
