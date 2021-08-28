list1=[4,6,8,[],7,[],8,[]]
# print("actual list"+str(list1))
# res=list(filter(None,list1))
# print(res)
i=0
b=[]
while i<len(list1):
    if list1[i]!=[]:
        b.append(list1[i])
    i=i+1
print(b) 

