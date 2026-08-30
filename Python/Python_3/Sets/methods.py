s ={1,2,2,2,3}

# add - adds a val
s.add(5)
print(s)

# remove - removes a val
s.remove(1)
print(s)

# clear - empties set
s.clear()
print(s)

# pop - removes a random val
s ={1,2,2,2,3}
s.pop()
print(s)

# union - returns new union
s2 = {4,6,8,9,7}
print(s.union(s2))

# intersection - returns new intersection
print(s.intersection(s2))
