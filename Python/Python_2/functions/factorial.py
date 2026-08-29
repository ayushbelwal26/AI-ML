def fact(n):
    prd = 1
    for i in range(1,n+1):
        prd *= i
    return prd

print(fact(5))