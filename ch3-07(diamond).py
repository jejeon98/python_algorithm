import sys
sys.stdin=open("input.TXT","rt")
n=int(input())
nlist=[list(map(int,input().split())) for _ in range(n)]
sum=0
sum+=nlist[0][(n-1)//2]
sum+=nlist[n-1][(n-1)//2]
for i in range(n):
    sum+=nlist[(n-1)//2][i]
k=((n-1)//2)-1
for i in range(1,(n-1)//2):
    for j in range(k,n-k):
        sum+=(nlist[i][j])
    k-=1
kk=1
for i in range((n+1)//2,n-1):
    for j in range(kk,n-kk):
        sum+=(nlist[i][j])
    kk+=1    
print(sum)