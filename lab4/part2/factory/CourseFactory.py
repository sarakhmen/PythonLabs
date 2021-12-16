from lab4.part2.factory.ICourseFactory import ICourseFactory
from lab4.part2.dto.impl.LocalCourse import LocalCourse
from lab4.part2.dto.impl.OffsiteCourse import OffsiteCourse


class CourseFactory(ICourseFactory):
    @staticmethod
    def create_course(name, course_type, teachers=None, topics=None):
        if course_type == 'local':
            return LocalCourse(name, teachers, topics)
        elif course_type == 'offsite':
            return OffsiteCourse(name, teachers, topics)
        else:
            raise ValueError('invalid course type')
