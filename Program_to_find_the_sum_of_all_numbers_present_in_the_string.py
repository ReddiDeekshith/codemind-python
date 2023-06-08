s=input()
a=[]
for i in s:
    if i.isdigit():
        a.append(int(i))
print(sum(a))