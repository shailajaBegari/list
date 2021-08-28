m=[10, 20, 30, 40, 20, 50, 60, 40,10,30,60,50,30,2,2,4]
i=0
b=[]
while i<len(m):
    if m[i] not in b:
        b.append(m[i])
    i=i+1
print(b)    
