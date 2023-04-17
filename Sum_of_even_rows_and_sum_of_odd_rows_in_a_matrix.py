a,b=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(a)]
s1=0
s2=0
for i in range(0,a):
    for j in range(0,b):
        if(i==0 or i%2==0):
            s1=s1+mat[i][j]
        else:
            s2=s2+mat[i][j]
print(s1,s2)