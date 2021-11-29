n = int(input())
k = 2
while(n>=k):
    d = 2
    Flag = False;
    while(k > d):
        if(k%d == 0):
            Flag = True
        d = d+1
    if not(Flag):
        print(k)
    k = k+1
        
