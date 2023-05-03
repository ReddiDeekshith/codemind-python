n=int(input())
m=n*n
t=m
sums=0
while(t!=0):
    r=t%10
    sums+=r
    t=t//10
if(sums==n):
    print("Neon Number")
else:
    print("Not Neon Number")