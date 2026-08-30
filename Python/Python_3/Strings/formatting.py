# FORMAT FUNCTION
a = 40
b = 10
sum = a+b

# normal formatting
print("language is {}".format("python"))
print("The sum of {} and {} is {}".format(a,b,sum))

# index-based formatting
print("The sum of {1} and {0} is {2}".format(a,b,sum))

# value-based formatting
print("the values of var are {a} and {b}".format(a = 5 , b = 10 ))


# F-string
# We use literal string interpolation

print(f"sum of {a} and {b} is {a+b}")