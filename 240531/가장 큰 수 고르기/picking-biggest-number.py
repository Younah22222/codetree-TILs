j=input().split()
list=[]
for i in range(10):
    list.append(int(j[i]))
max=0
for elem in list:
    if elem>max:
        max=elem
    
print(max)