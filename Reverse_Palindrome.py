n=int(input())
s=str(n)
while(1):
    s=str(int(s)+int(s[::-1]))
    if s==s[::-1]:
        print(s)
        break
