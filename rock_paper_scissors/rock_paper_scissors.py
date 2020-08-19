import random

def opponent_make_choice():
    choice=random.randint(1,3)
    return choice
def convert_answer_to_int(answer):
    answer_int=0
    if answer=='ROCK':
        answer_int=1
        return answer_int
    elif answer=='PAPER':
        answer_int=2
        return answer_int
    elif answer=='SCISSORS':
        answer_int=3
        return answer_int
    else:
        print('Invalid answer')
def convert_int_to_answer(answer_int):
    answer=''
    if answer_int==1:
        answer='ROCK'
    elif answer_int==2:
        answer='PAPER'
    elif answer_int==3:
        answer='SCISSORS'
    return answer

def determine_victor(choice_1,choice_2):
    if choice_1==choice_2:
        return'tie'
    match=[choice_1,choice_2]
    if (1 in match) and (2 in match):
        return 'PAPER'
    elif (2 in match) and(3 in match):
        return 'SCISSORS'
    elif (3 in match) and (1 in match):
        return 'ROCK'
    else:
        print(match)



user=input("What do you choose?\n rock,paper,scissors:\n ")
user=user.upper()
user_int=convert_answer_to_int(user)
opponent=opponent_make_choice()

winner=determine_victor(user_int,opponent)
print(winner)

print('Player:{} \n vs \n Opponent:{}'.format(user,convert_int_to_answer(opponent)))

if winner=='tie':
    print('tie')
if user==winner:
    print("You won!")
else:
    print('You lost')

