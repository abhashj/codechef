c = []
x = int(input())
for i in range(1,x+1):
    y = int(input())
    c.append(y)
for j in range(0,len(c)):
    i = 1
    p = int(c[j]/5)
    sum = p
    while(p!=0):
        i = i + 1 
        p = int(c[j]/(5)**i)
        sum = sum + p
    print(sum)