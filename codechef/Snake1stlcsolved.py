R = int(input())
if(1<=R<=500):
    c = []
    for i in range(R):
        L = int(input())
        if(1<=L<=500):
            x = input()
            c.append(x)
    b = []
    for i in range(len(c)):
        d = list(c[i])
        b.append(list(filter(lambda a: a != '.', d)))
        if(len(b[i])==0):
            print("Valid")
        else:
            if(b[i][0] == 'T' or b[i][len(b[i])-1] == 'H'):
                print("Invalid")
            else:
                k = 1
                if (k+1 == len(b[i])):
                    print("Valid")
                else:
                    while(k <= len(b[i])-2):
                        if(b[i][k] == 'T'):
                            if(b[i][k+1]== 'H'):
                                k = k + 2
                            else:
                                print("Invalid")
                                break
                        else:
                            print("Invalid")
                            break
                    if(k == len(b[i])-1):
                        print("Valid")
                    
                    
                        
                
    
    
                 
             
        