h, w=map(int, input().split())
n=h/100
b=w/n**2
print('%d'%b)
if b>=25:
    print('Obesity')