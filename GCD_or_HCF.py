a,b=map(int,input().split())
s=0
for i in range(1,a*b):
    if(a%i==0 and b%i==0):
        s=i
print(s)