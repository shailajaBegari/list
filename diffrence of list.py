list1=["red", "orange", "green", "blue", "white"]
list2=["black", "yellow", "green", "blue"]
i=0
empty1=[]
empty2=[]
while i<len(list1):
    if list1[i] not in list2:
        empty1.append(list1[i])
    i=i+1
print(empty1)
j=0
while j<len(list2):
    if list2[j] not in list1:
        empty2.append(list2[j])
    j=j+1
print(empty2)


