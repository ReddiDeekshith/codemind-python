def is_prime(n):
    for i in range(2,n):
        if(n%i==0):
            return 0
    return 1
n=int(input())
c=1
for i in range(1,n+1):
    if(n%i==0):
        if(is_prime(i)==0):
            c+=1
print(c)
            