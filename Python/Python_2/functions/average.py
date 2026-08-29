def average(a,b,c):
    av = (a+b+c)/3
    return av
print(average(1,2,3))

# Creating default value
def average(a,b,c = 1):
    av = (a+b+c)/3
    return av
print(average(1,2,3))

# Default parameter should come at last and it sould not be followed by any non default parameter