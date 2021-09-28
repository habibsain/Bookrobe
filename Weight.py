weight = input('Weight: ')
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    print(f'Your Weight is {float(weight) * 0.45359237} kg')
elif unit.upper() == "K":
    print(f'Your Weight is {float(weight) / 0.45359237} lbs')
else:
    print('Invalid unit!')