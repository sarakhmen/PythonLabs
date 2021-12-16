from lab4.part2.dto.ILocalCourse import ILocalCourse


class LocalCourse(ILocalCourse):
    def __init__(self, name, teachers, topics):
        if teachers is None:
            teachers = list()
        if topics is None:
            topics = list()
        super().__init__(name, 'local', teachers, topics)

    def start(self):
        print(f'start {self.name} local course')

    def end(self):
        print(f'end {self.name} local course')

    def local_course_feature(self):
        print('stub')

    def __str__(self):
        teachers = ',\n\t'.join(map(lambda x: x.name, self.teachers))
        topics = ',\n\t'.join(map(lambda x: x.name, self.topics))
        return f'Local course: name={self.name}, \n\tteachers={teachers},\n\ttopics={topics}\n'
