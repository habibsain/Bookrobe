name = input('What is your name?\n')
x = len(name)
if x < 3:
    print('Name must be of atleast 3 characters\n')
elif x > 50:
    print('Name must be of atmost 50 characters\n')
else:
    print('It looks good')