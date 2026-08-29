salary  =int(input("Enter  salary: "))
if (salary < 30000):
    print(0.05*salary)
elif (salary <= 70000):
    print(0.15*salary)
else:
    print(0.25*salary)
