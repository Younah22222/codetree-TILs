a=int(input())
b=input()
j=b.split()

for i in range(4):
    if a>int(j[i]):
       print(1)
    else:
       print(0)