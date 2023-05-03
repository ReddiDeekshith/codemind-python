n=input()
sum=0
c=1
for i in n:
    sum=sum+int(i)**c
    c+=1
print(sum==int(n))