from lab4.part2.dto.course import ICourse


class ITeacher:
    """
    A class to represent an interface of the training course teacher

    Attributes
    ----------
    name : str
        name of the teacher
    courses: ICourse
        list of training courses

    """

    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

    def teach(self):
        """ Starts teaching """
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


class Teacher(ITeacher):
    """
    A class to represent a training course teacher entity

    Attributes
    ----------
    name : str
        name of the teacher
    courses: ICourse
        list of training courses

    """

    def __init__(self, name, courses=None):
        if courses is None:
            courses = list()
        super().__init__(name, courses)

    def teach(self):
        """Prints a message about teaching start"""
        print(f'{self.name} started teaching')

    def __str__(self):
        courses = ',\n\t'.join(map(lambda x: f'course_name={x.name}, course_location={x.location}', self.courses))
        return f'Teacher: name={self.name}, courses={courses}\n'
