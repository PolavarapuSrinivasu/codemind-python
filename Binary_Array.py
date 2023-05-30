n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    if i==0 or i==1:
        s+=1
    else:
        continue
if s==n:
    print(True)
else:
    print(False)