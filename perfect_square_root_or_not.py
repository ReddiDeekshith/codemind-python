n=int(input())
import math
c=0
s=int(math.sqrt(n))
for i in range(1,s+1):
    if(i*i==n):
        c=1
        break
print(c==1)