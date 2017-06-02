from functools import reduce
def gcd(m,n):
    while(m%n != 0):
        (m,n) = (n,m%n)
    return(n)
def gsub(a):
    l = []
    for i in range(len(a)):
        for j in range(i,len(a)):            
            l.append(reduce(gcd,([a[m] for m in range(i,j+1)])))
    return sorted(l)
N,Q = map(int, input().split())
c = [int(i) for i in input().split()]
if(len(c) == N):
    q = []
    for i in range(Q):
        q.append(int(input()))
ml = [0] + gsub(sorted(c,reverse = True))
for i in range(len(q)):
    print(ml[q[i]])
    
    