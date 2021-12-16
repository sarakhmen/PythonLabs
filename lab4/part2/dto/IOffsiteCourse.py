from lab4.part2.dto.ICourse import ICourse


class IOffsiteCourse(ICourse):
    def __init__(self, name, location, teachers, topics):
        super().__init__(name, teachers, topics)
        self.location = location

    def offsite_course_feature(self):
        raise NotImplementedError

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        if not isinstance(value, str):
            raise TypeError('location must be of type str')
        self.__location = value