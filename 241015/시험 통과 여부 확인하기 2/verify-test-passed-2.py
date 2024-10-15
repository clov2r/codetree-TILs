t=int(input())
cnt=0
for i in range(t):
    score=list(map(int, input().split()))
    x=sum(score)
    y=len(score)
    avg=x/y
    if avg >=60:
        print('pass')
        cnt+=1
    else:
        print('fail')
print(cnt)