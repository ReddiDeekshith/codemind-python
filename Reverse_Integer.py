n=int(input())
import math
c=0
if n>=0:
    c=1
elif n<0:
    c=-1
s=abs(n)
t=s
rev=0
while(t!=0):
    r=t%10
    rev=rev*10+r
    t=t//10
print(c*rev)
