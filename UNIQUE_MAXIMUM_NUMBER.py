n=int(input())
a=list(map(int,input().split()))
c=0
s=[]
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if(a[i]==a[j]):
            c+=1
    if(c==1):
        s.append(a[i])
if(len(s)==0):
    print('-1')
else:
    print(max(s))