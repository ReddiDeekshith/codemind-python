import math
t=int(input())
for i in range(t):
    s,a,b,k=map(int,input().split())
    c=s//a
    c1=s//b
    c2=s//((a*b)//math.gcd(a,b))
    if(c+c1-(2*c2)>=k):
        print("Win")
    else:
        print("Lose")