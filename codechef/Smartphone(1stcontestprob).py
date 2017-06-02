ncust = int(input())
budg = []
for i in range(ncust):
    y = int(input())
    budg.append(y)
z = sorted(budg,reverse = True)
maxrev = []
for j in range(len(z)):
    maxrev.append(z[j]*(j+1))
print(max(maxrev))
    
    