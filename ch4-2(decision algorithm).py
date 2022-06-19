import sys
sys.stdin=open("input.TXT","rt")
n,m=map(int,input().split())
nlist=[]
for _ in range(n):
    k=int(input())
    nlist.append(k)

large=max(nlist)

lt=0
rt=large

while lt<=rt:#이분 검색이 끝날 때까지
    mid=((lt+rt)//2)
    cnt=0 
    for i in range(n):
        cnt+=nlist[i]//mid #랜선 갯수 갱신
    result=mid 
    if cnt>=m: #랜선의 갯수가 주어진 값보다 크면
        lt=mid+1 
        #중간 값보다 작은 값들을 제거하면서 랜선의 길이를 늘림
    else: #랜선의 갯수가 주어진 값보다 적으면
        rt=mid-1
        #랜선의 길이를 줄여서 랜선의 갯수를 늘림

print(result)
        