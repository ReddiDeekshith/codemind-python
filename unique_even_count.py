def unique(n):
    s=str(n)
    a=list(s)
    a.sort()
    for i in range(len(a)-1):
        if(a[i]==a[i+1]):
            return 0
    return 1
n=int(input())
a=list(map(int,input().split()))
c=0
for i in list(set(a)):
    if(unique(i) and i%2==0):
        c+=1
if(c==4):
    print(a)
print(c)