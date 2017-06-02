test_case = int(input())
for i in range(test_case):
    c = []
    nrows = int(input())
    for j in range(nrows):
        x = [int(i) for i in input().split()]
        c.append(x)
    a = nrows-2
    while(a >= 0):
        for b in range(0,a+1):
            c[a][b] = c[a][b] + max(c[a+1][b],c[a+1][b+1])
        a = a-1
    print(c[0][0])
              