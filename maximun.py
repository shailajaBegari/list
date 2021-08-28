x=[1,2,3,4,8,9,54]
i=0
max=0
while x[i:]:
    if x[i]>max:
        max=x[i]
        x[i]=max
    i+=1
print(max)
        