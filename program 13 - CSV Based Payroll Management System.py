# Program 13: CSV-Based Payroll Management System
import csv
from pathlib import Path

CSV_FILE = Path("payroll.csv")
FIELDNAMES = ["employee_id", "name", "basic_salary", "allowance", "deduction", "net_salary"]

def load_records():
    if not CSV_FILE.exists():
        return []
    with CSV_FILE.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))

records = load_records()

while True:
    print("\n=== Payroll Management ===")
    print("1. Add employee payroll\n2. View payroll\n3. Exit")
    choice = input("Choose: ").strip()

    if choice == "1":
        employee_id = input("Employee ID: ").strip()
        if any(row["employee_id"] == employee_id for row in records):
            print("Employee ID already exists.")
            continue
        name = input("Employee name: ").strip()
        basic = float(input("Basic salary: "))
        allowance = float(input("Allowance: "))
        deduction = float(input("Deduction: "))
        net = basic + allowance - deduction
        row = {
            "employee_id": employee_id, "name": name,
            "basic_salary": f"{basic:.2f}", "allowance": f"{allowance:.2f}",
            "deduction": f"{deduction:.2f}", "net_salary": f"{net:.2f}"
        }
        records.append(row)
        with CSV_FILE.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(records)
        print(f"Payroll saved. Net salary: {net:.2f}")
    elif choice == "2":
        if not records:
            print("No payroll records.")
        for row in records:
            print(row)
    elif choice == "3":
        break
    else:
        print("Invalid choice.")
