n=int(input())
a=list(map(int,input().split()))
s=''
for i in a:
    s=s+str(i)
f=int(s)+1
k=str(f)
for i in k:
    print(i,end=' ')