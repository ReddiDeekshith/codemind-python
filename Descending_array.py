m=int(input())
a=list(map(int,input().split()))
a1=list(tuple(a))
a1.sort(reverse=True)
if a==a1:
    print("yes")
else:
    print("no")
