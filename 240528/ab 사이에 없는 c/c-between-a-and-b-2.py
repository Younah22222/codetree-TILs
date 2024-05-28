j=input().split()
a,b,c=int(j[0]),int(j[1]),int(j[2])

for i in range(a,b+1):
    cnt=0
    if i%c==0:
        break
    elif i%c!=0:
        cnt+=1
if cnt==0:
    print('NO')
elif cnt!=0:
    print('YES')