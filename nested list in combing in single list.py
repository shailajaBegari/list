n=[[2,4,3],[1,5,6], [9], [7,9,0]]
i=0
b=[]
while i<len(n):
    j=0
    while j<len(n[i]):
        b.append(n[i][j])
        j=j+1
    i=i+1    
print(b)