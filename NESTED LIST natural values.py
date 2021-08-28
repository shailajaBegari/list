
# i=1
# b=[]
# while i<=30:
#     b1=[]
#     j=i
#     while j<=i+4:
#         b1.append(j)
#         j=j+1
#     b.append(b1)
#     i=i+5   
# print(b)            
            

l=[(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),(7, 8), (9, 10)]
b=[]
i=0
while i<len(l):
    j=0
    while j<len(l[i]):
        if l[i][j] not in b:
            b.append(l[i][j])
        j=j+1
    i=i+1
print(b)    
