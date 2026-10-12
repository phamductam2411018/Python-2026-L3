import math
import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = 0.0

    def calculate_gpa(self, course_list):
        if not self.marks:
            self.gpa = 0.0
            return 0.0
            
        mark_values = []
        credit_values = []
        
        for course in course_list:
            if course.id in self.marks:
                mark_values.append(self.marks[course.id])
                credit_values.append(course.credits)
                
        if len(credit_values) == 0:
            self.gpa = 0.0
            return 0.0
            
        marks_array = np.array(mark_values)
        credits_array = np.array(credit_values)
        
        weighted_sum = np.sum(marks_array * credits_array)
        total_credits = np.sum(credits_array)
        
        self.gpa = weighted_sum / total_credits
        return self.gpa

class Course:
    def __init__(self, course_id, name, credits):
        self.id = course_id
        self.name = name
        self.credits = credits

students = []
courses = []

def input_students():
    count = int(input("Enter number of students: "))
    for i in range(count):
        print(f"Student {i + 1}:")
        student_id = input("  ID: ")
        name = input("  Name: ")
        dob = input("  DoB: ")
        students.append(Student(student_id, name, dob))

def input_courses():
    count = int(input("Enter number of courses: "))
    for i in range(count):
        print(f"Course {i + 1}:")
        course_id = input("  ID: ")
        name = input("  Name: ")
        credits = int(input("  Credits: "))
        courses.append(Course(course_id, name, credits))

def list_courses():
    print("\n--- Course List ---")
    for course in courses:
        print(f"ID: {course.id} | Name: {course.name} | Credits: {course.credits}")

def list_students():
    print("\n--- Student List ---")
    for student in students:
        print(f"ID: {student.id} | Name: {student.name} | DoB: {student.dob} | GPA: {student.gpa:.2f}")

def input_marks():
    list_courses()
    selected_course_id = input("Select Course ID: ")
    
    print(f"Enter marks for course {selected_course_id}:")
    for student in students:
        score = float(input(f"  Mark for {student.name}: "))
        student.marks[selected_course_id] = math.floor(score * 10) / 10.0

def show_marks():
    selected_course_id = input("Enter Course ID: ")
    print(f"\n--- Marks for Course {selected_course_id} ---")
    for student in students:
        mark = student.marks.get(selected_course_id, "N/A")
        print(f"{student.name}: {mark}")

def calculate_all_gpa():
    for student in students:
        student.calculate_gpa(courses)

def sort_by_gpa():
    calculate_all_gpa()
    students.sort(key=lambda student: student.gpa, reverse=True)
    print("\nSorted students by GPA descending:")
    list_students()

def main():
    input_students()
    input_courses()

    while True:
        print("\n1. List Courses")
        print("2. List Students")
        print("3. Input Marks")
        print("4. Show Marks")
        print("5. Calculate GPA and Sort Students")
        print("0. Exit")

        choice = input("Choice: ")
        if choice == '1':
            list_courses()
        elif choice == '2':
            list_students()
        elif choice == '3':
            input_marks()
        elif choice == '4':
            show_marks()
        elif choice == '5':
            sort_by_gpa()
        elif choice == '0':
            break

if __name__ == '__main__':
    main()