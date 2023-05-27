n=int(input())
c=64+n
for i in range(n,0,-1):
    for j in range(0,i):
        print(chr(c),end=" ")
    c=c-1
    print()