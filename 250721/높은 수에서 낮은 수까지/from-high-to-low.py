arr=input().split()
a=int(arr[0])
b=int(arr[1])

if a>=b:
    for i in range (a,b-1,-1):
        print(i,end=' ')
elif b>=a:
    for i in range (b,a-1,-1):
        print(i,end=' ')
