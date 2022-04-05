from unicodedata import name
import Input
import Output
import math
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