L=float(input())
R=float(input())

if (L>=1.0) and (R>=1.0):
    print('High')
elif (1.0>L>=0.5) and (1.0>R>=0.5):
    print("Middle")
else:
    print('Low')