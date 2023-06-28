n=int(input())
s=str(n)
s1=0
p=1
for i in s:
    s1=s1+int(i)
    p=p*int(i)
if(s1==p):
    print("Spy Number")
else:
    print("Not Spy Number")
