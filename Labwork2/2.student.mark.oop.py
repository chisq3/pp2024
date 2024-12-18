class Student:
    def __init__(self, student_id, name, dob):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob

    def get_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def display(self):
        print(f"ID: {self.__student_id}, Name: {self.__name}, DOB: {self.__dob}")

class Course:
    def __init__(self, course_id, name):
        self.__course_id = course_id
        self.__name = name
        self.__marks = {}

    def get_id(self):
        return self.__course_id

    def get_name(self):
        return self.__name

    def set_mark(self, student_id, mark):
        self.__marks[student_id] = mark

    def get_mark(self, student_id):
        return self.__marks.get(student_id, "No mark assigned")

    def display(self):
        print(f"Course ID: {self.__course_id}, Name: {self.__name}")

    def display_marks(self, students):
        print(f"Marks for course {self.__name}:")
        for student_id, mark in self.__marks.items():
            student_name = next((s.get_name() for s in students if s.get_id() == student_id), "Unknown Student")
            print(f"Student: {student_name} - Mark: {mark}")

class StudentManagement:
    def __init__(self):
        self.__students = []
        self.__courses = []

    def add_student(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        self.__students.append(Student(student_id, name, dob))

    def add_course(self):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        self.__courses.append(Course(course_id, name))

    def input_mark(self):
        course_id = input("Enter course ID: ")
        course = next((c for c in self.__courses if c.get_id() == course_id), None)

        if not course:
            print("Course not found!")
            return

        for student in self.__students:
            mark = float(input(f"Enter mark for student {student.get_name()}: "))
            course.set_mark(student.get_id(), mark)

    def list_students(self):
        print("Listing all students:")
        for student in self.__students:
            student.display()

    def list_courses(self):
        print("Listing all courses:")
        for course in self.__courses:
            course.display()

    def show_marks(self):
        course_id = input("Enter course ID: ")
        course = next((c for c in self.__courses if c.get_id() == course_id), None)

        if not course:
            print("Course not found!")
            return

        course.display_marks(self.__students)


if __name__ == "__main__":
    sm = StudentManagement()
    while True:
        print("\nStudent Mark Management System")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Input Marks")
        print("4. List Students")
        print("5. List Courses")
        print("6. Show Marks")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            sm.add_student()
        elif choice == 2:
            sm.add_course()
        elif choice == 3:
            sm.input_mark()
        elif choice == 4:
            sm.list_students()
        elif choice == 5:
            sm.list_courses()
        elif choice == 6:
            sm.show_marks()
        elif choice == 7:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")
