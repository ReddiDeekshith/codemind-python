n=int(input())
l=list(map(int,input().split()))
x,y=map(int,input().split())
a=[]
for i in l:
    if x<=i and y>=i:
        a.append(i)
if(len(a)==0):
    print(-1)
else:
    print(*a)
