# Program 11: Log File Reader Program
from pathlib import Path

file_name = input("Enter log file path (default: sample.log): ").strip() or "sample.log"
path = Path(file_name)

if not path.exists():
    print(f"File not found: {path}")
    print("Create a text log file and run this program again.")
else:
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        print(f"\nTotal lines: {len(lines)}")
        print("\n--- Log contents ---")
        for line_number, line in enumerate(lines, start=1):
            print(f"{line_number:>4}: {line}")

        errors = [line for line in lines if "error" in line.lower()]
        warnings = [line for line in lines if "warning" in line.lower()]
        print(f"\nErrors found: {len(errors)}")
        print(f"Warnings found: {len(warnings)}")
    except OSError as error:
        print("Could not read the file:", error)
