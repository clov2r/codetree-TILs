a, b, c=map(int, input().split())
res=(a-11)*60*24+(b-11)*60+c-11
if res<0:
    print(-1)
else:
    print(res)