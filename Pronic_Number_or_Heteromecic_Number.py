n=int(input())
c=0
import math
s=int(math.sqrt(n))
for i in range(1,s+1):
    if(i*(i+1)==n):
        c=1
        break
if(c==1):
    print("YES")
else:
    print("NO")