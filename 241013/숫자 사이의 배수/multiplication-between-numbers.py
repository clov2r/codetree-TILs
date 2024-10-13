a, b=map(int, input().split())
tot=0
lst=[]
for i in range(a, b+1):
    if i%5==0 or i%7==0:
        tot+=i
        lst.append(tot)
avg=round(tot/len(lst), 1)
print(tot, avg)