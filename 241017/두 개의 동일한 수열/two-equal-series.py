x=int(input())
y=list(map(int, input().split()))
z=list(map(int, input().split()))
a=list(set(y+z))
if len(a)==x:
    print('Yes')
else:
    print('No')