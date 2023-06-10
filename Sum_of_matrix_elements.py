m=int(input())
n=int(input())
s=[]
for i in range(m):
    a=list(map(int,input().split()))
    s.extend(a)
print(sum(s))