n=int(input())
a=list(map(int,input().split()))
l=len(str(max(a)))
c=0
for i in a:
    if len(str(i))==l:
        c+=1
print(c)