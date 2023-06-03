class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):
        sum_rating = 0
        len_rating = 0
        for mark in self.grades.values():
            sum_rating += sum(mark)
            len_rating += len(mark)
        res = round(sum_rating / len_rating, 2)
        return res

    def average_rating_course(self, course):
        sum_rating = 0
        len_rating = 0
        for crs in self.grades.keys():
            if crs == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        res = round(sum_rating / len_rating, 2)
        return res

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.average_rating()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Нельзя сравнивать преподавателей и студентов между собой')
            return
        return self.average_rating() < other.average_rating()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rating(self):
        sum_rating = 0
        len_rating = 0
        for mark in self.grades.values():
            sum_rating += sum(mark)
            len_rating += len(mark)
        res = round(sum_rating / len_rating, 2)
        return res

    def average_rating_course(self, course):
        sum_rating = 0
        len_rating = 0
        for crs in self.grades.keys():
            if crs == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        res = round(sum_rating / len_rating, 2)
        return res

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.average_rating()}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(
                'Нельзя сравнивать преподавателей и студентов между собой')
            return
        return self.average_rating() < other.average_rating()


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

        def __str__(self):
            res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
            return res


student1 = Student('Student', 'One', 'm')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']
student2 = Student('Student', 'Two', 'w')
student2.courses_in_progress += ['Python', 'C+']
student2.finished_courses += ['Введение в программирование']

reviewer1 = Reviewer('Reviewer', 'One')
reviewer1.courses_attached += ['Python', 'C+']
reviewer2 = Reviewer('Reviewer', 'Two')
reviewer2.courses_attached += ['Python', 'Git']

lecturer1 = Lecturer('Lecturer', 'One')
lecturer2 = Lecturer('Lecturer', 'Two')

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 6)
reviewer2.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'Python', 7)

student1.rate_lecturer(lecturer1, 'Python', 5)
student1.rate_lecturer(lecturer2, 'Python', 6)
student2.rate_lecturer(lecturer1, 'Python', 7)
student2.rate_lecturer(lecturer2, 'Python', 8)

student_list = [student1, student2]
lecturer_list = [lecturer1, lecturer2]


def average_rating_course(course, student_list):
    sum_rating = 0
    quantity_rating = 0
    for student in student_list:
        for course in student.grades:
            student_sum_rating = student.average_rating_course(course)
            sum_rating += student_sum_rating
            quantity_rating += 1
    average_rating = round(sum_rating / quantity_rating, 2)
    return average_rating


print('Средняя оценка за домашние задания по курсу "Python":')
print(average_rating_course('Python', student_list))
print('Средняя оценка за лекции по курсу "Python":')
print(average_rating_course('Python', lecturer_list))
print()

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
