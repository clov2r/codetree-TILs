a, b=map(int, input().split())
if a%2==0:
    for i in range(a, b+1, 2):
        print(i+1, end='')
else:
    for i in range(a, b+1, 2):
        print(i, end=' ')