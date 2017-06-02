from math import factorial
c = []
x = int(input())
for i in range(1,x+1):
    y = int(input())
    c.append(y)
for i in range(0,len(c)):
    print(factorial(c[i]))