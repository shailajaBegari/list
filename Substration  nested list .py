n=[[7,2,3,4,5,6,8],[1,2,3,4,5,6,4]]
i=0
j=1
b=[]
while i<=0:
    k=0                                   
    b.append(n[i][k]-n[j][k])
    k=k+1
    i=i+1
print(b)

i=0
j=1
k=0
b=[]       
while k<len(n[i]):                                     
    b.append(n[i][k]-n[j][k])
    k=k+1
print(b)    
