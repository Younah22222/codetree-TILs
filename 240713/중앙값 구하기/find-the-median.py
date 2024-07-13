i=input()
j=i.split()

a=int(j[0])
b=int(j[1])
c=int(j[2])

if a>c:
    a,c=c,a
if a>b:
        a,b=b,a
print(b)