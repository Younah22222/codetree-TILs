i=input()
j=i.split()

a=int(j[0])
b=int(j[1])
c=int(j[2])

if a<b and a<c:
    print(1,end=' ')
else:
    print(0,end=' ')

if a==b==c:
    print(1)
else:
    print(0)