from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from lab4.part2.database.DBManager import DBManager
from lab4.part2.model.CourseToTeacherRelation import CourseToTeacherRelation
from lab4.part2.model.TeacherModel import TeacherModel
from lab4.part2.model.TopicModel import TopicModel


class CourseModel(DBManager.base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    location = Column(String(20))
    teachers = relationship('TeacherModel', secondary='course_to_teacher', back_populates='courses')
    topics = relationship('TopicModel', back_populates='course', cascade="all, delete, delete-orphan")
