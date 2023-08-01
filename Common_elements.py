m,n=map(int,input().split())
a=list(map(int,input().split()))
a1=list(map(int,input().split()))
s=[]
for i in a:
    if i in a1 and i not in s:
        s.append(i)
print(*s)
