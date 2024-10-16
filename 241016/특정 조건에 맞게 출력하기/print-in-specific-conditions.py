n=list(map(int, input().split()))
for i in range(len(n)):
    if n[i]==0:
        break
    else:
        if n[i]%2==0:
            n[i]=n[i]//2
            print(n[i], end=' ')
        else:
            n[i]=n[i]+3
            print(n[i], end=' ')