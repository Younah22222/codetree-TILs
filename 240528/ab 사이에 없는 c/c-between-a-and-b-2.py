j=input().split()
a,b,c=int(j[0]),int(j[1]),int(j[2])
cnt=0
for i in range(a,b+1):
    if i%c==0:
        pass
    else:
        cnt+=1
if cnt==0:
    print('NO')
else:
    print('YES')