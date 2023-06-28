def selfdiv(a):
    s=str(a)
    c=0
    for i in s:
        if(i=='0'):
            return 0
        elif(a%(int(i))==0):
            c+=1
    if(c==len(s)):
        return 1
    else:
        return 0
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(selfdiv(i)):
        print(i,end=' ')