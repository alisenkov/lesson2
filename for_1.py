# ###Cоздать список с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# Посчитать и вывести средний балл по всей школе.
# Посчитать и вывести средний балл по каждому классу.
# ###




spisok = [
    {'school_class': '4a',
     'scores' : [4,2,4,2,5]},
    {'school_class': '5a',
     'scores' : [5,4,3,1,3,5]},
]

all_marks_sum = int()
number_of_students_all = int()



for data in spisok:
    scores = sum(data['scores'])    #  сумма всех оценок в классе
    number_of_students = (len(data['scores']))   # количество учеников в классе
    number_of_students_all += len(data['scores']) # количество учеников в школе
    name = (data['school_class'])   # название класса
    summ = int(scores / number_of_students)   # средний балл в классе
    print('Средний балл класса {} равен {} '.format(name, summ ))

    all_marks_sum += sum(data['scores'])   # сумма всех оценок в школе
 



average_ball_of_school = int(all_marks_sum / number_of_students_all)    # средний балл в школе
print ('Средний балл школы равен: {} '.format(average_ball_of_school))