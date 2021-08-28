list=[4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
i=0
b=[]
while i<len(list):
    if list[i] not in b:
        b.append(list[i])
    i=i+1
print(b)




# Output: [4, 3]


