tup = (1,2,3,4,5,6,7,8,9,10)
tup1 = ()
tup2 = ()

for val in tup:
    if(val % 2 == 0):
        tup1 = tup1 + (val,)
    else:
        tup2 = tup2 + (val,)

print(f"The even tuple is {tup1}")
print(f"The odd tuple is {tup2}")