def fact (n):
    fact_num = 1
    for i in range(1, n+1):
        fact_num *= i
        yield fact_num

for y in fact(4):
    print(y)
