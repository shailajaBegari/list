
x = [1,2,3,4,5,6]
y = [2,3,1,0,6,7] 
z=[]
i=0
while i<len(x):
    if x[i] not in y:
        z.append(x[i])
    i=i+1
print(z)

