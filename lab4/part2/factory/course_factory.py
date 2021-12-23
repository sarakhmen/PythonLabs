from lab4.part2.dto.course import LocalCourse, OffsiteCourse


class ICourseFactory:
    """
    A class to represent an interface of the training courses factory

    """

    @staticmethod
    def create_course(name, location, teachers, topics):
        """ Creates a course according to the location """
        raise NotImplementedError


class CourseFactory(ICourseFactory):
    """
    A class to represent a training courses factory entity

    """

    @staticmethod
    def create_course(name, course_type, teachers=None, topics=None):
        """Creates a course according to the location"""
        if course_type == 'local':
            return LocalCourse(name, teachers, topics)
        elif course_type == 'offsite':
            return OffsiteCourse(name, teachers, topics)
        else:
            raise ValueError('invalid course type')
