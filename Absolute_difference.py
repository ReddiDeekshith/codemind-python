def isprime(a):
    for i in range(2,a):
        if(a%i==0):
            return 0
    return 1
n=int(input())
a=list(map(int,input().split()))
p=1
p1=1
for i in a:
    if(isprime(i)):
        p=p*i
    else:
        p1=p1*i
print(abs(p-p1))