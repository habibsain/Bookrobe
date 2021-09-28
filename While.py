sNum = 5
gCount = 0
gLimit = 3
while gCount < gLimit:
    guess = int(input("guess: "))
    gCount += 1
    if(guess == sNum):
        print("You have won!")
        break

else:
    print("You Lose!")
