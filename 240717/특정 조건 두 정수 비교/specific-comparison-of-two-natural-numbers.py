i=input()
j=i.split()
a=int(j[0])
b=int(j[1])

if a<b:
    print(1,end=' ')
else:
    print(0,end=' ')

if a==b:
    print(1)
else:
    print(0)