from lab4.part2.dto.teacher import Teacher
from lab4.part2.dto.topic import Topic
from lab4.part2.factory.course_factory import CourseFactory
from lab4.part2.repository.course_repository import CourseRepository

teacher1 = Teacher('myTeacher1')
teacher2 = Teacher('myTeacher2')

topic1 = Topic('topic1')
topic2 = Topic('topic2')

course1 = CourseFactory().create_course('course1', 'local', [teacher1, teacher2], [topic1, topic2])
course2 = CourseFactory().create_course('course2', 'offsite', [teacher1, teacher2], [topic1, topic2])

CourseRepository.insert_course(course1)
CourseRepository.insert_course(course2)

all_cources = CourseRepository.select_all_courses()
for course in all_cources:
    print(course)
print('well done')
