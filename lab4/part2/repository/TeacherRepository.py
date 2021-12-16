from lab4.part2.database.DBManager import DBManager
from lab4.part2.dto.ITeacher import ITeacher
from lab4.part2.factory.CourseFactory import CourseFactory
from lab4.part2.model.CourseModel import CourseModel
from lab4.part2.model.TeacherModel import TeacherModel


class TeacherRepository:
    @staticmethod
    def insert_teacher(teacher):
        if not isinstance(teacher, ITeacher):
            raise TypeError('course must be of type ITeacher')
        with DBManager().sessionmaker() as session:
            teacher_model = TeacherModel(name=teacher.name)
            session.add(teacher_model)
            session.commit()

    @staticmethod
    def select_all_courses_for_teacher_name(name):
        if not isinstance(name, str):
            raise TypeError('teacher name must be of type str')
        with DBManager().sessionmaker() as session:
            course_models = session.query(CourseModel)\
                .join(CourseModel.teachers).filter(TeacherModel.name == name).all()
            courses = list()
            for course_model in course_models:
                courses.append(CourseFactory().create_course(name=course_model.name, course_type=course_model.location))
            return courses
