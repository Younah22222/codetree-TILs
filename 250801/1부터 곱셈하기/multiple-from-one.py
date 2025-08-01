n=int(input())
p=1

for i in range(1,11):
    p*=i
    if p>=n:
        break

print(i)