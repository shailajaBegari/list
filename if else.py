i=0
sum=0
while i<100:
    sum=sum+i
    print(i)
    i=i+1
print(sum)

name=input('enter name:')
if  len(name)>3 and  "ing" in name:
    print(name+"ly")
else:
    print(name+"ing")
