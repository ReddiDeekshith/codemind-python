r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
sum=0
for i in mat:
    for j in i:
        sum=sum+j
print(sum)