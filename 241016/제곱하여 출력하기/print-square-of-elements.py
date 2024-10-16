n=int(input())
n_list=list(map(int, input().split()))
for i in range(len(n_list)):
    n_list[i]=n_list[i]**2
print(*n_list)