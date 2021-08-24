import sys
sys.stdin=open("input.txt","rt")
n=int(input())
nlist=list(map(int,input().split()))
primes=[]
revlist=[]
def reverse(x):
    revx=0
    cnt=0
    y=x
    z=x
    for i in range(z):
        z=z//10
        cnt+=1
        if z<=0:
            break
    for i in range(cnt-1,0-1,-1):
        revx+=(10**i)*(y%10)
        y=y//10
        if y<=0:
            break
    return revx
for i in range(n):
    revlist.append(reverse(nlist[i]))

def isPrime(x):
    cnt=0
    if x<=1:
        return False
    for i in range(2,x):
        if(x%i==0):
            cnt+=1
    if cnt==0:
        return(x)

for i in range(n):
    if isPrime(revlist[i]):
        primes.append(isPrime(revlist[i]))

for i in range(len(primes)):
    print(primes[i], end=' ')
