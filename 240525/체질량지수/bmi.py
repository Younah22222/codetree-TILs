j=input().split()
h=int(j[0])
w=int(j[1])
b=w/(h/100)**2
if b<25:
    print(int(b))
elif b>=25:
    print(int(b))
    print('Obesity')