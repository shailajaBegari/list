# output=[2,3,5,6,7,7,8,8,9]
list1=[[6,8,7],[3,5,7],[8,9,2]]
i=0
b=[]
while i<len(list1):                     
    j=0
    while j<len(list1[i]):
        b.append(list1[i][j])
        j=j+1  
    i=i+1
k=0
while k<len(b)-1:
    l=0
    while l<len(b):                      
        if b[l]>b[k+1]:
            # b[l],b[k+1]=b[k+1],b[l]        (asending order)
        l=l+1
    k=k+1
print(b)                   
k=0
while k<len(b):
    l=0
    while l<len(b):
        if b[k]<b[l]:
            b[k],b[l]=b[l],b[k]
        l=l+1    
    k=k+1          
print(b)    