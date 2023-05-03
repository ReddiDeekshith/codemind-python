n=input()
c=0
for i in n:
    if(i=="6" and c==0):
        print("9",end="")
        c=1
        continue
    print(i,end="")