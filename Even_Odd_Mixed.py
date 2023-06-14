n=input()
l=list(n)
c,c1=0,0
for i in range(len(l)):
    if(int(l[i])%2==0):
        c+=1
    else:
        c1+=1
if(c==len(l)):
    print("Even")
elif(c1==len(l)):
    print("Odd")
else:
    print("Mixed")