import sys
sys.stdin=open("input.TXT","rt")
n1=int(input())
list1=list(map(int,input().split()))
n2=int(input())
list2=list(map(int,input().split()))
nlist=[]
i=0
j=0
while i<n1 and j<n2:
    if list1[i]<list2[j]:
        nlist.append(list1[i])
        i+=1
    else:
        nlist.append(list2[j])
        j+=1
if i<n1:
    nlist=nlist+list1[i:]
if j<n2:
    nlist=nlist+list2[j:]
for k in nlist:
    print(k, end=" ")



        


