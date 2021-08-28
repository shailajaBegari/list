position_of_home=1
position_of_apple_tree=5
position_of_orange_tree=-3
orange_fell_down=4
apple_fell_down=5
i=1
c=0
while i<=orange_fell_down:
    direction=int(input('enter direction:'))
    p=direction+position_of_orange_tree
    if p==position_of_home:
        c=c+1
    i=i+1
print("how many orange fell down in the home:",c)
i=1
c=0
while i<=apple_fell_down:
    direction=int(input('enter direction:'))
    p=direction+position_of_apple_tree
    if p==position_of_home:
        c=c+1
    i=i+1
print("how many oapple fell down in the home:",c)

