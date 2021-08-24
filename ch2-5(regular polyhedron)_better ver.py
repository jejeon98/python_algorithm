import sys 
sys.stdin=open("input.txt","rt")
n,m=list(map(int, input().split()))
max=1
cntnum=[0]*(n+m+3)
for i in range(1,n+1):
    for j in range(1,m+1):
        cntnum[i+j]+=1
for i in range(len(cntnum)):
    if(cntnum[i]>max):
        max=cntnum[i]
for i in range(len(cntnum)):
    if(cntnum[i]==max):
        print(i, end=' ')