test_case = int(input())
if(1<=test_case<=100000):
    a = []
    b = []
    for i in range(test_case):
        x = [int(i) for i in input().split() if(-1000000000<=int(i)<=1000000000)]
        y = [int(i) for i in input().split() if(-1000000000<=int(i)<=1000000000)]
        a.append(x)
        b.append(y)
    for i in range(len(a)):
        for j in range(len(b)):
            if(i == j):
                if(a[i][0] == a[i][2]):        #Vertical case for a
                    leng = abs(a[i][1] - a[i][3])+1
                    if(leng > 1):
                        if(b[j][0] == b[j][2]):    #Vertical case for b
                            s = abs(b[j][1] - b[j][3]) + 1
                            if(s > 1):
                                if(b[j][0] == a[i][0]):
                                    h = 0
                                    for k in range(min(a[i][1],a[i][3]),max(a[i][1],a[i][3])+1):
                                        h = k + 1
                                        if(b[j][1] == k or b[j][3] == k):
                                            print("yes")
                                            break
                                        if(h == max(a[i][1],a[i][3])+1  ):
                                            print("no")
                                            break
                                else:
                                    print("no")
                                    break
                            else:
                                if(b[j][0] == a[i][0]):
                                    h = 0
                                    for k in range(min(a[i][1],a[i][3]),max(a[i][1],a[i][3])+1):
                                        h = k + 1
                                        if(b[j][0] == k or b[j][1] == k):
                                            print("yes")
                                            break
                                        if(h == max(a[i][1],a[i][3])+1  ):
                                            print("no")
                                            break
                                else:
                                    print("no")
                                    break
                        elif(b[j][1] == b[j][3]):
                            s = abs(b[j][0] - b[j][2]) + 1
                            if(s > 1):
                                if(b[j][1] == a[i][1] or b[j][1] == a[i][3]):
                                    if(b[j][0] == a[i][0] or b[j][2] == a[i][0]):
                                        print("yes")
                                        break
                                    else:
                                        print("no")
                                        break
                                else:
                                    print("no")
                                    break
                            else:
                                if(b[j][0] == a[i][0]):
                                    h = 0
                                    for k in range(min(a[i][1],a[i][3]),max(a[i][1],a[i][3])+1):
                                        h = k + 1
                                        if(b[j][0] == k or b[j][1] == k):
                                            print("yes")
                                            break
                                        if(h == max(a[i][1],a[i][3])+1  ):
                                            print("no")
                                            break
                                else:
                                    print("no")
                                    break
                        else:
                            print("no")
                            break
                    else:
                        if(b[j][0] == b[j][2]):
                            s = abs(b[j][1] - b[j][3]) + 1
                            if(s > 1):
                                if(b[j][0] == a[i][0]):
                                    h = 0
                                    for k in range(min(b[j][1],b[j][3]),max(b[j][1],b[j][3])+1):
                                        h = k + 1
                                        if(a[i][0] == k or a[i][1] == k):
                                            print("yes")
                                            break
                                        if(h == max(b[j][1],b[j][3])+1  ):
                                            print("no")
                                            break
                                else:
                                    print("no")
                                    break
                            else:
                                if(a[i][0] == b[j][0] and a[i][1] == b[j][1]):
                                    print("yes")
                                    break
                                else:
                                    print("no")
                                    break
                        elif(b[j][1] == b[j][3]):
                            s = abs(b[j][0] - b[j][2]) + 1
                            if(s > 1):
                                if(b[j][1] == a[i][1]):
                                    h = 0
                                    for k in range(min(b[j][1],b[j][3]),max(b[j][1],b[j][3])+1):
                                        h = k + 1
                                        if(a[i][0] == k or a[i][1] == k):
                                            print("yes")
                                            break
                                        if(h == max(b[j][1],b[j][3])+1  ):
                                            print("no")
                                            break
                                else:
                                    print("no")
                                    break
                            else:
                                if(a[i][0] == b[j][0] and a[i][1] == b[j][1]):
                                    print("yes")
                                    break
                                else:
                                    print("no")
                                    break
                        else:
                            print("no")
                            break
                elif(a[i][1] == a[i][3]):       #Horizontal case for a
                    leng = abs(a[i][0] - a[i][2])+1
                    if(leng > 1):
                        if(b[j][0] == b[j][2]):
                            s = abs(b[j][1] - b[j][3]) + 1
                            if(s > 1):
                                if(b[j][0] == a[i][0] or b[j][0] == a[i][2]):
                                    if(b[j][1] == a[i][1] or b[j][3] == a[i][1]):
                                        print("yes")
                                        break
                                    else:
                                        print("no")
                                        break
                                else:
                                    print("no")
                                    break
                            else:
                                if(b[j][1] == a[i][1]):
                                    h = 0
                                    for k in range(min(a[i][0],a[i][2]),max(a[i][0],a[i][2])+1):
                                        h = k + 1
                                        if(b[j][0] == k or b[j][1] == k):
                                            print("yes")
                                            break
                                        if(h == max(a[i][0],a[i][2])+1  ):
                                            print("no")
                                            break
                                else:
                                    print("no")
                                    break
                        elif(b[j][1] == b[j][3]):    
                            s = abs(b[j][0] - b[j][2]) + 1
                            if(s > 1):
                                if(b[j][1] == a[i][1]):
                                    h = 0
                                    for k in range(min(a[i][0],a[i][2]),max(a[i][0],a[i][2])+1):
                                        h = k + 1
                                        if(b[j][0] == k or b[j][2] == k):
                                            print("yes")
                                            break
                                        if(h == max(a[i][0],a[i][2])+1  ):
                                            print("no")
                                            break
                                else:
                                    print("no")
                                    break
                            else:
                                if(b[j][1] == a[i][1]):
                                    h = 0
                                    for k in range(min(a[i][0],a[i][2]),max(a[i][0],a[i][2])+1):
                                        h = k + 1
                                        if(b[j][0] == k or b[j][1] == k):
                                            print("yes")
                                            break
                                        if(h == max(a[i][0],a[i][2])+1  ):
                                            print("no")
                                            break
                                else:
                                    print("no")
                                    break
                        else:
                            print("no")
                            break
                else:
                    print("no")
                    break  
           
        