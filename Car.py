i = 0
f = 1
x = ""
while True:
    x = input("> ").upper()
    if x == 'HELP':
        print("start - to start the car\nstop - to stop the car\nquit - to exit")
    elif x == 'START':
        if i == 0:
            print("Car started... Ready to go")
            i += 1
            f -= 1
        else:
            print("Car has already started, Dude!")
    elif x == 'STOP':
        if f == 0:
            print("Car stopped.")
            f += 1
            i -= 1
        else:
            print("Car has already stopped, Dude!")
    elif x == 'QUIT':
        print("You Quit!")
        break
    else:
        print("I don't understand that...\n")