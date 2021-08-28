n=1
n1=10
b=[]
while n<=n1:
    i=1
    f=0
    while i<=n:
        if n%i==0:
            f=f+1
        i=i+1
    if f==2:
        b.append(n)
    n=n+1 
print(b)    

