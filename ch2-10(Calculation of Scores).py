import sys
sys.stdin=open("input.txt","rt")
n=int(input())
nlist=list(map(int,input().split()))
score=[0]*n
sum=0
cnt=0
if nlist[0]==1:
    score[0]=1
else:
    score[0]=0
for i in range(n):
    if (nlist[i-1]==0 and nlist[i]==1):
        score[i]=1
        cnt=1
    elif nlist[i-1]==1 and nlist[i]==1:
        cnt+=1
        score[i]=cnt
        if nlist[i]==0:
            cnt=0
            score[i]=0
    elif nlist[i]==0:
        score[i]=0
for i in range(n):
    sum+=score[i]
print(sum)

