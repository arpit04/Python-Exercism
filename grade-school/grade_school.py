import itertools

class School(object):

    
    def __init__(self):
        self.students_by_grade = {'a':'arnold','s':'sam','h':'herry','k':'kevin'}
        print(self.students_by_grade)
    
    def add_student(self, name, grade):
        students = self.students_by_grade.get('a')
        print("in add_student")
        print(students)
        if not name in students:
            students = list(students.split())
            students.append(name)
            print(students)
            students.sort()
            self.students_by_grade[grade] = students

    def roster(self):
        grades = sorted(self.students_by_grade.keys())
        print("in roster")
        print(grades)
        result =  list(itertools.chain(*[self.students_by_grade[g] for g in grades]))
        return result

    def grade(self, grade_number):
        result = self.students_by_grade.get(grade_number)
        print("in grade")
        print(result)
        return result
s = School()
s.add_student('a','arnold')
s.roster()
s.grade('s')


