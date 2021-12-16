from lab4.part2.dto.IOffsiteCourse import IOffsiteCourse


class OffsiteCourse(IOffsiteCourse):
    def __init__(self, name, teachers, topics):
        if teachers is None:
            teachers = list()
        if topics is None:
            topics = list()
        super().__init__(name, 'offsite', teachers, topics)

    def start(self):
        print(f'start {self.name} offsite course')

    def end(self):
        print(f'end {self.name} offsite course')

    def offsite_course_feature(self):
        print('stub')

    def __str__(self):
        teachers = ',\n\t'.join(map(lambda x: x.name, self.teachers))
        topics = ',\n\t'.join(map(lambda x: x.name, self.topics))
        return f'Offsite course: name={self.name}, \n\tteachers={teachers},\n\ttopics={topics}\n'
