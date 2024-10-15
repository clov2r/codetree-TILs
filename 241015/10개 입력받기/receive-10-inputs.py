x=list(map(int, input().split()))
tot=0
length=0
for i in range(len(x)):
    if x[i]==0:
        break
    else:
        tot+=x[i]
        length+=1
print(tot, round(tot/length, 1))