from itertools import permutations
a,b=map(int,input().split())
c=1
s=''
for i in range(a):
    s=s+str(c)
    c+=1
k=1
for p in permutations(s,a):
    if(k==b):
        print(''.join(p))
        break
    k=k+1