numbers = [1005, 1000, 107, 7, 8]
maximum = numbers[0]

for item in numbers:
    if item >= maximum:
        maximum = item
print(maximum)