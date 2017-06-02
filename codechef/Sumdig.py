test_case = int(input())
c = []
for i in range(test_case):
    x = int(input())
    c.append(x)
for i in range(len(c)):
    dig = []
    p = int(c[i]/10)
    if p == 0:
        print(c[i]%10)
    else:
        dig.append(c[i]%10)
        while(p != 0):
            dig.append(p%10)
            p = int(p/10)
    print(sum(dig))    
        
        