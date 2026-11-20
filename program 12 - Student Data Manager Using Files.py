# Program 12: Student Data Manager Using Files
import json
from pathlib import Path

DATA_FILE = Path("students.json")

def load_students():
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            print("Could not read saved data. Starting with an empty list.")
    return []

def save_students(students):
    DATA_FILE.write_text(json.dumps(students, indent=4), encoding="utf-8")

students = load_students()

while True:
    print("\n=== Student Data Manager ===")
    print("1. Add student\n2. View students\n3. Search by roll number\n4. Exit")
    choice = input("Choose: ").strip()

    if choice == "1":
        roll = input("Roll number: ").strip()
        if any(s["roll"] == roll for s in students):
            print("That roll number already exists.")
            continue
        name = input("Student name: ").strip()
        course = input("Course: ").strip()
        students.append({"roll": roll, "name": name, "course": course})
        save_students(students)
        print("Student saved to", DATA_FILE)
    elif choice == "2":
        if not students:
            print("No student records.")
        for student in students:
            print(student)
    elif choice == "3":
        roll = input("Enter roll number: ").strip()
        result = next((s for s in students if s["roll"] == roll), None)
        print(result if result else "Student not found.")
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
