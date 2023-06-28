n=int(input())
a=list(map(int,input().split()))
n1=int(input())
a1=list(map(int,input().split()))
s=[]
for i in range(n):
    s.append(-1)
for i in range(n):
    s.insert(a1[i],a[i])
for i in range(n):
    print(s[i],end=' ')