from student import Student

class StudentList:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.students = [None] * capacity   
        self.size = 0

    def add_student(self, student: Student):
        if self.size < self.capacity:
            self.students[self.size] = student
            self.size += 1
        else:
            print("Student list is full!")

    def display_all(self):
        print("\nStudents:")
        for i in range(self.size):
            print(self.students[i])
