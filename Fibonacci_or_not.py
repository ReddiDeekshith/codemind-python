n=int(input())
a=0
b=1
while(n>=b):
    c=a+b
    a=b
    b=c
print(n==a)
