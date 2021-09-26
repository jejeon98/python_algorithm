import sys
sys.stdin=open("input.TXT","rt")
n=int(input())
nlist=[list(map(int,input().split())) for _ in range(n)]
nlist.insert(0,[0]*n)
nlist.append([0]*n)
for x in nlist:
    x.insert(0,0)
    x.append(0)
dx=[-1,0,1,0]
dy=[0,-1,0,1]
cnt=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if all(nlist[i][j]> nlist[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1
print(cnt)
