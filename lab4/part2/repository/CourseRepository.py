from lab4.part2.database.DBManager import DBManager
from lab4.part2.dto.ILocalCourse import ILocalCourse
from lab4.part2.dto.IOffsiteCourse import IOffsiteCourse
from lab4.part2.dto.impl.Teacher import Teacher
from lab4.part2.dto.impl.Topic import Topic
from lab4.part2.factory.CourseFactory import CourseFactory
from lab4.part2.model.CourseModel import CourseModel
from lab4.part2.model.TeacherModel import TeacherModel
from lab4.part2.model.TopicModel import TopicModel


class CourseRepository:
    @staticmethod
    def select_all_courses():
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
