import random

user_choice = input('do you want odd or even??\n')
if user_choice == 'even':
    user_choice_num = 0
    computer_choice_num = 1
else:
    user_choice_num = 1
    computer_choice_num = 0
print('computer chose:', 'odd' if user_choice == 'even' else 'even')

user_num = int(input('choose a number between 1 and 6:\n'))
computer_num = random.randint(1, 6)
print('computer chose:', computer_num)

toss = user_choice_num + computer_choice_num


def play_cricket(n):
    def play_rule_u(n):
        user_score = 0
        computer_score = 0
        for i in range(1, n + 1):
            user_num = int(input('choose a number between 1 and 6:\n'))
            computer_num = random.randint(1, 6)
            print('computer chose:', computer_num)
            if user_num != computer_num:
                print(f'ball no {i} for user')
                user_score += 1
            else:
                print(f'ball no {i} for computer')
                computer_score += 1
        print(f'computer is now out with a score of {computer_score} and the results announced soon')

        if user_score > computer_score:
            print('user won the game with a score of:', user_score)
            return user_score
        else:
            print('computer won the game with a score of:', computer_score)
            return computer_score

    def play_rule_c(n):
        computer_score = 0
        user_score = 0
        for i in range(1, n + 1):
            user_num = int(input('choose a number between 1 and 6:\n'))
            computer_num = random.randint(1, 6)
            print('computer chose:', computer_num)
            if computer_num != user_num:
                print(f'ball no {i} for computer')
                computer_score += 1
            else:
                print(f'ball no {i} for user')
                user_score += 1
        print(f'user is now out with a score of {user_score} and the results announced soon')

        if user_score > computer_score:
            print('user won the game with a score of:', user_score)
            return user_score
        else:
            print('computer won the game with a score of:', computer_score)
            return computer_score

    if toss % 2 == 0 and user_num % 2 == 0:
        print('user won the toss and computer lost the toss\n')
        user_opt = input('choose bat or ball: ')
        if user_opt == 'bat':
            play_rule_u(n)
        else:
            play_rule_c(n)
    elif toss % 2 == 0 and computer_num % 2 == 0:
        print('computer won the toss and user lost the toss\n')
        computer_opt = random.choice(['bat', 'ball'])
        print('computer chose to', computer_opt)
        if computer_opt == 'bat':
            play_rule_c(n)
        else:
            play_rule_u(n)
    elif toss % 2 != 0 and user_num % 2 != 0:
        print('user won the toss and computer lost the toss\n')
        user_opt = input('choose bat or ball: ')
        if user_opt == 'bat':
            play_rule_u(n)
        else:
            play_rule_c(n)
    elif toss % 2 != 0 and computer_num % 2 != 0:
        print('computer won the toss and user lost the toss\n')
        computer_opt = random.choice(['bat', 'ball'])
        print('computer chose to', computer_opt)
        if computer_opt == 'bat':
            play_rule_c(n)
        else:
            play_rule_u(n)
    else:
        print('It\'s a tie. Play again.')

play_cricket(6)
