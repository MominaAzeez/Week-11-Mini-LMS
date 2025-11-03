from student import Student

class Course:
    def __init__(self, code, title):
        self.code = code
        self.title = title
        self.students = []   

    def enroll(self, student: Student):
        self.students.append(student)

    def display(self):
        print(f"\nCourse {self.code} - {self.title}")
        if not self.students:
            print("  No students enrolled yet.")
        for s in self.students:
            print(f" - {s}")
