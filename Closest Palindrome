def pre(n):
    t=n-1
    m=0
    while(1):
        s=t
        rev=0
        while(s!=0):
            r=s%10
            rev=rev*10+r
            s=s//10
        if(rev==t):
            m=rev
            break
        else:
            t=t-1
    return m
def post(n):
    t=n+1
    m=0
    while(1):
        s=t
        rev=0
        while(s!=0):
            r=s%10
            rev=rev*10+r
            s=s//10
        if(rev==t):
            m=rev
            break
        else:
            t=t+1
    return m
n=int(input())
s=pre(n)
f=post(n)
if(n-s>f-n):
    print(f)
elif(n-s<f-n):
    print(s)
else:
    print(s,f)
