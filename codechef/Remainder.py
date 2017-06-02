test_case = int(input())
c = []
for i in range(test_case):
    x = [int(i) for i in input().split()]
    c.append(x)
for i in range(len(c)):
    print(c[i][0] % c[i][1])
