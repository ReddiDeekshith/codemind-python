n=int(input())
a=list(map(int,input().split()))
s=[]
s1=[]
for i in a:
    if(i==0):
        s1.append(i)
    else:
        s.append(i)
s.extend(s1)
for i in s:
    print(i,end=' ')