k=int(input())
def sum(k):
    count=0
    for i in range(k+1):
        count+=i
    return count//10

print(sum(k))