n="my name is shailaja"
b=[]
i=0
m=input('enter a element:')
while i<len(n):
    element=""
    while  True:
        if n[i] == m:
            b.append(element)
            b=b+[n[i]]
            i=i+1
            break
        else:
            element=element+n[i]
            i=i+1
        if i==len(n):
            b.append(element)
            break
print(b)




