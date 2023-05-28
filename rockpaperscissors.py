rounds = int(input('enter the number of rounds'))
 #rock>scissor
 #paper>rock
 #scissor>paper
p1_score = 0
p2_score = 0
count = 0
while(count <= rounds):
    p1_inp = input('player1 : rock or paper or scissor?\n')
    p2_inp = input('player2 : rock or paper or scissor?\n')

    if((p1_inp == 'rock') and (p2_inp == 'scissor')):
        print('p1 wins')
        p1_score = p1_score + 1
    elif((p1_inp == 'paper') and (p2_inp == 'rock')):
        print('p1 wins')
        p1_score = p1_score + 1
    elif((p1_inp == 'scissor') and (p2_inp == 'paper')):
        print('p1 wins')
        p1_score = p1_score + 1
    else:
        print('p2 wins')
        p2_score = p2_score + 1
    count+=1
if(p1_score>p2_score):
    print(f'yay!! player 1 wins finally with a score of {p1_score} and player 2 has a score of {p2_score}')
else:
    print(f'yay!! player 2 wins finally with a score of {p2_score} and player 1 has a score of {p1_score}')