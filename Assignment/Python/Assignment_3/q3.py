l1 = []
l2 = []

n1 = int(input("How many numbers want to enter: "))
for x in range(n1):
    num = int(input("Enter the number: "))
    l1.append(num)

n2 = int(input("How many numbers want to enter: "))
for x in range(n2):
    num = int(input("Enter the number: "))
    l2.append(num)

result = l1 + l2
result.sort()

print(result)