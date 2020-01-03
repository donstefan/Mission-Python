students = []

class Student:
    school_name = 'Springfield Elementary'

    def __init__(self, name, student_id=322):
        self.name = name
        self.student_id = student_id
        # student = {'name': name, 'student_id': student_id}
        students.append(self)

    def __str__(self):
        return "Student  " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name