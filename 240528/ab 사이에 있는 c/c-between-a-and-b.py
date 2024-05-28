j=input().split()
a=int(j[0])
b=int(j[1])
c=int(j[2])
cnt=0
for i in range(a,b+1):
    if i%c==0:
        cnt+=1

    else:
        pass

if cnt==0:
    print('NO')
else:
    print('YES')