n, m=map(int, input().split())
cnt=0
n_list=list(map(int, input().split()))
for i in range(len(n_list)):
    if n_list[i]==m:
        cnt+=1
print(cnt)