import random

def opponent_make_choice():
    choice=random.randint(0,4)
    return choice
def convert_answer_to_int(answer):
    answer_int=0
    if answer=='ROCK':
        answer_int=1
    elif answer=='PAPER':
        answer_int=2
    elif answer=='SCISSORS':
        answer_int=3
    else:
        print('Invalid answer')
def match(answer_int,opponent):
    


user=input("What do you choose?\n rock,paper,scissors:\n ")
user=user.upper()


