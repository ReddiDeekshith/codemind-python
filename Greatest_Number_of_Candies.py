n=int(input())
a=list(map(int,input().split()))
k=int(input())
for i in a:
    print(i+k>=max(a),end=' ')
        