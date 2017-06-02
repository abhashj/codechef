T = int(input())
l = []
c = []
if(1 <= T <= 5):
    for i in range(T):
        N,Q = map(int,input().split())
        if(1<=N,Q<=100000):
            x = [int(i) for i in input().split() if(1<=int(i)<=1000000000)]
            l.append(x)
            h = []
            for j in range(Q):
                y = int(input())
                if(1<=y<=1000000000):
                    h.append(y)
            c.append(h)
f = []
for i in range(len(l)):
    f.append(sorted((l[i]), reverse = True))
    for j in range(len(c)):
        if(i == j):
            m = 0
            while(m < len(c[j])):
                d = f[i][:]
                if(c[j][m] - d[0] > 0):
                    if(c[j][m] - d[0] > len(d)-1):
                        print('0')
                    else:
                        k = 0
                        while(len(d)-k-1 >= c[j][m] - d[k]):
                            while(d[k] != c[j][m]):
                                d.pop(len(d)-1)
                                d[k] = d[k] + 1
                            k = k + 1
                            if(k == len(d)):
                               break                            
                        print(k)
                else:
                    if(d[len(d)-1]) >= c[j][m]:
                       print(len(d))
                    else:                       
                        k = 0
                        while(d[k] >= c[j][m]):
                            k = k + 1                        
                        if(len(d)-k-1 < c[j][m] - d[k]):
                            print(k)
                        else:
                            while(len(d)-k-1 >= c[j][m] - d[k]):
                                while(d[k] != c[j][m]):
                                    d.pop(len(d)-1)
                                    d[k] = d[k] + 1
                                k = k + 1
                                if(k == len(d)):
                                    break
                            print(k) 
                m = m + 1
                
                