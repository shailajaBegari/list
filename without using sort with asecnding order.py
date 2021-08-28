n=[3,0,1,-1,-3,2,5]
i=0
while i<len(n):
    j=0
    while j<len(n)-1:
        if n[j]>n[j+1]:
            n[j],n[j+1]=n[j+1],n[j]
        j=j+1
    i=i+1
print(n)





    