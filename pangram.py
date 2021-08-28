
n=input('enter  string:')
i=0
while i<len(n):
    if "a" in n and "b" in n and "c" in n  and "d" in n and  "e" in n and "f" in n and "g" in n and "h" in n and "i" in n and "j" in n and "k" in n and  "l" in n and  "m" in n and  "n" in n and "o" in n and "p" in n and "q" in n and "r" in n and "s" in n and "t" in n and "u" in n and "v" in n and "w" in n and  "x" in n and"y" in n and "z" in n:
        print('its a pangram')
        break
    else:
        print('its not a pangram')
        break
    i=i+1    


# string=input("enter any string===")
# length=len(string)
# count=0
# count1=0
# i=0
# while i<length:
#     if string[i]>="a" and string[i]<="z":
#         count=count+1
#     else:
#         count1=count1+1
#     i+=1
# print("upper",count1)
# print("lower",count)