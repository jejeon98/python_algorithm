import sys
sys.stdin=open("input.TXT","rt")
card=[0]*20
for i in range(20):
    card[i]=(i+1)
for i in range(10):
    a,b=map(int,input().split())
    for j in range(((b-a)+1)//2):
        card[j+a-1],card[b-j-1]=card[b-j-1],card[j+a-1]
for a in card:
    print(a,end=' ')
