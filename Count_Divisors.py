a,b,c=map(int,input().split())
k=0
for i in range(a,b+1):
    if(i%c==0):
        k+=1
print(k)
        