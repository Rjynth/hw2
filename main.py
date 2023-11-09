class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades_student = {}

    def rate_hw_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade]
            else:
                lecturer.grades_lecturer[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades_lecturer = {}


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades_student:
                student.grades_student[course] += [grade]
            else:
                student.grades_student[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

awesome_lecturer = Lecturer('Another', 'Lecturer')
awesome_lecturer.courses_attached += ['Python']

cool_mentor.rate_hw_student(best_student, 'Python', 10)
cool_mentor.rate_hw_student(best_student, 'Python', 10)
cool_mentor.rate_hw_student(best_student, 'Python', 10)

print(best_student.grades_student)

best_student.rate_hw_lecturer(awesome_lecturer, 'Python', 10)
best_student.rate_hw_lecturer(awesome_lecturer, 'Python', 10)
best_student.rate_hw_lecturer(awesome_lecturer, 'Python', 10)

print(awesome_lecturer.grades_lecturer)
