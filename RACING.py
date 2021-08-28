# n1=input('enter player name:')
# n2=input('enter player name:')
i=0
while i<=2:
    position_of_player1=int(input('enter postion of player1:'))
    position_of_player2=int(input('enter position of player2:'))
    speed_of_player1=int(input('enter speed of player1:'))
    speed_of_player2=int(input('enter speed of player2'))
    # runner1=position_of_player1+speed_of_player1
    # runner2=position_of_player2+speed_of_player2
    while True: 
        runner1=position_of_player1+speed_of_player1
        runner2=position_of_player2+speed_of_player2
        if runner1==runner2:
            print('they will met',runner1)
            break
        else:
            print('they will never met')
            break
    i=i+1 
