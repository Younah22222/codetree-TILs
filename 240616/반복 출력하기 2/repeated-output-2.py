n=int(input())

def print_string(n):
    if n==0:
        return

    print_string(n-1)
    print('HelloWorld')

print_string(n)