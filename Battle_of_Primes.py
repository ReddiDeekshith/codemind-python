def is_prime(n):
    for i in range(2,n):
        if(n%i==0):
            return 0
    else:
        return 1
a=int(input())
b=int(input())
c=a+b
t=c+1
while(1):
    if(is_prime(t)):
        break
    else:
        t+=1
print(t-c)