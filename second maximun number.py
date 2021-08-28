n = [50, 40, 23, 70, 56, 12, 5, 10, 7] 
i=0
max=0
s_m=1
while i<len(n):
    if  n[i]>max:
        max=n[i]
        n[i]=max
    elif n[i]> s_m:
        s_m=n[i]
    i=i+1
print(max)
print(s_m)   




# n = [50, 40, 23, 70, 56, 12, 5, 10, 7] 
# print(max(n))