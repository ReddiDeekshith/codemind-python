def far(n):
    t=n
    while(1):
        s=t
        for i in range(2,s//2):
            if s%i==0:
                t=t+1
                break
        else:
            break
    return s 
def near(n):
    t=n
    while(1):
        s=t
        for i in range(2,s//2):
            if s%i==0:
                t=t-1
                break
        else:
            break
    return s  
s=int(input())
a=near(s)
b=far(s)
if(b-s>=s-a):
    print(abs(s-a))
elif(b-s<s-a):
    print(b-s)
    
    