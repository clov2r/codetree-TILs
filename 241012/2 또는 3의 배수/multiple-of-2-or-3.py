x=int(input())
for i in range(x):
    if (i+1)%2==0 or (i+1)%3==0:
        print(1, end=' ')
    else:
        print(0, end=' ')