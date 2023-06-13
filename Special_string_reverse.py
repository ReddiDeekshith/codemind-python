n=input()
l=list(n)
s=[]
for i in l:
    if(i.isalpha()):
        s.append(i)
s.reverse()
j=0
for i in range(len(l)):
    if(l[i].isalpha()):
        l[i]=s[j]
        j+=1
print(''.join(l))