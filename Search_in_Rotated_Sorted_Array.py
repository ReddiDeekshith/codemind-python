n=int(input())
a=list(map(int,input().split()))
k=int(input())
for i in range(len(a)):
    if(a[i]==k):
        print(i,end=' ')
        break
else:
    print('-1')