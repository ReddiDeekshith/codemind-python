def primes(n):
    if n<=1:
        return 0
    else:
        for i in range(2,n):
            if n%i==0:
                return 0
        return 1
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if primes(i)==1:
        c+=1
print(c)