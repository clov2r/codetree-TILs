n, m=map(int, input().split())
n_list=list(map(int, input().split()))
n_list2=sorted(n_list)
print(sum(n_list2[m-1:]))