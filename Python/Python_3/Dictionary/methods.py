info = {
    "name":"ayush",
    "cgpa":"9.65",
    "subject":["maths","science"]
}

# keys - returns all keys
print(info.keys())

# values -  rtuens all values
print(info.values())

# items - returns (key,val) pairs
print(info.items())

# get - returns val acc. to key
print(info.get("cgpa"))

# update - add new item
info.update({"city":"Delhi"})
print(info)