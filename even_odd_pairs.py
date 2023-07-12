n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in l:
    if i%2==0:
        a.append(i)
    else:
        b.append(i)
c=[]
i=0
j=0
while(i<len(a) and j<len(b)):
    c.append(a[i])
    c.append(b[j])
    i+=1
    j+=1
while(i<len(a)):
    c.append(a[i])
    i+=1
while(j<len(b)):
    c.append(b[j])
    j+=1
if n%2==1:
    c.append(0)
print(*c)
    