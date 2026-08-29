def count_dig(n):
    count = 0
    while(n != 0):
        count += 1
        n = int(n/10)
    return count

print(count_dig(312))