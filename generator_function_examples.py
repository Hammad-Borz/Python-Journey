def count_to_five():
    for x in range(1, 6):
        yield x
for numbers in count_to_five():
 print(numbers)
def even_numbers(n):
    for z in range(0, n + 1, 2):
        yield z
for number in even_numbers(10):
    print(number)
def squares(n):
    for a in range(1, n + 1):
        yield a ** 2
for numbers in squares(5):
    print(numbers)
