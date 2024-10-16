n=int(input())
n_list=list(map(int, input().split()))
for i in range(len(n_list)):
    if n_list[i]%2==0:
        print(n_list[i], end=' ')