# Function
# Input functions:
def Studentscount():
	s = int(input("The total number of students is: "))
	return s

# Input total courses information
def Coursescount():
	c = int(input("The total number of courses is: "))
	return c

# Input student information
def Studentinfo():
	id = input("\tStudent's ID is: ")
	name = input("\tYour name: ")
	DoB = input("\tDate of birth: ")
	s = {"ID": id, "Name": name, "DoB": DoB}
	return s

# Input Courses Infomation
def Coursesinfo():
	id = input("\tCourse ID: ")
	name = input("\tCourse name: ")
	c = {"ID": id, "name": name}
	return c

# Input Mark for students in this course
def studentMarks():
	sel_course_id = input("Select a course ID: ")
	for i in range(len(course)):
		if course[i].get("ID") == sel_course_id:
			cid = course[i].get("name")
			m = {"Course": cid, "Students and marks": []}
			print("Course name: " + course[i].get("name") + "\n")
			for j in range(len(students)):
				mark = float(input("\tEnter " + students[j].get("Name") + "'s mark "))
				sid = students[j].get("Name")
				m["Students and marks"].append((sid, mark))
			return m

# Display functions
# Input List students
def Studentsprint():
	print("\nThe list of all student is: ")
	print('\n'.join(map(str, students)))

# Input List courses
def Coursesprint():
	print("\nThe list of all courses is: ")
	print('\n'.join(map(str, course)))

# Display marks
def displayMarks():
	choose = input("\n---------------------------------\nPlease choose the course that you want to see marks (course name only): ")
	for i in range(len(marks)):
		if marks[i].get("Course") == choose:
			print(marks[i])

# Main
# Students and Courses
# Input
students = []
scount = Studentscount()
print("Please enter the information of the student: ")
for i in range(0, scount):
	s = Studentinfo()
	students += [s]
	print("\n---------------------------------")

course = []
ccount = Coursescount()
print("\nPlease enter the information of the course: ")
for i in range(0, ccount):
	c = Coursesinfo()
	course += [c]
	print("\n---------------------------------")

# Display
Studentsprint()
Coursesprint()

# Marks
# Input
rawmarks = []
marks = []
print("\n---------------------------------\nPlease enter the marks of the course: ")
x = 'yes'
while x == 'yes':
	ma = studentMarks()
	rawmarks += [ma]
	x = input("\n*** Do you want to select another course? (yes or no) *** ")
	if (x != "yes") and (x != "no"):
		print("Invalid choice! Please choose again.")
		x = "yes"
marks = list(filter(None, rawmarks))

# Display
y = 'yes'
while y == 'yes':
	displayMarks()
	y = input("\n*** Do you want to select another course? (yes or no) *** ")
	if (y != "yes") and (y != "no"):
		print("Invalid choice! Please choose again.")
		y = "yes"
