a, b=map(int, input().split())
while (a>=b):
    if a%2==0:
        if a<b:
            break;
        print(a, end=' ')
        a-=2
    else:
        if a<b:
            break;
        print(a, end=' ')
        a-=3