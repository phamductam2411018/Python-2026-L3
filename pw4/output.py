def list_courses(courses):
    print("\n--- Course List ---")
    for course in courses:
        print(f"ID: {course.id} | Name: {course.name} | Credits: {course.credits}")

def list_students(students):
    print("\n--- Student List ---")
    for student in students:
        print(f"ID: {student.id} | Name: {student.name} | DoB: {student.dob} | GPA: {student.gpa:.2f}")

def show_marks(students):
    selected_course_id = input("Enter Course ID: ")
    print(f"\n--- Marks for Course {selected_course_id} ---")
    for student in students:
        mark = student.marks.get(selected_course_id, "N/A")
        print(f"{student.name}: {mark}")