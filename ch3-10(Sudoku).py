import sys
sys.stdin=open("input.TXT","rt")
nlist=[list(map(int,input().split())) for _ in range(9)]

n=0
cnt=0
dx=[0,0,0,1,1,1,2,2,2]
dy=[0,1,2,0,1,2,0,1,2]

for i in range(0,9,3):
    for j in range(0,9,3):
        num=[0]*9
        for k in range(9):
            p=(nlist[i+dx[k]][j+dy[k]])
            num[p-1]=p
        for a in range(9):
            if num[a]==0:
                cnt+=1
        
if cnt==0:
    print("YES")
else :
    print("NO")
