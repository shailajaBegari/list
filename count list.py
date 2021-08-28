 
n=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
i=0
count=0
while n[i:]:
    if n[i]>=20 and n[i]<=40:
        count=count+1
        print(n[i])
    i=i+1
print('=',count)        