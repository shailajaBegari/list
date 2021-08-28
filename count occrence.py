# x=["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"] 
x="shailaja"
i=0
b=[]
c=[]
while i<len(x):
    if x[i] not in c:
        c.append(x[i])
        j=0
        count=0
        l=[]
        l.append(x[i])
        while j<len(x):
            if x[i]==x[j]:
                count=count+1
            j=j+1
        l.append(count)
        b.append(l)
    i=i+1 
# print(b)
i=0
while i<len(b):
    print(b[i][0],"-",b[i][1],"times")
    i=i+1





    