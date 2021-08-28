n=['abc', 'xyz', 'aba', '1221']
i=0
c=0
while i<len(n):
    if n[i][0]==n[i][-1]:
        c=c+1
    i=i+1
print(c)