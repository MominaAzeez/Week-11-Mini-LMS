from student import Student
from studentlist import StudentList
from course import Course
from courselist import CourseList


sl = StudentList(capacity=3)


s1 = Student(1, "Amara")
s2 = Student(2, "Maryam")
s3 = Student(3, "Marif")
sl.add_student(s1)
sl.add_student(s2)
sl.add_student(s3)
sl.display_all()

cl = CourseList()

c1 = Course("CS352", "Object Oriented Programming")
c2 = Course("CS356", "Linear Algebra")
cl.add_course(c1)
cl.add_course(c2)
cl.display_all()

c1.enroll(s1)
c1.enroll(s2)
c1.enroll(s3)
c1.display()
