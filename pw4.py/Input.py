import domains
import math
def Students(listStudents):
    TotalnumberStudent= int(input("Total number of Course:"))

    for index in range(0, TotalnumberStudent):
        id = input("Enter id of student"+str(index+1)+": ")
        name = input("Enter name of student"+str(index+1)+": ")
        Dob = input("Enter date of birth of student"+str(index+1)+": ")

def Course(ListCourse):
    TotalnumberCourse =int(input('Total number of Course: '))

    for index in range(0, TotalnumberCourse):
        id = int(input("Enter course id:"))
        name = str(input("Enter course name"))

def Markofstudents(listStudents, listCourse):
    for course in listCourse:
        for student in listStudents:
            mark = float(input("Enter mark of student:"+ student.getName() + " for " + course.getName() + ": "))
            student.setCourseMark(course.getName(), 
            math.floor(mark*10)/10)

def Sortaveragemark(listStudents):
    listStudents.sort(key = lambda student: student.getaverageMark(),reverse = False)



