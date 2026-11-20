# Program 7: Fibonacci Series Using Recursion

def fibonacci(n):
    """Return the nth Fibonacci number, where F(0)=0 and F(1)=1."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

terms = int(input("How many Fibonacci terms do you want? "))

if terms < 0:
    print("Please enter a non-negative number.")
else:
    print("Fibonacci series:")
    for index in range(terms):
        print(fibonacci(index), end=" ")
    print()
