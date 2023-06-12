n=int(input())
a=list(map(int,input().split()))
s=[]
for i in a:
    if i in s:
        print(i)
    else:
        s.append(i)
