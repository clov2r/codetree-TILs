x=list(map(int, input().split()))
tot, cnt=0,0

for i in range(len(x)):
    if x[i]==0:
        break
    else:
        if x[i]%2==0:
            tot+=x[i]
            cnt+=1
print(cnt, tot)