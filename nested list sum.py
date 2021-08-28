 
# m= [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65, 76],
#     [95, 45, 78, 52, 49]
# ] 
# i=0
# sum=0
# while i<len(m):
#     j=0
#     while j<len(m[i]):
#         sum=sum+m[i][j]
#         j=j+1    
#     i=i+1
# print(sum)        


m=[[78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78]] 
i=0
sum=0
while i<len(m):
    j=0
    while j<len(m[i]):
        sum=sum+m[i][j]
        j=j+1
    i=i+1
print(sum)        