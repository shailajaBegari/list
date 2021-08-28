n="chin"
m="inch"
# if len(n)==len(m):
c=0
i=0
while i<len(n):
    if n[i] in m:
        c=c+1
    i=i+1
if len(n)==len(m):
    print('anagram') 
else:
    print('no')               
