n=int(input())
l=list(map(int,input().split()))
print(abs(sum(l[0:n//2])-sum(l[n//2:n])))