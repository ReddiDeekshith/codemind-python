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
n=int(input())
for i in range(n):
    s=int(input())
    a=near(s)
    b=far(s)
    if(b-s>=s-a):
        print(a)
    elif(b-s<s-a):
        print(b)
    