n=list(map(int, input().split()))
x=[]
for i in range(len(n)):
    if n[i]>=250:
        break
    else:
        x.append(n[i])
print(sum(x), round(sum(x)/len(x), 1))