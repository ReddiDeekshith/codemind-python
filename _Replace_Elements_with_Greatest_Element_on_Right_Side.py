n=int(input())
a=list(map(int,input().split()))
for i in range(len(a)):
    if(i==len(a)-1):
        print("-1",)
        break
    print(max(a[i+1:len(a):1]),end=' ')