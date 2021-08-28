list1=[2,8,-6,-1,7,-8]
i=0
b=[]
while i<len(list1):
    if list1[i]<0:
        b=b+[0]
    else:
        b=b+[list1[i]]    
    i=i+1
print(b)  
      
        