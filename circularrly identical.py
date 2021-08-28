

l=[10, 10, 0, 0, 10]
m=[10, 10, 10, 0, 0]
n=[1, 10, 10, 0, 0]
i=0
b=[]
c=[]
while i<len(l):
    if l[i] in m:
        b.append(l[i])
    if l[i] in n:
        c.append(l[i])
    i=i+1
if len(b)==len(l):
    print("true")
if len(c)==len(l):
    print('false')



    

