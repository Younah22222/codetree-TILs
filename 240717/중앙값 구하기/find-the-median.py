i=input()
j=i.split()

a=int(j[0])
b=int(j[1])
c=int(j[2])

if a>b:
    a,b=b,a
    if b>c:
      b,c=c,b
else:
    pass

print(b)