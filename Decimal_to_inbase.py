n=int(input())
b=int(input())
s=""
t=n
while(t!=0):
    r=t%b
    s+=str(r)
    t=t//b
a=s[::-1]
c=0
m=0
if '0' not in a:
    print("-1")
else:
    for i in a:
        if i=='0':
            c+=1
        else:
            if c>m:
                m=c
            c=0
    if c>m:
        m=c
    print(m)
