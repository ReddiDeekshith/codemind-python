def is_prime(n):
    if(n==1):
        return 0
    for i in range(2,n):
        if(n%i==0):
            return 0
    else:
        return 1
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(is_prime(i)):
        print(i)
