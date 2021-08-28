n=int(input('enter number:'))
i=1
a=[]
while i<=n:
    a.append(i**2)
    i=i+1
print(a[0:5]+a[n-5:])
