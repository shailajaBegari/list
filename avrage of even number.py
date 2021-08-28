n= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
sum=0
avg=0
while i<len(n):
    if n[i]%2==0:
        sum=sum+n[i]
    i=i+1
print(sum)   
print(sum/11) 
