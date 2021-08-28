
list1=[1,2,3,4]
list2=["emp"]
b=[]
i=0
while i<4:
    j=0
    while j<len(list2):
        b=b+[str(list2[j])+str(list1[i])]
        j=j+1
    i=i+1    
print(b)        

# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']