n=int(input())
t=n
s=0
while(t!=0):
    r=t%10
    s=s+r
    t=t//10
    if(t==0 and s>=10):
        t=s
        s=0
print(s)