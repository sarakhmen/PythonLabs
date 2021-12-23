from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from lab4.part2.database.dbmanager import DBManager


class CourseModel(DBManager.base):
    """
    A class to represent a database course model entity

    """

    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    location = Column(String(20))
    teachers = relationship('TeacherModel', secondary='course_to_teacher', back_populates='courses')
    topics = relationship('TopicModel', back_populates='course', cascade="all, delete, delete-orphan")


class CourseToTeacherRelation(DBManager.base):
    """
    A class to represent a database course to teacher relation

    """

    __tablename__ = "course_to_teacher"
    course_id = Column(Integer, ForeignKey('course.id'), primary_key=True)
    teacher_id = Column(Integer, ForeignKey('teacher.id'), primary_key=True)


class TeacherModel(DBManager.base):
    """
    A class to represent a database teacher model entity

    """

    __tablename__ = "teacher"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    courses = relationship('CourseModel', secondary='course_to_teacher', back_populates='teachers')


class TopicModel(DBManager.base):
    """
    A class to represent a database topic model entity

    """

    __tablename__ = 'topic'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    course_id = Column(Integer, ForeignKey('course.id', ondelete='CASCADE'))
    course = relationship('CourseModel', back_populates='topics')
