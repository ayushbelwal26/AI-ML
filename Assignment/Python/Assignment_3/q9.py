l = [1,1,1,2,3,3,5,5,6,4]
s = set()
s2 = set()
for val in l:
    if val not in s:
        s.add(val)
    else:
        s2.add(val)

print(f"The repeating values are {s2}")