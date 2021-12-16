from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from lab4.part2.database.DBManager import DBManager
from lab4.part2.model.CourseToTeacherRelation import CourseToTeacherRelation


class TeacherModel(DBManager.base):
    __tablename__ = "teacher"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    courses = relationship('CourseModel', secondary='course_to_teacher', back_populates='teachers')
