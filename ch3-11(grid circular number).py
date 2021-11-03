import sys
sys.stdin=open("input.TXT","rt")
nlist=[list(map(int,input().split())) for _ in range(7)]

cnt=0
for i in range(0,3):
    for j in range(0,7):
        new=[]
        for k in range(5):
            new.append(nlist[i+k][j])
        revnew=new[::-1]
        if new==revnew:
            cnt+=1

for i in range(0,7):
    for j in range(0,3):
        new=[]
        for k in range(5):
            new.append(nlist[i][j+k])
        revnew=new[::-1]
        if new==revnew:
            cnt+=1
print(cnt)