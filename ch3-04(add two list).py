import sys
sys.stdin=open("input.TXT","rt")
n1=int(input())
list1=list(map(int,input().split()))
n2=int(input())
list2=list(map(int,input().split()))
for i in list2:
    list1.append(i)
list1=sorted(list1)
for i in list1:
    print(i, end=" ")







        


