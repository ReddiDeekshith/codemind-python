a=int(input())
b=list(map(int,input().split()))
c1=0
c2=0
for i in b:
    if(i%2==0):
        c1+=1
    else:
        c2+=1
print(c1,c2)