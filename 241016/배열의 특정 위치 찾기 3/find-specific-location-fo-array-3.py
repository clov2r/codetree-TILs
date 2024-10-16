x=list(map(int, input().split()))
y=[]
for i in range(len(x)):
    if x[i]==0:
        break
    else:
        y.append(x[i])
print(y[-1]+y[-2]+y[-3])