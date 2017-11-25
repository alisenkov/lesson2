#При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!”


import random
answers = ["хорошо", "пойдет", "сам такой"]

def ask_user():
    while True:
        answer = input("спроси что-нибудь:\n")
        if answer == "Пока":
            print("И тебе")
            break
        elif len(answer) > 0:
            get_answer()
        
   

def get_answer():
        print(random.choice(answers))
        


ask_user()