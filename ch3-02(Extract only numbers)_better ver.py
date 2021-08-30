import sys
sys.stdin=open("input.TXT","rt")
n=list(input())
res=0
cnt=0
for i in n:
    if i.isdecimal():
        res=res*10+int(i)
print(res)
for i in range(1,res+1):
    if res%i==0:
        cnt+=1
print(cnt)
    


        


