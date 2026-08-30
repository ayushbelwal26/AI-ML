nums = [1,2,3,10,4]
x = int(input("Enter number to search: "))
idx = 0
for val in nums:
    if (val == x ):
        print(idx)
        break
    idx += 1
