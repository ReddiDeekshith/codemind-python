t=int(input())
for i in range(t):
    t=int(input())
    l=list(map(int,input().split()))
    for i in range(len(l)):
        if sum(l[0:i])==sum(l[i+1::]):
            print(i)
            break
    else:
        print("-1")
            
    