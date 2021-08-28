n = ['a','b','c','d','e','f']
m = ['d','e','f','g','h']
i=0
b=[]
while i<len(n):
    if n[i] not in  m:
        b.append(n[i])
    i=i+1                
print(b)
j=0
c=[]
while j<len(m):
    if m[j] not in n:
        c.append(m[j])
    j=j+1
print(c)        
