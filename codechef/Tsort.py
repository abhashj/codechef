c = []
x = int(input())
for i in range(1,x+1):
    y = int(input())
    c.append(y)
for j in range(0,len(c)):
    
        
    for i in range(0,j+1):
        if i != 3:
            
        
            if c[i] > c[i+1]:
                a = c[i]
                c[i] = c[i+1]
                c[i+1] = a
for i in range(0,len(c)):
    print(c[i])