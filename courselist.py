from course import Course

class CourseList:
    def __init__(self):
        self.courses = []   

    def add_course(self, course: Course):
        self.courses.append(course)   

    def display_all(self):
        print("\nCourses:")
        for c in self.courses:
            print(f"{c.code} - {c.title}")
