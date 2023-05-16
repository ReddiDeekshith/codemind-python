n=int(input())
s=str(n)
c=0
for i in range(2,n):
    if(n%i==0):
        break
else:
    for i in s:
        if i in "2357":
            c+=1

if(c==len(s)):
    print("Mega Prime")
else:
    print("Not Mega Prime")
    
