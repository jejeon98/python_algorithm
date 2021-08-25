import sys
sys.stdin=open("input.txt","rt")
n=int(input())
money=[]
for i in range(n):
    tmp=input().split()
    tmp.sort()
    a,b,c=map(int,tmp)
    if a==b and a==c:
        money.append(10000+a*1000)
    elif (a==b and a!=c) or (a==c and b!=c):
        money.append(1000+a*100)
    elif (b==c and b!=a):
        money.append(1000+b*100)
    else:
        if(a>b and a>c):
            money.append(a*100)
        elif(b>a and b>c):
            money.append(b*100)
        else:
            money.append(c*100)
print(max(money))