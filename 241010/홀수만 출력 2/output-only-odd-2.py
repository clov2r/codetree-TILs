b, a=map(int, input().split())
if b%2==0:
    for i in range(b, a-1, -1):
        if i%2==1:
            print(i, end=' ')
else:
    for i in range(b, a-1, -1):
        if i%2==1:
            print(i, end=' ')