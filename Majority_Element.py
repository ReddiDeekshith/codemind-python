n=int(input())
a=list(map(int,input().split()))
s=[]
max=0
c=1
for i in range(len(a)):
    c=1
    for j in range(i+1,len(a)):
        if(a[i]==a[j]):
            c+=1
    if(c>n//2):
        s.clear()
        s.append(a[i])
if(len(s)==0):
    print('-1')
else:
    print(s[0])
