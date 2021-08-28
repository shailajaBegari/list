# number=30
# n = [10, 11, 12, 13, 14, 17, 18, 19] 
# i=0
# while i<len(n):
#     j=0
#     while j<i:
#         if n[i]+n[j]==30:
#              print([n[i],n[j]],end=" ")
#         j=j+1
#     i=i+1

n = [10, 11, 12, 13, 14, 17, 18, 19] 
i=0
b=[]
while i<len(n):
    c=[]
    j=0
    while j<i:
        if n[i]+n[j]==30:
            c.append(n[i])
            c.append(n[j])
            b.append(c)
        j=j+1
    i=i+1
print(b)            




