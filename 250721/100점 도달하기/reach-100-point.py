n=int(input())

for i in range(n,101,1):
    if i<60:
        print('F',end=' ')
    elif 60<=i<70:
        print('D',end=' ')
    elif 70<=i<80:
        print('C',end=' ')
    elif 80<=i<90:
        print('B',end=' ')
    elif 90<=i:
        print('A',end=' ')