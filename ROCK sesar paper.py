player1=input('enter the player1:')
player2=input('enter the player2:')
if player1==player2:
    print("game tie")
elif player1=="rock" and player2=="paper":
    print('winner  of game is paper')
elif player1=="rock" and player2=="sesar":
    print('winner of game is  rock')
elif player1=="paper" and player2=="sesar":
    print("winner of game is  sesar ")
elif player1=="paper" and player2=="rock":
    print('winner of game is  paper')
elif player1=="sesar" and player2=="rock":
    print('winner of game is  rock')
elif player1=="sesar" and player2=="paper":
    print('winner of game is sesar ')                 
