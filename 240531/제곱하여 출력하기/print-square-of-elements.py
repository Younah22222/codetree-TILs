n=int(input())
ar=list(map(int,input().split()))
n_ar=[elem*elem for elem in ar]

for i in range(n):
    print(n_ar[i],end=' ')