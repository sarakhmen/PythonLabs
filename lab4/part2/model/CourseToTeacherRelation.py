from sqlalchemy import Column, Integer, ForeignKey

from lab4.part2.database.DBManager import DBManager


class CourseToTeacherRelation(DBManager.base):
    __tablename__ = "course_to_teacher"
    course_id = Column(Integer, ForeignKey('course.id'), primary_key=True)
    teacher_id = Column(Integer, ForeignKey('teacher.id'), primary_key=True)
