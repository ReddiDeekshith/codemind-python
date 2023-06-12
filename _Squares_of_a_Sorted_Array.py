n=int(input())
a=list(map(int,input().split()))
s=[]
for i in a:
    s.append(i*i)
s.sort()
for i in s:
    print(i,end=' ')
    