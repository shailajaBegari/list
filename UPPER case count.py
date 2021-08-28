
string=input("enter any string===")
# length=len(string)
count=0
count1=0
i=0
while i<len(string):
    if string[i]>="a" and string[i]<="z":
        count=count+1
    else:
        count1=count1+1
    i+=1
print("upper",count1)
print("lower",count)