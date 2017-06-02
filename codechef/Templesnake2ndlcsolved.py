S = int(input())
if(1<=S<=100):
    c = []
    for i in range(S):
        N = int(input())
        if(3<=N<=100):
            H = [int(i) for i in input().split() if(1<=int(i)<=100)]
            c.append(H)
    for i in range(len(c)):
        if(len(c[i])%2 != 0):
            if(c[i][0] == 1 and c[i][len(c[i])-1] == 1):
                if(c[i][int((len(c[i])-1)/2)] == max(c[i])):
                    j = 1
                    while(j <= (len(c[i])-1)/2):
                        if(c[i][j] - c[i][j-1] == 1):
                            j = j + 1
                        else:
                            print("no")
                            break
                    if(j == (len(c[i])-1)/2 + 1):
                        while(j <= len(c[i])-1):
                            if(c[i][j-1] - c[i][j] == 1):
                                j = j + 1
                            else:
                                print("no")
                                break
                    if(j == len(c[i])):
                        print("yes")
                else:
                    print("no")
            else:
                print("no")
        else:
            print("no")
                    
            
            



    