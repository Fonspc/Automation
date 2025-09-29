# num = 3
#
# if num >=0:
#     print(" Число больше или равно 0")
# else:
#     print("Число отрицательное")
#
#
# def task_yes_no(str_1, str_2):
#     if str_1 in str_2:
#         print('ДА')
#     else:
#         print('НЕТ')
#
# task_yes_no(str_1='test', str_2='test1')


# num_float = -4.5
#
# if num_float > 0:
#     print("Число положительное")
# elif num_float == 0:
#     print("Ноль")
# else:
#     print("Число отрицательное")
#
# permint_print = True
# if num > 0 and permint_print:
#     print('num - Положительное число')
# elif not permint_print:
#     print("Печать запрещена")


def student_rank(year_of_sudy):
    if year_of_sudy == 1 or year_of_sudy == 2 or year_of_sudy == 3 or year_of_sudy == 4:
        print('Вы бакалавр')
    elif year_of_sudy in range (5,7):
        print('Вы магистр')
    elif 7 <= year_of_sudy <= 9:
        print('Вы аспирант')
    else:
        print('Введите корректный год обучения')

student_rank(5)