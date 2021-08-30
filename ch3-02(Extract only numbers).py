import sys
sys.stdin=open("input.TXT","rt")
n=list(input())
num=[]
res=0
cnt=0
for i in range(len(n)):
    if '0'<=n[i]<='9':
        num.append(n[i])
if num[0]=='0':
    del(num[0])
for i in range(len(num)):
    num[i]=int(num[i])
    res=res*10+num[i]
print(res)
for i in range(1,res+1):
    if res%i==0:
        cnt+=1
print(cnt)
    


        


