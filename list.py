numbers = [1, 2, 1, 3, 1, 6, 6, 7, 8, 8, 6, 9, 9, 5]
for item in numbers:
    x = numbers.count(item)
    if x > 1:
        numbers.remove(item)
numbers.sort()
print(numbers)