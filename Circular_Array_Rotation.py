n,k,q=map(int,input().split())
a=list(map(int,input().split()))
for i in range(k):
    for k in range(1,len(a)):
        for j in range(len(a)-1):
            a[j],a[j+1]=a[j+1],a[j]
for i in range(q):
    f=int(input())
    print(a[f])
