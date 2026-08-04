def factorial(z):
    if z == 1:
        return 1
    return z * factorial(z - 1)
jems = int(input("Enter a number to find the factorial: "))
print(f"The factorial of {jems} is {factorial(jems)}")