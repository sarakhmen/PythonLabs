from Student import Student


class Group:
    """
    This class represents a students' group entity
    """

    __group_id = 0

    def __init__(self, *args):
        Group.__group_id += 1
        self.__id = Group.__group_id
        self.max_size = 20
        self.students = list(args)
        print('')

    @property
    def students(self):
        return self.__students

    @students.setter
    def students(self, students):
        if not isinstance(students, list):
            raise TypeError('students must be of type list')
        if not all(isinstance(student, Student) for student in students):
            raise TypeError('student must be of type Student')
        if 0 > len(students) > self.__max_size:
            raise ValueError(f'group with id {self.__group_id} must contain not more than {self.__max_size} students')
        if len(students) != len(set(students)):
            raise ValueError(f'group must not contain duplicate students')
        self.__students = students

    @property
    def id(self):
        return self.__id

    @property
    def max_size(self):
        return self.__max_size

    @max_size.setter
    def max_size(self, value):
        if not isinstance(value, int):
            raise TypeError('max_size must be of type int')
        if value < 0:
            raise ValueError('max_size should not be less than 0')
        self.__max_size = value

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError('student must be of type Student')
        if len(self.__students) == self.__max_size:
            raise ValueError(f'group with id {self.__group_id} must contain not more than {self.__max_size} students')
        if student in self.__students:
            raise ValueError(f'group must not contain duplicate students')
        self.__students.append(student)

    def del_student(self, student):
        if not isinstance(student, Student):
            raise TypeError('student must be of type Student')
        self.__students.remove(student)

    def highest_average_score(self, number_of_students):
        self.__students.sort(reverse=True, key=lambda x: x.average_grade())
        return '\t' + '\n\t'.join(map(lambda x: str(x) + '\n\t\twith average score = ' + str(x.average_grade()),
                                      self.__students[:number_of_students]))

    def __str__(self):
        students = '\n\t'.join(map(str, self.__students))
        return f'Group {self.id} consists of {len(self.__students)}:\n\t{students}'
