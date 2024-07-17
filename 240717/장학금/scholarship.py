i=input()
j=i.split()
a=int(j[0])
b=int(j[1])

if a>=90 and b>=95:
    print(100000)

elif a>=90 and b>=90:
    print(50000)
else:
    print(0)