n=int(input())
a=list(map(int,input().split()))
s=[]
c=0
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if(a[i]>a[j]):
            c+=1
    s.append(c)
for i in s:
    print(i,end=' ')