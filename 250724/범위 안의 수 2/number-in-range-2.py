sum=0
avg=0

for _ in range(10):
    i=int(input())
    if 0<=i<=200:
        sum+=i
        avg+=1
print(f'{sum} {sum/avg:.1f}')
    