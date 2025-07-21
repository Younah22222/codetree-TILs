cnta=0
cntb=0

for i in range(10):
    i=int(input())
    if i%3==0:
        cnta+=1
        if i%5==0:
            cntb+=1
    elif i%5==0:
        cntb+=1
    
print(f'{cnta} {cntb}')
    