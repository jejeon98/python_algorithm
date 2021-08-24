import sys 
sys.stdin=open("input.txt","rt")
n,k = map(int, input().split())
a=list(map(int, input().split()))
b=set()
for i in range (n):
    for j in range (i+1, n):
        for t in range(j+1,n):
            new=a[i]+a[j]+a[t]
            b.add(new)
blist=sorted(b, reverse=True)
print(blist)
print(blist[k-1])