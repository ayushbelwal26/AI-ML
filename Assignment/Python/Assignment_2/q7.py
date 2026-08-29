while True:
    n = input("Enter: ")
    if(n == 'Quit'):
        break
    if(int(n) > 0):
        print("p")
    elif(int(n) < 0):
        print("n")
print("Outside loop......")