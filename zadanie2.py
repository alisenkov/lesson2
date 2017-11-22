
"""
Сравнение строк

Написать функцию, которая принимает на вход две строки.
Если строки одинаковые, возвращает 1.
Если строки разные и первая длиннее, возвращает 2.
Если строки разные и вторая строка 'learn', возвращает 3.
"""



first_str = input('введите первую строку: ')
second_str = input('введите вторую строку: ')

#print(dlina1)
#print(dlinа2)



def compare_srt(first_str, second_str):
    dlina1 = (len(first_str))
    dlinа2 = (len(second_str))
    if str(first_str) == str(second_str):
        return 1
        
    elif first_str != second_str and second_str == "learn":
        return 3
        

    elif str(first_str) != str(second_str) and dlina1 > dlinа2:
        return 2
        
    
    


compare_srt(first_str, second_str)






            
 






