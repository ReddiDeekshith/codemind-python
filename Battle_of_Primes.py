a=int(input())
b=int(input())
m=a+b
while(1):
    c=m+1
    for i in range(2,c):
        if(c%i==0):
            m=m+1
            break
    else:
        break
print(c-(a+b))