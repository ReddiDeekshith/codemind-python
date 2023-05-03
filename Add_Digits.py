n=int(input())
t=n
sum=0
while(t!=0):
    r=t%10
    sum=sum+r
    t=t//10
    if(t==0 and sum>=10):
        t=sum
        sum=0
print(sum)