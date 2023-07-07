n=int(input())
l=list(map(int,input().split()))
print(sum(l[0:n//2]),sum(l[n//2:n]),sep="
")