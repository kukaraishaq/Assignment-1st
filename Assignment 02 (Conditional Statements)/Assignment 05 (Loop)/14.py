# Program to calculate factorial of a number

# Input from user
n = int(input("Enter a positive integer: "))

# Check conditions
if n < 0:
    print("Factorial does not exist for negative numbers.")
elif n == 0:
    print("The factorial of 0 is 1")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print("The factorial of", n, "is:", factorial)
