n=int(input())
a=list(map(int,input().split()))
n1=int(input())
a1=list(map(int,input().split()))
k=int(input())
c=0
for i in range(n):
    if(a[i]<=k and a1[i]>=k):
        c+=1
print(c)