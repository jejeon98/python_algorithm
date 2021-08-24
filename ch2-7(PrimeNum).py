import sys 
sys.stdin=open("input.txt","rt")
n=int(input())
cntlist=[0]*(n+1)
cnt =0
for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            cntlist[i]+=1
    if(cntlist[i]==0):
        cnt+=1

print(cnt)