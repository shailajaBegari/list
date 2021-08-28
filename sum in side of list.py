
list=[12,14,16]
i=0
newlist=[]
while i<len(list):
    j=list[i]
    sum=0
    while j>0:
        r=j%10
        sum=sum+r
        j=j//10
    newlist.append(sum)
    i=i+1
print(newlist)
