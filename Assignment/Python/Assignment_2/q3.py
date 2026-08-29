def digits(n):
    while(n != 0):
        print(n%10)
        n = int(n/10)
    return

digits(312)