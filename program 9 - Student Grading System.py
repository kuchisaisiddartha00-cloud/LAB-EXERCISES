# Program 9: Student Grading System

students = []
count = int(input("How many students? "))

for _ in range(count):
    name = input("\nStudent name: ").strip()
    marks = []
    for subject in ("Subject 1", "Subject 2", "Subject 3"):
        mark = float(input(f"{subject} marks (0-100): "))
        if not 0 <= mark <= 100:
            print("Marks must be between 0 and 100. Please re-enter.")
            mark = float(input(f"{subject} marks (0-100): "))
        marks.append(mark)

    average = sum(marks) / len(marks)
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    elif average >= 40:
        grade = "E"
    else:
        grade = "F"

    students.append({"name": name, "marks": marks, "average": average, "grade": grade})

print("\n=== Student Results ===")
for student in students:
    print(f"{student['name']}: marks={student['marks']}, average={student['average']:.2f}, grade={student['grade']}")
