n=int(input())
sum1=0
for i in range(1,n):
    if(n%i==0):
        sum1=sum1+i
print(sum1>n)