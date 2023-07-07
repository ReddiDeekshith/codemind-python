def prime(a):
    if a<=1:
        return 0
    for i in range(2,a):
        if a%i==0:
            return 0
    return 1
n=int(input())
l=list(map(int,input().split()))
k=int(input())
a=[]
for i in l:
    if prime(i)==1 and i>=k:
        a.append(i)
print(len(a))