def find_max(message):

    numbers = message.split(",")
    num = []
    for points in numbers:
        x = int(points)
        num.append(x)

    maximum = num[0]

    for item in num:
        if item >= maximum:
            maximum = item
    return maximum


