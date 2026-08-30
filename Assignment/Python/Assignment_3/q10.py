str = input("Enter string: ")
s = set()
for char in str:
    s.add(char)

print(f"The uniques character are : {s} ")
print(f"the count is : {len(s)}")