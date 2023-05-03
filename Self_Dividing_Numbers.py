a=int(input())
b=int(input())
for i in range(a,b+1):
    t=i
    c=0
    l=int(len(str(i)))
    while(t!=0):
        r=t%10
        if(r!=0 and i%r==0):
            c+=1
        t=t//10
    if(c==l):
        print(i,end=" ")
        