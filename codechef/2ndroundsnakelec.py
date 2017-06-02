t = int(input())
for k in range(t):
    p = input()
    l = list(p)
    if(len(p) == 1):
        if(l[0] == 'm'):
            print("mongooses")
        else:
            print("snakes")
    elif(len(p) == 2):
        if(l[0] == 'm' or l[1] == 'm'):
            print("mongooses")
        elif(l[0] == 's' and l[1] == 's'):
            print("snakes")
    else:        
        i = 0
        while(i<len(p)-1):
            if(l[i] == 's'):
                if(l[i+1] == 's'):
                    i = i + 1
                else:
                    l[i] = 0
                    i+=2
            else:
                if(l[i+1] == 'm'):
                    i = i + 1
                else:
                    l[i+1] = 0
                    i+=2
        sn = l.count('s')
        mn = l.count('m')
        if(mn > sn):
            print("mongooses")
        elif(mn == sn):
            print("tie")
        else:
            print("snakes")
                 
