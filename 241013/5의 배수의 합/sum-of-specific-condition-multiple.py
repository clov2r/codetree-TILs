a, b=map(int, input().split())
tot=0
if a<b:
    for i in range(a, b+1):
        if i%5==0:
            tot+=i
    print(tot)
elif a>b:
    for i in range(b, a+1):
        if i%5==0:
            tot+=i
    print(tot)
else:
    for i in range(a, b+1):
        if i%5==0:
            tot+=i
    print(tot)