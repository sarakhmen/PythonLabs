from Student import Student
from Group import Group


def main():
    try:
        student1 = Student('Артур', 'Сарахман', {'мат': 90, 'англ': 95, 'фп': 100})
        student2 = Student('Богдан', 'Чуй', {'мат': 95, 'англ': 95, 'фп': 100})
        student3 = Student('Іван', 'Власюк', {'мат': 100, 'англ': 85, 'фп': 90})
        student4 = Student('Ліза', 'Гончарова', {'мат': 99, 'англ': 99, 'фп': 99})
        student5 = Student('Євгеній', 'Захарчук', {'мат': 100, 'англ': 100, 'фп': 100})
        student6 = Student('Тетяна', 'Кушнірук', {'мат': 100, 'англ': 100, 'фп': 99})
        student7 = Student('Анна', 'Котова', {'мат': 95, 'англ': 95, 'фп': 95})
        student8 = Student('Олег', 'Моругий', {'мат': 100, 'англ': 90, 'фп': 70})
        student9 = Student('Сокирка', 'Кирило', {'мат': 100, 'англ': 100, 'фп': 100})
        ti_02 = Group(student1, student2, student3, student4, student5, student6, student7)
        print('Group after creating', ti_02, sep='\n')
        ti_02.add_student(student8)
        ti_02.add_student(student9)
        print('Group after addition new two students', ti_02, sep='\n')
        print('Highest average score for 5 students', ti_02.highest_average_score(5), sep='\n')
        ti_02.del_student(student8)
        print('Group after removal of the Oleg', ti_02, sep='\n')
        ti_02.add_student(student1)
    except Exception as e:
        print(e)


main()
