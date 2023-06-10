n=int(input())
a=list(map(int,input().split()))
s=list(set(a))
k=s
m=0
s.sort()
if(len(s)<3):
    print(max(s))
else:
    for i in range(3):
        m=max(k)
        k.remove(m)
    print(m)
    