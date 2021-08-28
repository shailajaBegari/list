n=[['Red'], ['Green'], ['Black']]
i=0
while i<3:
    print(n[i])
    i=i+1



#  Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
# Click me to see the sample solution
n=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
b=[]
i=0
while i<3:
    j=i
    c=[]
    while j<len(n):
        c.append(n[j])
        j=j+3
    b.append(c)
    i=i+1
print(b)        

  
