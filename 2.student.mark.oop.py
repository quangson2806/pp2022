#Function
Listcourse = []
Liststudent = []
class Student_infomation:
    def _init_ (self,name,id,Dob):
        self.name = name
        self.id = id
        self.Dob = Dob
        
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
    
    def setID(self):
        self.id = id

    def getID(self):
        return self.id
    
    def setDob(self, Dob):
        self.Dob = Dob

    def getDOB(self):
        return self.Dob

    def setcourse(self, course):
        self.course = course
    
    def setmark(self, mark):
        self.mark = mark
        
    def display(self):
        print("name",self.name)
        print("id", self.id)
        print("Dob", self.Dob)
        print("course", self.course)
        print("mark", self.mark)
        
class Course:
    def _init_ (self,id,name):
        self.name = name
        self.id = id

    def getName(self):
      return  self.name   
    
    def display(self):
        print("Namecourse", self.name)
        print("Idcourse", self.id)

def Student(Liststudent):
    TotalnumberStudents = int(input('Total number of Students: '))
    
    for index in range(0, TotalnumberStudents):
        id = input("Enter id of student "+str(index+1)+": ")
        name = input("Enter name of student"+str(index+1)+": ")
        Dob = input("Enter date of birth of student "+str(index+1)+': ')
        
        Liststudent.append(Student)

def Course(ListCourse):
  TotalnumberCourse = int(input('Total number of Course: '))

  for index in range(0, TotalnumberCourse):
    id = int(input("Enter couse id: "))
    name = str(input("Enter course name: "))

    ListCourse.append(Course)

def Markofstudents(listStudents, listCourse):
  NameCourse = str(input("Enter name of course to mark: "))
  s = True

  while s :
    for course in Listcourse:
      if (NameCourse == course.getName()):
        s = False

  for students in listStudents:
    mark = float(input("Mark of students "+ students.getName()))
    students.setcourse(NameCourse)
    students.setmark(mark)

def Main():
  ListStudent = list()
  ListCourse = list ()
  Student(ListStudent)
  Course(ListCourse)

  Markofstudents(ListStudent, ListCourse)

  for student in ListStudent:
    student.display()
Main();
