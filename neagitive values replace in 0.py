list1=[-1,2,7,-1,5,-1]
i=0
b=[]
while i<len(list1):
    if list1[i]<0:
        b.append(0)
    else:
        b.append(list1[i])
    i=i+1
print(b)