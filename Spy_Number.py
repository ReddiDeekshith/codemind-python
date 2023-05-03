n=int(input())
t=n
sums=0
pro=1
while(t!=0):
    r=t%10
    sums+=r
    pro*=r
    t=t//10
if(sums==pro):
    print("Spy Number")
else:
    print("Not Spy Number")