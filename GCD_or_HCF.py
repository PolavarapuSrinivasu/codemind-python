a,b=map(int,input().split())
if a==b:
    print(a)
elif a%b==0:
    print(b)
elif b%a==0:
    print(a)
else:
    for i in range(1,a):
        if a%i==0 and b%i==0:
            m=i
    print(m)