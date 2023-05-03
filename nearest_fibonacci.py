def front(n,a,b):
    while(n>=b):
        c=a+b
        a=b
        b=c
    return b
def back(n,a,b):
    while(n>=b):
        c=a+b
        a=b
        b=c
    return a
n=int(input())
m=front(n,0,1)
s=back(n,0,1)
if(m-n>n-s):
    print(s)
elif(m-n<n-s):
    print(m)
else:
    print(s,m,sep=" ")