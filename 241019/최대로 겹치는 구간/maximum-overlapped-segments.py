n=int(input())
x_list=[0]*100
for i in range(n):
    x, y=map(int, input().split())
    for j in range(x-1, y):
        x_list[j]+=1
print(max(x_list))