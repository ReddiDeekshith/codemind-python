n=int(input())
a=list(map(int,input().split()))
s=[]
for i in a:
    if i not in s:
        s.append(i)
s1=[]
for i in s:
    c=0
    for j in a:
        if(i==j):
            c+=1
    if(c==1):
        s1.append(i)
if(len(s1)==0):
    print('-1')
else:
    for i in s1:
        print(i,end=' ')