list1=[3,4,6,2,0,0,0,0,0,6,7,6,9,10,0,0,0,0,7,4,4,0,0,5,3,2,9,7,1,0,0,0]
# output=[(totalsum)15,38,15,27]
i=0
mainlist=[]
list2=[]
while i<len(list1): 
    if list1[i]==0:
        if len(list2)!=0:
            mainlist.append(list2)
        list2=[]
    else:
        list2.append(list1[i])
    i=i+1
i=0
newlist=[]                
while i<len(mainlist):
    sum=0
    j=0
    while j<len(mainlist[i]):
        sum=sum+int(mainlist[i][j])
        j=j+1
    newlist.append(sum)
    i=i+1
print(newlist)        

