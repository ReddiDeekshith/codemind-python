n=int(input())
l=len(str(n))
m=n*n
r=m%(10**l)
if(r==n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
