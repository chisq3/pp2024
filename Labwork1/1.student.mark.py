
students = []
courses = []
marks = {}

def input_students():
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student Date of Birth (DD/MM/YYYY): ")
        students.append((student_id, student_name, student_dob))

def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses.append((course_id, course_name))

def input_marks():
    if not students or not courses:
        print("Please input students and courses first.")
        return

    # Select a course
    print("\nSelect a course to input marks for:")
    for idx, course in enumerate(courses, 1):
        print(f"{idx}. {course[1]}")

    course_choice = int(input("Enter course number: ")) - 1
    course_id, course_name = courses[course_choice]

    # Input marks for each student in the selected course
    print(f"\nEntering marks for course: {course_name}")
    for student in students:
        student_id, student_name, _ = student
        mark = float(input(f"Enter marks for {student_name} (ID: {student_id}): "))

        # Save marks in the dictionary
        if course_id not in marks:
            marks[course_id] = {}
        marks[course_id][student_id] = mark

def list_courses():
    if not courses:
        print("No courses available.")
        return
    print("\nList of courses:")
    for course in courses:
        print(f"Course ID: {course[0]}, Course Name: {course[1]}")

def list_students():
    if not students:
        print("No students available.")
        return
    print("\nList of students:")
    for student in students:
        student_id, student_name, student_dob = student
        print(f"ID: {student_id}, Name: {student_name}, Date of Birth: {student_dob}")

def show_student_marks():
    if not students or not courses:
        print("Please input students and courses first.")
        return

    student_id = input("Enter student ID to view marks: ")

    # Show marks for each course for the student
    print(f"\nMarks for student ID {student_id}:")
    for course in courses:
        course_id, course_name = course
        if course_id in marks and student_id in marks[course_id]:
            print(f"{course_name}: {marks[course_id][student_id]}")
        else:
            print(f"{course_name}: No marks entered")

def main():
    while True:
        print("\nStudent Mark Management System")
        print("1. Input student information")
        print("2. Input course information")
        print("3. Input marks for students")
        print("4. List courses")
        print("5. List students")
        print("6. Show student marks for a course")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            input_students()
        elif choice == '2':
            input_courses()
        elif choice == '3':
            input_marks()
        elif choice == '4':
            list_courses()
        elif choice == '5':
            list_students()
        elif choice == '6':
            show_student_marks()
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
