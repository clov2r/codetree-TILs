N=int(input())
n=list(map(int, input().split()))
cnt=0
for i in range(len(n)):
    if n[i]==min(n):
        cnt+=1
print(min(n), cnt)