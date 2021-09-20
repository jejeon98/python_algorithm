import sys
sys.stdin=open("input.TXT","rt")
n=int(input())
nlist=[list(map(int,input().split())) for _ in range(n)]
s=int(input())
for _ in range(s):
    s1,s2,s3=map(int, input().split())
    if s2==0:
        for _ in range(s3):
            nlist[s1-1].append(nlist[s1-1].pop(0))
    else:
        for _ in range(s3):
            nlist[s1-1].insert(0,nlist[s1-1].pop()) 

sum=0
a=0
b=n
for i in range((n-1)//2):
    for j in range(a,b):
        sum+=nlist[i][j]
    a+=1
    b-=1
aa=((n-1)//2)-1
bb=((n+1)//2)+1
for i in range((n+1)//2,n):
    for j in range(aa,bb):
        sum+=nlist[i][j]
    aa-=1
    bb+=1
sum+=nlist[(n-1)//2][(n-1)//2]
print(sum)