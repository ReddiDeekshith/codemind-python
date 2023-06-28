n=int(input())
s=str(n*n)
a=0
for i in s:
    a=a+int(i)
if(a==n):
    print("Neon Number")
else:
    print("Not Neon Number")