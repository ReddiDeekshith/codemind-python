n=int(input())
a=list(map(int,input().split()))
m=min(a)
m1=max(a)
mi=a.index(m)
ma=a.index(m1)
c=0
for i in range(min(mi,ma),max(mi,ma)+1):
    if(a[i]<=1):
        continue
    for j in range(2,a[i]):
        if(a[i]%j==0):
            break
    else:
        c+=1
print(c)
    