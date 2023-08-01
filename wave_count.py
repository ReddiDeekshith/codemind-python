m=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,len(a)-2,2):
    if a[i]<a[i+1] and a[i+1]>a[i+2]:
        c+=1
    else:
        print("-1")
        break
else:
    print(c)
