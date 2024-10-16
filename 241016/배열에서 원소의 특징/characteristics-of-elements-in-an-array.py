x=list(map(int, input().split()))
y=0
for i in range(len(x)):
    if x[i]%3==0:
        y=i
        print(x[y-1])
        break;