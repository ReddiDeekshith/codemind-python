n=int(input())
a=list(map(int,input().split()))
c=0
c1=0
s=list(set(a))
for i in s:
    c=0
    for j in range(len(a)):
        if(i==a[j]):
            c+=1
    c1=c1+c//2
print(c1)