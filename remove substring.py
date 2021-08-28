m="the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
n=m.split()
print(n)
i=0
a=""
while i<len(n):
    if n[i]!="over":
        a=a+n[i]+" "
    i=i+1
print(a)


        

                
        
