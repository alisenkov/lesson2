#Написать функцию ask_user() чтобы с помощью input() спрашивать пользователя “Как дела?”, пока он не ответит “Хорошо”



def ask_user():
    answer = input("Как дела?\n")
    if answer == "Хорошо":
        pass
    else:
        ask_user()


ask_user()