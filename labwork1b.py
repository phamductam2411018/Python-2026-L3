students = []
courses = []
marks = {}

def input_students():
    n = int(input("Enter number of students: "))
    for i in range(n):
        print(f"Student {i + 1}:")
        s_id = input("  ID: ")
        s_name = input("  Name: ")
        dob = input("  DoB: ")
        students.append({"id": s_id, "name": s_name, "dob": dob})

def input_courses():
    n = int(input("Enter number of courses: "))
    for i in range(n):
        print(f"Course {i + 1}:")
        c_id = input("  ID: ")
        c_name = input("  Name: ")
        courses.append({"id": c_id, "name": c_name})

def list_courses():
    print("\n--- Courses ---")
    for c in courses:
        print(f"ID: {c['id']} | Name: {c['name']}")

def list_students():
    print("\n--- Students ---")
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | DoB: {s['dob']}")

def input_marks():
    list_courses()
    c_id = input("Select Course ID: ")
    marks[c_id] = {}
    print(f"Enter marks for course {c_id}:")
    for s in students:
        m = float(input(f"  Mark for {s['name']}: "))
        marks[c_id][s['id']] = m

def show_marks():
    c_id = input("Enter Course ID: ")
    if c_id in marks:
        print(f"\n--- Marks for {c_id} ---")
        for s in students:
            m = marks[c_id].get(s['id'], "N/A")
            print(f"{s['name']}: {m}")
    else:
        print("No marks found.")

def main():
    input_students()
    input_courses()
    
    while True:
        print("\n1. List Courses")
        print("2. List Students")
        print("3. Input Marks")
        print("4. Show Marks")
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
        elif choice == '0':
            break

if __name__ == '__main__':
    main()