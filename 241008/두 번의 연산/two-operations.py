a=int(input())
if a%2==1:
    a+=3
    if a%3==0:
        print(int(a//3))
    else:
        print(a)
else:
    if a%3==0:
        print(int(a//3))
    else:
        print(a)