import sys 
sys.stdin=open("input.txt","rt")
n,m=list(map(int, input().split()))
nn=[]
mm=[]
out=[]
check=[]
max=1
cntnum=[]
for i in range (1,n+1):
    nn.append(i)
for i in range (1,m+1):
    mm.append(i)
for i in range(n):
    for j in range(m):
        out.append(nn[i]+mm[j])
result=sorted(out)
for i in range(2,50):
    check.append(i)
    cntnum.append(0)
for i in range(len(check)):
    for j in range(len(result)):
        if(check[i]==result[j]):
            cntnum[i]+=1
for i in range(len(cntnum)):
    if(cntnum[i]>max):
        max=cntnum[i]
for i in range(len(cntnum)):
    if(cntnum[i]==max):
        print(i+2, end=' ')