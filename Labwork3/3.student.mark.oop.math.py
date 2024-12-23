import math
import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob
        self.__marks = {}  # Stores marks as {course_id: (mark, credits)}

    def get_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def set_mark(self, course_id, mark, credits):
        # Round down mark to 1 decimal place
        self.__marks[course_id] = (math.floor(mark * 10) / 10, credits)

    def get_marks(self):
        return self.__marks

    def calculate_gpa(self):
        total_weighted_marks = 0
        total_credits = 0
        for mark, credits in self.__marks.values():
            total_weighted_marks += mark * credits
            total_credits += credits
        return total_weighted_marks / total_credits if total_credits > 0 else 0

    def display(self):
        print(f"ID: {self.__student_id}, Name: {self.__name}, DOB: {self.__dob}")

class Course:
    def __init__(self, course_id, name, credits):
        self.__course_id = course_id
        self.__name = name
        self.__credits = credits
        self.__marks = {}

    def get_id(self):
        return self.__course_id

    def get_name(self):
        return self.__name

    def get_credits(self):
        return self.__credits

    def set_mark(self, student_id, mark):
        self.__marks[student_id] = mark

    def get_mark(self, student_id):
        return self.__marks.get(student_id, "No mark assigned")

    def display(self):
        print(f"Course ID: {self.__course_id}, Name: {self.__name}, Credits: {self.__credits}")

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
        credits = int(input("Enter course credits: "))
        self.__courses.append(Course(course_id, name, credits))

    def input_mark(self):
        course_id = input("Enter course ID: ")
        course = next((c for c in self.__courses if c.get_id() == course_id), None)

        if not course:
            print("Course not found!")
            return

        for student in self.__students:
            mark = float(input(f"Enter mark for student {student.get_name()}: "))
            student.set_mark(course_id, mark, course.get_credits())

    def calculate_average_gpa(self):
        gpas = [student.calculate_gpa() for student in self.__students]
        return np.mean(gpas) if gpas else 0

    def sort_students_by_gpa(self):
        self.__students.sort(key=lambda s: s.calculate_gpa(), reverse=True)

    def run(self):
        while True:
            print("\nStudent Mark Management System")
            print("1. Add Student")
            print("2. Add Course")
            print("3. Input Marks")
            print("4. List Students")
            print("5. List Courses")
            print("6. Calculate Average GPA")
            print("7. Sort Students by GPA")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.add_course()
            elif choice == "3":
                self.input_mark()
            elif choice == "4":
                print("Listing all students:")
                for student in self.__students:
                    student.display()
            elif choice == "5":
                print("Listing all courses:")
                for course in self.__courses:
                    course.display()
            elif choice == "6":
                avg_gpa = self.calculate_average_gpa()
                print(f"Average GPA: {avg_gpa:.2f}")
            elif choice == "7":
                self.sort_students_by_gpa()
                print("Students sorted by GPA.")
            elif choice == "8":
                print("Exiting...")
                break
            else:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    sm = StudentManagement()
    sm.run()
