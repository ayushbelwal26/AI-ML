num = 9
while True:
    guess = int(input("Take you guess: "))
    if(guess > num):
        print("Too High")
    elif(guess < num):
        print("Too low")
    else:
        print("Correct")
        break


