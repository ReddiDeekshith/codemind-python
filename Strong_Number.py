import math
n=int(input())
s=str(n)
s1=0
for i in s:
    s1=s1+math.factorial(int(i))
if(s1==n):
    print("The number %d is a strong number"%(n))
else:
    print("The number %d is not a strong number"%(n))