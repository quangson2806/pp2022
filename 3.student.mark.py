import math
from numpy import average, double,number
from unicodedata import name
from itertools import count
from audioop import reverse

class Student:
    def __init__(self,name,id,dob):
        self.name = name
        self.id = id
        self.dob = dob
        self.listCourseMark = list()
    
    def setName(self,name):
        self.name = name

    def getName(self):
         return self.name

    def setID(self):
        self.id = id

    def getID(self):
        return self.id

    def setDob(self,Dob):
        self.Dob = Dob

    def setCoursemark (self, course, mark):
        courseMark = {
            "course": course,
            "mark": mark
        }        
        self.listCoursemark.append(courseMark)
    def getaverageMark(self):
        sumMark = 0;
        for courseMark in self.listCourseMark:
            sumMark += courseMark["mark"]

        average = sumMark/len(self.listCourseMark)
        return math.floor(average*10)/10

    def display(self):
        print("Name", self.name)
        print("ID", self.id)
        print("Dob", self.dob)
        print("List of CourseMark", self.listCourseMark)
        print("Average GPA", self.getaverageMark())
        print("\n")

class Course:
    def __init__(self,id,name):
        self.id = id
        self.Name = name
    def setName(self):
        self.Name = name

    def getName(self):
        return self.Name

    def setID(self):
        self.id = id

    def getID(self):
        return self.id         

    def display(self):
        print("Name of Course", self.Name)
        print("ID of Course", self.id)  
        print("\n")

def Students(listStudents):
    TotalnumberStudent= int(input("Total number of Course:"))

    for index in range(0, TotalnumberStudent):
        id = input("Enter id of student"+str(index+1)+": ")
        name = input("Enter name of student"+str(index+1)+": ")
        Dob = input("Enter date of birth of student"+str(index+1)+": ")

        listStudents.append(Student(id, name, Dob))

def Course(ListCourse):
    TotalnumberCourse =int(input('Total number of Course: '))

    for index in range(0, TotalnumberCourse):
        id = int(input("Enter course id:"))
        name = str(input("Enter course name"))

        ListCourse.append(Course)
def Markofstudents(listStudents, listCourse):
    for course in listCourse:
        for student in listStudents:
            mark = float(input("Enter mark of student:"+ student.getName() + " for " + course.getName() + ": "))
            student.setCourseMark(course.getName(), 
            math.floor(mark*10)/10)
def Sortaveragemark(listStudents,mark):
    return listStudents.Sortaveragemark(mark)

def Sortaveragemark(listStudents):
    listStudents.sort(key = lambda student: student.getaverageMark(),reverse = False)

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





