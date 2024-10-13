n=int(input())
tot=0
n_list=[]
for i in range(n):
    x=int(input())
    n_list.append(x)
for i in range(len(n_list)):
    if n_list[i] %2==1 and n_list[i]%3==0:
        tot+=n_list[i]
print(tot)