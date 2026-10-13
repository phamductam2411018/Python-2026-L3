import math
from domains import Student, Course

def input_students(students):
    count = int(input("Enter number of students: "))
    for i in range(count):
        print(f"Student {i + 1}:")
        student_id = input("  ID: ")
        name = input("  Name: ")
        dob = input("  DoB: ")
        students.append(Student(student_id, name, dob))

def input_courses(courses):
    count = int(input("Enter number of courses: "))
    for i in range(count):
        print(f"Course {i + 1}:")
        course_id = input("  ID: ")
        name = input("  Name: ")
        credits = int(input("  Credits: "))
        courses.append(Course(course_id, name, credits))

def input_marks(students, courses, list_courses_fn):
    list_courses_fn(courses)
    selected_course_id = input("Select Course ID: ")
    
    print(f"Enter marks for course {selected_course_id}:")
    for student in students:
        score = float(input(f"  Mark for {student.name}: "))
        student.marks[selected_course_id] = math.floor(score * 10) / 10.0