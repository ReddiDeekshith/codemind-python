m=int(input())
a=list(map(int,input().split()))
s=[]
for i in range(0,len(a),2):
    s.extend([a[i]]*a[i+1])
print(*s)
    
