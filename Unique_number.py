n=input()
l=len(n)
c=0
for i in range(l):
    m=i+1
    for j in range(m,l):
        if(n[i]==n[j]):
            c+=1
if(c==0):
    print("Unique Number")
else:
    print("Not Unique Number")
