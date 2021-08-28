n=[2,3,4,5,11]
m=[1,9,8,7,9,8]
# output:[1,2,3,4,5,7,8,9,11]
i=0
b=[]
while i<len(n):
    if n[i] not in b:
        b.append(n[i])
    if m[i] not in b:
        b.append(m[i])
    j=0
    while j<len(b)-1:
        if b[j]>b[j+1]:
            b[j],b[j+1]=b[j+1],b[j]
        j=j+1     
    i=i+1
print(b)