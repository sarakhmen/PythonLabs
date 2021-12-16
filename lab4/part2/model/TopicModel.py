from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from lab4.part2.database.DBManager import DBManager


class TopicModel(DBManager.base):
    __tablename__ = 'topic'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    course_id = Column(Integer, ForeignKey('course.id', ondelete='CASCADE'))
    course = relationship('CourseModel', back_populates='topics')
