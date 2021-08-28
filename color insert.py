
n=['Red', 'Green', 'Black']                                                                     
# Original List:  ['c', 'Red', 'c', 'Green', 'c', 'Black'] 
i=0
j=0
b=[]
while i<6:
    # if i==0 or i==2 or i==4:
    if i%2==0:
        b.append("c")
    else:
        b.append(n[j])
        j=j+1
    i=i+1
print(b)   
 



# n.insert(0,"c" and 2,"c" and 4,"c")
# n.insert(2,"c")
# n.insert(4,"c") 
# print(n)    