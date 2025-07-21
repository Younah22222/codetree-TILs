arr=input().split()
a=int(arr[0])
b=int(arr[1])

c=a//b
print(f'{c}.',end='')
for _ in range(20):
    a=a%b
    a=a*10
    d=a//b
    if d==0:
        print(0,end='')
    elif d!=0:
        print(d,end='')
    
