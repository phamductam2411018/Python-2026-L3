# 1. Input Students
students = []
n_students = int(input("Number of students: "))
for i in range(n_students):
    s_id = input("  Student ID: ")
    s_name = input("  Student Name: ")
    s_dob = input("  Date of Birth: ")
    students.append((s_id, s_name, s_dob))

# 2. Input Courses
courses = []
n_courses = int(input("\nNumber of courses: "))
for i in range(n_courses):
    c_id = input("  Course ID: ")
    c_name = input("  Course Name: ")
    courses.append((c_id, c_name))

# 3. List Courses and Students
print("\n--- COURSE LIST ---")
for c in courses:
    print(c[0], "-", c[1])

print("\n--- STUDENT LIST ---")
for s in students:
    print(s[0], "-", s[1], "-", s[2])

# 4. Input Marks for a Selected Course
marks = {}
select_course = input("\nEnter Course ID to input marks: ")
marks[select_course] = {}

for s in students:
    score = float(input(f"Enter mark for {s[1]}: "))
    marks[select_course][s[0]] = score

# 5. Show Marks for the Selected Course
print(f"\n--- MARKS FOR COURSE {select_course} ---")
for s in students:
    print(f"Student: {s[1]} | Mark: {marks[select_course][s[0]]}")