import sys
sys.stdin=open("input.TXT","rt")
n,m=map(int,input().split())
nlist=list(map(int, input().split()))
cnt=0
sum=nlist[0]
i=0
j=1
while True:
    if sum<m:
        if j<n:
            sum+=nlist[j]
            j+=1
        else:
            break
    elif sum==m:
        cnt+=1
        sum-=nlist[i]
        i+=1
    elif sum>m:
        sum-=nlist[i]
        i+=1
print(cnt)