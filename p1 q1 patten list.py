# x = [10, 20, 30]
# y = [40, 50, 60]
# x[:0]=y
# print(x)


n=['p','q']
i=1
b=[]
m=int(input('enter number:'))
while i<=m:
    j=0
    while j<len(n):
        b=b+[n[j]+str(i)]
        j=j+1
    i=i+1 
print(b)
      


