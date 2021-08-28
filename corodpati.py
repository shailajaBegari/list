 
x=[3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100] 
i=0
c=0
d=0
l=0
while i<len(x):
    if x[i]<100000:
        d=d+1
    elif x[i]>100000 and x[i]<10000000:
        l=l+1
    elif x[i]>10000000:
        c=c+1   
    i=i+1  
print(d,"dilwale")
print(l,"lacpati")
print(c,"carodpati")
