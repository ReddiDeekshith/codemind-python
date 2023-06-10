n=int(input())
a=list(map(int,input().split()))
t=int(input())
for i in range(t):
    print(a[i],a[t+i],end=' ')