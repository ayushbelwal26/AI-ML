info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English")
]

s = set()
for val in info:
    s.add(val[1])

print(f"Unique courses are : {s}") 


print("Students in English course are: ")
for val in info:
    if(val[1] == "English"):
        print(val[0])

d = dict()
for name , course in info:
    if(d.get(name) == None):
        d.update({name:set()})
        d[name].add(course)
    else:
        d[name].add(course)

print(d)