m=int(input())
a=list(map(int,input().split()))
if a==sorted(a) and len(a)==len(set(a)):
    print("yes")
else:
    print("no")
