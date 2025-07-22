cntc=0
cntl=0
cntb=0
n=int(input())

for i in range(1,n+1):
    if i%2==0:
        cntc+=1
        if i%3==0:
            cntc-=1
            cntl+=1
            if i%12==0:
                cntl-=1
                cntb+=1
            else:
                pass
    elif i%3==0:
        cntl+=1

print(f'{cntc} {cntl} {cntb}')