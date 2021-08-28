import random
n=[1,3,4,5,6,7,2,9]
b=[]
i=0
while True:
    m=random.choice(n)
    if i==len(n):
        # print(b)
        break
    if m not in b:
        b.append(m)
        i=i+1
print(b)        



