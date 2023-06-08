n=input()
e=[]
o=[]
c=0
for i in n:
    if i.isdigit():
        if(int(i)%2==0):
            e.append(int(i))
        else:
            o.append(int(i))
    elif i.isalnum():
        continue
    elif i.isalpha():
        continue
    else:
        c+=1
if(c%2==0):
    if(len(e)>=len(o)):
        for i in range(len(o)):
            print(e[i],end='')
            print(o[i],end='')
        for i in range(len(o),len(e)):
            print(e[i],end='')
    else:
        for i in range(len(e)):
            print(e[i],end='')
            print(o[i],end='')
        for i in range(len(e),len(o)):
            print(o[i],end='')