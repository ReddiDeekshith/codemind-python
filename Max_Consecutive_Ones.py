n=int(input())
a=list(map(int,input().split()))
c=0
max1=0
for i in range(len(a)):
    if(a[i]==1):
        c+=1
    else:
        if(max1<c):
            max1=c
        c=0
if(max1<c):
    max1=c
print(max1)