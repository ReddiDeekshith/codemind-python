n=int(input())
a=0
b=1
for i in range(n):
    c=a+b
    print(a,end=' ')
    a=b
    b=c