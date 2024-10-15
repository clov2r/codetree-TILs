x=int(input())
m=list(map(int, input().split()))
n=[]
for i in range(len(m)):
    if m[i]%2==0:
        n.append(m[i])
print(*n[::-1])