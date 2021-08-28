list=[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
# Insert 20 in said list after every 4 th element:
# [1, 3, 5, 7, 20, 9, 11, 0, 2, 20, 4, 6, 8, 10, 20, 8, 9, 0, 4, 20, 3, 0]######

list1=[2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3
i=0
count=0
count1=0
b=[]
c=[]
while i<len(list1):
    if list1[i]>0:
        count=count+1
        b.append(list1[i])
    else:
        c.append(list1[i])
        count1+=1
    i=i+1
print(c,count1)
print(b,count)