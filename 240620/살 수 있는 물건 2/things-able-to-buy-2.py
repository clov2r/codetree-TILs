money=int(input())
if money<500:
    print('no')
elif 500<=money<1000:
    print('pen')
elif 1000<=money<3000:
    print('mask')
else:
    print('book')