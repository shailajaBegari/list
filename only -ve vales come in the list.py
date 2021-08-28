list=[1,2,3,4,-1,-2,-5,-65]
i=0
empty1=[]
empty2=[]
while i<len(list):
    if list[i]<0:
        empty1.append(list[i])
    else:
        empty2.append(list[i])
    i=i+1
print(empty2,empty1)