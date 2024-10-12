x, n=map(str, input().split())
N=int(n)
if x=='A':
    for i in range(N):
        print(i+1, end=' ')
elif x=='D':
    for i in range(N, 0, -1):
        print(i, end=' ')