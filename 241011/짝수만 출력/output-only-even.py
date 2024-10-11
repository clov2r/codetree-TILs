a, b=map(int, input().split())
if a%2==0:
    while a<=b:
        if a>b:
            break
        print(a, end=' ')
        a+=2
else:
    while a<=b:
        if a>b:
            break
        a+=1
        print(a, end=' ')