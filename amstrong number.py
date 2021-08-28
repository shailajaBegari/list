n=[23,25,145,153,225]
i=0
while i<len(n):
    a=len(str(n[i]))
    b=n[i]
    sum=0
    while n[i]>0:
        d=n[i]%10
        sum=sum+d**a
        n[i]=n[i]//10
    if sum==b:
        print(b,'amstrong')
    else:
        print(b,'not a amstrong')        
    i=i+1