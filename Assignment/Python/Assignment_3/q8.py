l1 = []
l2 = []
s1 = set()
s2 = set()

n1 = int(input("How many numbers want to enter: "))
for x in range(n1):
    num = int(input("Enter the number: "))
    l1.append(num)
    s1.add(num)
n2 = int(input("How many numbers want to enter: "))
for x in range(n2):
    num = int(input("Enter the number: "))
    l2.append(num)
    s2.add(num)


if s1.intersection(s2):
    print("True")
else:
    print("False")