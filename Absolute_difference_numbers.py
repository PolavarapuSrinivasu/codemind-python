n,d=map(int,input().split())
c=0
t=n
while(n!=0):
    r=n%10
    c+=1
    n=n//10
f=c-d
fs=pow(10,f)
ls=pow(10,d)
r=t%ls
q=t//fs
if r>q:
    print(r-q)
else:
    print(q-r)