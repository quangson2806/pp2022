from Output import *
from Input import *
from domains import *

def Start_program():
    listStudents = list()
    listCourse = list()
    Students(listStudents)
    Course(listCourse)

    Markofstudents(listStudents, listCourse)

    print("before sort")
    for student in listStudents:
        student.display()

    Sortaveragemark(listStudents)

    print("after sort")
    for student in listStudents:
        student.display()

Start_program();    

