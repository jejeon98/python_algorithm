import sys
sys.stdin=open("input.TXT","rt")
n,m=map(int,input().split())
nlist=list(map(int,input().split()))

nlist.sort()
lt=0
rt=n-1

while(True):
    mid=(lt+rt)//2
    if nlist[mid]==m:
        print(mid+1)
        break
    elif nlist[mid]>m:
        rt=mid-1
    elif nlist[mid]<m:
        lt=mid+1
