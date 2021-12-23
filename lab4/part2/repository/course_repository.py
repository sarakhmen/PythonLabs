from lab4.part2.database.dbmanager import DBManager
from lab4.part2.dto.course import ILocalCourse, IOffsiteCourse
from lab4.part2.dto.teacher import Teacher
from lab4.part2.dto.topic import Topic
from lab4.part2.factory.course_factory import CourseFactory
from lab4.part2.model.models import CourseModel, TeacherModel, TopicModel


class CourseRepository:
    """
    A class to represent a course repository entity

    """

    @staticmethod
    def select_all_courses():
        """Returns all courses from database"""
        courses = list()
        with DBManager().sessionmaker() as session:
            course_models = session.query(CourseModel).all()
            for course_model in course_models:
                teachers = list()
                for teacher in course_model.teachers:
                    teachers.append(Teacher(teacher.name, list()))
                topics = list()
                for topic in course_model.topics:
                    topics.append(Topic(topic.name))
                course = CourseFactory.create_course(course_model.name, course_model.location, teachers, topics)
                courses.append(course)
        return courses

    @staticmethod
    def insert_course(course):
        """Inserts a course into database"""
        if not isinstance(course, (ILocalCourse, IOffsiteCourse)):
            raise TypeError('course must be of type ILocalCourse or IOffsiteCourse')
        with DBManager().sessionmaker() as session:
            teacher_names = list(map(lambda x: x.name, course.teachers))
            teacher_models = session.query(TeacherModel).filter(TeacherModel.name.in_(teacher_names)).all()
            for teacher_model in teacher_models:
                teacher_names.remove(teacher_model.name)
            for teacher_name in teacher_names:
                teacher_models.append(TeacherModel(name=teacher_name))
            topic_models = list()
            for topic in course.topics:
                topic_models.append(TopicModel(name=topic.name))
            course_model = CourseModel(name=course.name, location=course.location, teachers=teacher_models,
                                       topics=topic_models)
            session.add(course_model)
            session.commit()
