T = int(input())
for i in range(T):
    N = int(input())
    a = "{0:b}".format(N)
    print(min(abs(N - 2**(len(a)-1)),abs(N - 2**len(a))))