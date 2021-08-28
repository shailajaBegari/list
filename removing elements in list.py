n=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
i=0
b=[]
while i<len(n):
    if n[i]!=n[0] and n[i]!=n[4] and n[i]!=n[5]:
        b.append(n[i])
    i=i+1
print(b)        



# n=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# n.remove('Red')
# n.remove('Pink')
# n.remove('Yellow')
# print(n)