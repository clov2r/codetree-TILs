n=int(input())
x=list(map(float, input().split()))
res=round(sum(x)/len(x), 1)
print(res)
if 3.9>res>=4.0:
    print('Perfect')
elif res>=3.0:
    print('Good')
elif res<3.0:
    print('Poor')