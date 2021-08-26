import sys
sys.stdin=open("input.txt","rt")
f=sys.stdin
n=int(input())
fw=[]
for i in range(n):
    a=list(f.readline().strip().upper())
    lw=[]
    for j in range(0,len(a)):
        lw+=a[len(a)-(j+1)]
    if(lw==a):
        print("#",i+1, "YES")
    else:
        print("#",i+1, "NO")


