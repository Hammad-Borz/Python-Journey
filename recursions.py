def count_up(x):
    if x <= 0:
        return
    count_up(x - 1)
    print(x)
count_up(5)
def sum_numbers(n):
    if n <= 0:
        return 0
    return n + sum_numbers(n - 1)
print(sum_numbers(7))
def countdown(z):
    if z == 0:
        print("Blastoff!")
        return
    print(z)
    countdown(z - 1)
countdown(5)