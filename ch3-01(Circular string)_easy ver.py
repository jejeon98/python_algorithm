import sys
sys.stdin=open("input.txt","rt")
n=int(input())
for i in range(n):
    s=input()
    s=s.upper()
    if s==s[::-1]:
        print("#",i+1, "YES")
    else:
        print("#",i+1, "NO")

