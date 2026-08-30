word = ["apple","banana","kiwi","cherry","mango"]
d = {}
for val in word:
    d.update({val:len(val)})

print(d)