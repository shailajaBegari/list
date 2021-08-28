m="the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
n=m.split()
i=0
a=""
while i<len(n):
    if n[i]=="over":
        a=a+"on"+" "
    else:
        a=a+n[i]+" "
    i=i+1
print(a)


        

                
        
