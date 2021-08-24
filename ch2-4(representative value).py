import sys 
sys.stdin=open("input.txt","rt")
n=int(input())
a=list(map(int, input().split()))
sum=0
for i in range(n):
    sum+=a[i]
avg=(sum/n)
a.append(avg)
b=sorted(a)
avg_index=b.index(avg)
num=b[avg_index+1]
for i in range (n-1):
    if(num==a[i]):
        print(round(avg), a.index(num)+1)
        break
