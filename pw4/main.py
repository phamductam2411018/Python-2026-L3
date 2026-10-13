from input import input_students, input_courses, input_marks
from output import list_courses, list_students, show_marks

students = []
courses = []

def calculate_all_gpa():
    for student in students:
        student.calculate_gpa(courses)

def sort_by_gpa():
    calculate_all_gpa()
    students.sort(key=lambda student: student.gpa, reverse=True)
    print("\nSorted students by GPA descending:")
    list_students(students)

def main():
    input_students(students)
    input_courses(courses)

    while True:
        print("\n1. List Courses")
        print("2. List Students")
        print("3. Input Marks")
        print("4. Show Marks")
        print("5. Calculate GPA and Sort Students")
        print("0. Exit")

        choice = input("Choice: ")
        if choice == '1':
            list_courses(courses)
        elif choice == '2':
            list_students(students)
        elif choice == '3':
            input_marks(students, courses, list_courses)
        elif choice == '4':
            show_marks(students)
        elif choice == '5':
            sort_by_gpa()
        elif choice == '0':
            break

if __name__ == '__main__':
    main()