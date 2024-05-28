j=input().split()
a=int(j[0])
b=int(j[1])
prod=1
for i in range(a,b+1):
    prod*=i

print(prod)