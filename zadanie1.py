
"""
Возраст

Попросить пользователя ввести возраст.
По возрасту определить, чем он должен заниматься: учиться в детском саду, школе, ВУЗе или работать.
Вывести занятие на экран.
"""




age = int(input("Введите свой возраст: "))
print('Твой возраст - {} лет и '.format(age))
if age < 18:
    print("ты школьник")

elif age > 25:
    print("ты старый")

else:
    print("ты студент")




