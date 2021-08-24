import sys 
sys.stdin=open("input.txt","rt")
n=int(input())
sumlist=[0]*n
nlist=list(map(int, input().split()))
def digit_sum(x):
    for i in range (len(x)):
        for j in range(x[i]):
            sumlist[i]+=x[i]%10
            x[i]=(x[i]//10)
    return sumlist
copy_list=nlist[:]
mmax=digit_sum(copy_list).index(max(digit_sum(copy_list)))
print(nlist[mmax])
