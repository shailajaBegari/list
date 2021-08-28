a=[1,2,3]
b=['a','b','c']
i=0
while i<len(a):
    print(a[i],end="")
    # i=i+1
    j=0
    while j<len(b):
        print(b[j],end="")
        j=j+1
    i=i+1

# c=""
# print(c)
# while i<len(a):
#     c=c+str(a[i])
#     i=i+1
# j=0
# while j<len(b):
#     c+=b[j]
#     j=j+1    
# print("["+c+"]")