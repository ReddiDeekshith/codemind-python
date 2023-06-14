for i in range(int(input())):
    n,r=map(int,input().split())
    a=list(map(int,input().split()))
    k=list(tuple(a))
    for f in range(r):
        for i in range(1,len(k)):
            for j in range(len(k)-1):
                a[j],a[j+1]=a[j+1],a[j]
    for i in range(len(a)):
        if(i==len(a)-1):
            print(a[i])
        else:
            print(a[i],end=' ')
