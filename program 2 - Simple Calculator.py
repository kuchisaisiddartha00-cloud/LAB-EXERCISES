# Program 2: Simple Calculator

print("=== Simple Calculator ===")
a = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ").strip()
b = float(input("Enter second number: "))

if operator == "+":
    result = a + b
elif operator == "-":
    result = a - b
elif operator == "*":
    result = a * b
elif operator == "/":
    if b == 0:
        print("Error: division by zero is not allowed.")
        raise SystemExit
    result = a / b
else:
    print("Invalid operator.")
    raise SystemExit

print("Result:", result)
