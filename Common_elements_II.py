m,n=map(int,input().split())
a=list(map(int,input().split()))
a1=list(map(int,input().split()))
s=[]
for i in a:
    if i not in a1:
        s.append(i)
for j in a1:
    if j not in a:
        s.append(j)
print(*s)