from lab4.part2.dto.ITeacher import ITeacher


class Teacher(ITeacher):
    def __init__(self, name, courses=None):
        if courses is None:
            courses = list()
        super().__init__(name, courses)

    def teach(self):
        print(f'{self.name} started teaching')

    def __str__(self):
        courses = ',\n\t'.join(map(lambda x: f'course_name={x.name}, course_location={x.location}', self.courses))
        return f'Teacher: name={self.name}, courses={courses}\n'
