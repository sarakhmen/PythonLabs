from lab4.part2.database.dbmanager import DBManager
from lab4.part2.dto.teacher import ITeacher
from lab4.part2.factory.course_factory import CourseFactory
from lab4.part2.model.models import TeacherModel, CourseModel


class TeacherRepository:
    """
    A class to represent a teacher repository entity

    """

    @staticmethod
    def insert_teacher(teacher):
        """Inserts a teacher into database"""
        if not isinstance(teacher, ITeacher):
            raise TypeError('course must be of type ITeacher')
        with DBManager().sessionmaker() as session:
            teacher_model = TeacherModel(name=teacher.name)
            session.add(teacher_model)
            session.commit()

    @staticmethod
    def select_all_courses_for_teacher_name(name):
        """Returns all courses for the given teacher name"""
        if not isinstance(name, str):
            raise TypeError('teacher name must be of type str')
        with DBManager().sessionmaker() as session:
            course_models = session.query(CourseModel)\
                .join(CourseModel.teachers).filter(TeacherModel.name == name).all()
            courses = list()
            for course_model in course_models:
                courses.append(CourseFactory().create_course(name=course_model.name, course_type=course_model.location))
            return courses
