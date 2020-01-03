students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student['name'].title())
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

def add_student(name, student_id: object = 322):
    student = {'name': name, 'student_id': student_id}
    students.append(student)

def save_file(student):
    try:
        f = open('students.txt', 'a')
        f.write(student + '\n')
        f.close()
    except Exception:
        print('Could not save file')

def read_file():
    try:
        f = open('Students.txt', 'r')
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print('could not read file')




def yes_or_no(question):
    while "The answer is invalid":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[:1] == 'y':
            return True
        if reply[:1] == 'n':
            return quit('If you want to continue, please chose YES')

yes_or_no('Oce li: ')

read_file()
print_students_titlecase()

student_name = input('Enter Student Name: ')
student_id = input('Enter Student ID: ')

add_student(student_name, student_id)
save_file(student_name)