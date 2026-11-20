# Program 1: Basic Python Programs
# Demonstrates variables, operators, input, and output.

print("=== Basic Python Demonstration ===")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\n--- Output ---")
print("Hello,", name)
print("Next year, you will be", age + 1)
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
    print("Floor division:", num1 // num2)
    print("Remainder:", num1 % num2)
else:
    print("Division, floor division, and remainder are undefined because the second number is zero.")

print("Is the first number greater than the second?", num1 > num2)
