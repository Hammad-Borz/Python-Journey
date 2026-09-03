def sum_numbers(*args):
    total = 0
    for number in args:
        total += number
    return total
count = int(input("How many numbers do you want to sum? "))
numbers = []
for i in range(count):
    numbers.append(int(input(f"Enter number {i+1}: ")))
print("The sum of the numbers is:", sum_numbers(*numbers))
