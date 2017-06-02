T = int(input())
if(1 <= T <= 100):
    A = []
    for i in range(T):
        N = int(input())
        if(1<=N<=100000):
            x = [int(i) for i in input().split() if(1<=int(i)<=100000000)]
            A.append(x)
    for i in range(len(A)):
        if(len(A[i])==1):
            print("NO")
        elif(len(A[i])==2):
            if(A[i][0] <= A[i][1]):
                print("YES")
            else:
                print("NO")
        else:
            j = 0
            while(j != len(A[i])-1):
                k = j + 1
                while(k != len(A[i])):
                    if(A[i][j] <= A[i][k]):
                        print("YES")
                        break
                    k = k + 1
                j = j + 1
            if(j == len(A[i])-1):
                print("NO")
                