n=int(input())
a=list(map(int,input().split()))
a.sort()
c=0
max1=0
s=[]
k=set(a)
for i in k:
    c=0
    for j in a:
        if(i==j):
            c+=1
    if(c>max1):
        max1=c
        s=i
print(s)
        