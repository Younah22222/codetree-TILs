i=input()
j=i.split()
a=int(j[0])
b=int(j[1])
c=int(j[2])


if a<=b and a<=c:
    print(a)
elif b<=a and b<=c:
    print(b)
else:
    print(c)