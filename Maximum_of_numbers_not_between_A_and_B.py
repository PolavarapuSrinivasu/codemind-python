n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
m=0
for i in range(0,n):
    if (l[i]<a or l[i]>b):
        if l[i]>m:
            m=l[i]
    else:
        continue
if m==0:
    print(-1)
else:
    print(m)