a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
c1=0
for i in range(len(a)):
    if(a[i]>b[i]):
        c+=1
    elif a[i]<b[i]:
        c1+=1
print(c,c1)