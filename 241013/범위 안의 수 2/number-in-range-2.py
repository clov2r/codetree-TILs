lst=[]
for i in range(10):
    x=int(input())
    if x>=0 and x<=200:
        lst.append(x)
print(sum(lst), round(sum(lst)/len(lst), 1))