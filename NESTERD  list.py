list1=[0,0,1,2,3,4,4,5,6,6,6,7,8,9,4,4]
# output=[[0,0],[1],[2],[3],[4,4],[5],[6,6,6],[7],[8],[9],[4,4]]
i=0
empty=[] 
while i<len(list1):
    j=0
    empty2=[]
    while j<len(list1):
        if list1[i]==list1[j]:
            empty2.append(list1[i])
        j=j+1
    if empty2 not  in empty:
        empty.append(empty2)
    i+=1
print(empty)    


