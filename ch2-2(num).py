import sys 
sys.stdin=open("input.txt","rt")
t = int(input())
for i in range (t):
    n,s,e,k = map(int, input().split())
    a=list(map(int, input().split()))
    a_sort1=a[s-1:e]
    a_sort2=sorted(a_sort1)
    print("#%d %d"%(i+1,a_sort2[k-1]))
