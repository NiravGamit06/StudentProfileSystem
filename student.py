class Student:
    def __init__(self, name, roll_no, branch, semester):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch
        self.semester = semester

    def display_student(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Branch:", self.branch)
        print("Semester:", self.semester)


student1 = Student("Nirav Gamit", "IT001", "B.Tech IT", 5)
student2 = Student("Rahul Patel", "IT002", "B.Tech IT", 5)


student1.display_student()

print()

student2.display_student()