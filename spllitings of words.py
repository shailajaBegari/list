# n='my name is shailaja and my sis name rani'
# y=n.split()
# print(y)


n='my name is shailaja and my sis name rani'
# i=0
# c=n.split()
# while i<len(n[i]):
#     i=i+1   
# print(c)


##################################
n='my name is shailaja and my sis name rani'
i=0
b=[]
s=""
while i<len(n):
    if n[i]==" ":
        b.append(s)
        s=""
    else:
        s=s+n[i]
    i=i+1
b.append(s)
print(b)




