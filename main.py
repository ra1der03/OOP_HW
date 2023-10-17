class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def av(self):
        aver=[]
        for i in self.courses_in_progress:
            aver.append(sum(self.grades[i])/len(self.grades[i]))
        return aver

    def __lt__( other, self):
        return (sum(self.av()) / len(self.av())) > (sum(other.av()) / len(other.av()))

    def __str__(self):
        return f'''\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {sum(self.av())/len(self.av())}
Курсы в процессе изучения:{self.courses_in_progress}\nЗавершенные курсы:{self.finished_courses}'''


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def av(self, courses):
        return round(sum([sum(self.grades[course])/len(self.grades[course]) for course in courses if course in self.courses_attached])/len(courses),1)


    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{self.av(self.courses_attached)}'

    def __lt__(other, self):
        return self.av(self.courses_attached)>other.av(other.courses_attached)

def avg(students:list, course):
    return sum([sum(student.grades[course])/len(student.grades[course]) for student in students if course in student.courses_in_progress])/len(students)

def average(lecturers:list, course):
    return sum([sum(lecturer.grades[course])/len(lecturer.grades[course]) for lecturer in lecturers if course in lecturer.courses_attached])/len(lecturers)

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']+['Git']+ ['OOP']
best_student.finished_courses +=['Введение в программирование']
worst_student = Student("Steve", 'Jobs', 'your_gender')
worst_student.courses_in_progress += ['Python']+ ['Git']+ ['OOP']
worst_student.finished_courses +=['Введение в программирование']

cool_mentor = Reviewer('Some', 'Buddy')
awful_mentor= Lecturer( 'Bad', 'Guy')
some_lecturer = Lecturer('Nice', "Dude")

awful_mentor.courses_attached += ['Git']+['Python']+ ['OOP']
cool_mentor.courses_attached += ['Git']+ ['Python']+ ['OOP']
some_lecturer.courses_attached += ["OOP"]+['Python']+['Git']

cool_mentor.rate_hw(worst_student, 'OOP', 1)
cool_mentor.rate_hw(worst_student, 'OOP', 1)
cool_mentor.rate_hw(best_student, 'OOP', 10)
cool_mentor.rate_hw(best_student, 'OOP', 10)
cool_mentor.rate_hw(worst_student, 'Python', 1)
cool_mentor.rate_hw(best_student, 'Git', 10)
cool_mentor.rate_hw(worst_student, 'Python', 1)
cool_mentor.rate_hw(best_student, 'Git', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(worst_student, 'Git', 1)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(worst_student, 'Git', 1)
worst_student.rate_lecture(some_lecturer, 'OOP', 8)
best_student.rate_lecture(some_lecturer, 'OOP', 9)
worst_student.rate_lecture(awful_mentor, 'Git', 1)
best_student.rate_lecture(awful_mentor, 'Git', 2)

worst_student.rate_lecture(some_lecturer, 'Git', 7)
best_student.rate_lecture(some_lecturer, 'Git', 9)
worst_student.rate_lecture(awful_mentor, 'OOP', 0)
best_student.rate_lecture(awful_mentor, 'OOP', 1)

worst_student.rate_lecture(some_lecturer, 'Python', 8)
best_student.rate_lecture(some_lecturer, 'Python', 10)
worst_student.rate_lecture(awful_mentor, 'Python', 1)
best_student.rate_lecture(awful_mentor, 'Python', 3)

print('REVIEWER:', cool_mentor, sep='\n', end='\n')
print('LECTURER:',awful_mentor, end='\n')
print('LECTURER:', some_lecturer, end='\n')
print("STUDENTs:",best_student, worst_student, end='\n')

print(best_student>worst_student)
print(some_lecturer>awful_mentor)

print(avg([best_student, worst_student], 'Python'))
print(average([some_lecturer, awful_mentor], 'Git'))
