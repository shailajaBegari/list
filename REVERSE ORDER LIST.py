n=[0,1,2,3,4,5]
# output=[1,0,3,2,5,4]
i=0
b=[]
while i<len(n):
    j=0
    while j<len(n)-1:
        if n[j]>n[j+1]:
            n[j]=n[j+1]
        j=j+1
    i=i+1
print(n)               