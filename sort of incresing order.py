n=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
i=0
while i<len(n):
    j=0
    while j<len(n)-1:
        if n[j][1]>n[j+1][1]:
            n[j],n[j+1]=n[j+1],n[j]
        j=j+1
    i=i+1
print(n)