numbers = [3, 5, 6, 9, 13, 22]
doubled = list(map(lambda x: x * 3, numbers))
print(doubled)
quantity = [11, 22, 33, 44, 55]
greater_than_30 = list(filter(lambda x: x > 30, quantity))
print(greater_than_30)
items = ["Starc", "Roy", "Hazlewood", "John", "Maxwell"]
print(sorted(items))
print(sorted(items, reverse=True))
print(sorted(items, key=lambda x: len(x)))
