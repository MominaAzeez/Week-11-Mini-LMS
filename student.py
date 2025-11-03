class Student:
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name

    def __str__(self):
        return f"Student[ID={self.id}, Name={self.name}]"
