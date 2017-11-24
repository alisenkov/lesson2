#При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!”


import random
answers = ["хорошо", "пойдет", "сам такой"]

def ask_user():
    answer = input("спроси что-нибудь:\n")
    if answer == "Пока":
        print("И тебе")
    elif len(answer) > 0:
        get_answer()
        ask_user()
        
   

def get_answer():
    for x in ["answers"]:
        print(random.choice(answers))
        


ask_user()