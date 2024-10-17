n, k, t=map(str, input().split())
n=int(n)
k = int(k)
dct=[]
for i in range(n):
    x=input()
    if x.startswith(t):
        dct.append(x)
dct2=sorted(dct)
print(dct2[k-1])