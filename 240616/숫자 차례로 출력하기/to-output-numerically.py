n=int(input())

def print_num(n):
    if n==0:
        return
    print_num(n-1)
    print(n,end=' ')

def num_print(n):
    if n==0:
        return

    print(n,end=' ')
    num_print(n-1)

print_num(n)
print()
num_print(n)