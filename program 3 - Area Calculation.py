# Program 3: Area Calculation
import math

print("=== Area Calculator ===")
print("1. Circle\n2. Rectangle\n3. Triangle\n4. Square")
choice = input("Choose a shape (1-4): ").strip()

if choice == "1":
    radius = float(input("Enter radius: "))
    if radius < 0:
        print("Radius cannot be negative.")
    else:
        print("Area of circle:", math.pi * radius ** 2)
elif choice == "2":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    print("Area of rectangle:", length * width)
elif choice == "3":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print("Area of triangle:", 0.5 * base * height)
elif choice == "4":
    side = float(input("Enter side: "))
    print("Area of square:", side ** 2)
else:
    print("Invalid choice.")
