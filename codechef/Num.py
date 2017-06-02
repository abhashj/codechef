n,k = map(int,input().split())
c = []
for i in range(1,n+1):
    t = int(input())
    c.append(t)
count = 0
for i in range(0,len(c)):
    
    if c[i]%k == 0:
        count = count + 1
print(count)