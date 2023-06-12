n=int(input())
a=list(map(int,input().split()))
if(abs(sum(a[1:n:2]))-sum(a[0:n:2])==0):
    print("YES")
else:
    print("NO")
    