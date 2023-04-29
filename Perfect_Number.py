n=int(input())
t=n
sum=0
for i in range(1,n):
    if t%i==0:
        sum=sum+i
print(sum==n)
    