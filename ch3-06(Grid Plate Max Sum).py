import sys
sys.stdin=open("input.TXT","rt")
n=int(input())
nlist=[list(map(int, input().split())) for _ in range(n)]
max=1
sum3=0
sum4=0
for i in range(n):
    sum1=0
    for j in range(n):
        sum1+=nlist[i][j]
        if max<=sum1:
            max=sum1
    sum2=0
    for j in range(n):
        sum2+=nlist[j][i]
        if max<=sum2:
            max=sum2

    sum3+=nlist[i][i]
    if max<sum3:
        max=sum3
    sum4+=nlist[i][n-i-1]
    if max<sum3:
        max=sum4
print(max)

        


