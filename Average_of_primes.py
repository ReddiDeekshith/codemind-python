def prime(a):
    if a<=1:
        return 0
    for i in range(2,a):
        if a%i==0:
            return 0
    return 1
n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if prime(i)==1:
        a.append(i)
print("%.2f"%(sum(a)/len(a)))