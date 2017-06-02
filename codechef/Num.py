n,p = map(int,input().split())
d = []
for i in range(1,n+1):
    t = int(input())
    d.append(t)
count = 0
for i in range(0,len(d)):
    
    if d[i]%k == 0:
        count = count + 1
print(count)
