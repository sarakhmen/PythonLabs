from lab4.part2.dto.ICourse import ICourse


class ILocalCourse(ICourse):
    def __init__(self, name, location, teachers, topics):
        super().__init__(name, teachers, topics)
        self.location = location

    def local_course_feature(self):
        raise NotImplementedError

    # def start(self):
    #     print(f'start {self.name} course')
    #
    # def end(self):
    #     print(f'end {self.name} course')

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        if not isinstance(value, str):
            raise TypeError('location must be of type str')
        self.__location = value