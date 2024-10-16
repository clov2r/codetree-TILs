x=list(map(int, input().split()))
y, z=0,0
for i in range(len(x)):
    if i%2==0:
        y+=x[i]
    else:
        z+=x[i]
if y>z:
    print(y-z)
else:
    print(z-y)