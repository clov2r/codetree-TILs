a, b, c, d=map(int, input().split())
x=a*60+b
y=c*60+d
if x>y:
    print(x-y)
else:
    print(y-x)