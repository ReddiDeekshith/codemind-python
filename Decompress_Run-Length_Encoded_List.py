n=int(input())
a=list(map(int,input().split()))
s=[]
for i in range(0,n-1,2):
    for j in range(a[i]):
        s.append(a[i+1])
for i in s:
    print(i,end=' ')
    