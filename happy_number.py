n=int(input())
t=n
sum1=0
while(t!=0):
    r=t%10
    sum1=sum1+r**2
    t=t//10
    if(t==0 and sum1>=10):
        t=sum1
        sum1=0
if(sum1==1 or sum1==7):
    print("True")
else:
    print("False")
