arr=input().split()
a=int(arr[0])
b=int(arr[1])
i=a
while a<=i<=b:

    if i%2!=0:
        print(i,end=' ')
        i=2*i
    elif i%2==0:
        print(i,end=' ')
        i+=3
