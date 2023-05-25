n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
for i in range(0,n):
    if l[i]<a or l[i]>b:
        print(l[i],end=" ")
        s+=1
    else:
        continue
if s==0:
    print(-1)