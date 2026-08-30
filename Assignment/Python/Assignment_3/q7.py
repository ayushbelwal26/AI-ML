s = input("Enter string: ")
count = 0
for val in s:
    if(val == " "):
        count += 1

print(f"The count of spaces is {count}")