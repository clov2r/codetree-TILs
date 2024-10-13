n=int(input())
tot=0
for i in range(n):
    x=int(input())
    tot+=x
print(tot, round(tot/n, 1))