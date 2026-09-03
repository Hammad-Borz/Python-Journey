def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total
print(multiply(4, 9)) 
print(multiply(6, 9, 17))
print(multiply(3, 7, 8, 13))
def show_info(**info):
    for key, value in info.items():
        print(key, ":", value)
show_info(
    title="Stay Hard",
    author="Goggins",
    year=2018,
    price=77
)
converter = lambda c: (c * 9/5) + 32
print(converter(0))
print(converter(25))
print(converter(100))
