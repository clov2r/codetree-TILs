n=int(input())
i=1
while i<n:
    res=i*3
    if res>n:
        break
    print(res, end=' ')
    i+=1