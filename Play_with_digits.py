n=int(input())
a=list(map(int,input().split()))
sum1=0
for i in a:
    s=str(i)
    for j in s:
        sum1+=int(j)
print(sum1)