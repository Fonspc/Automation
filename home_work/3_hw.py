def func_max(a = 4, b = 7):
    if a > b :
        print(a)
    else:
        print(b)

func_max()



def func_yesno( a= 50, b = 600):
    if abs(a - b) == 135:
        print('Yes')
    else:
        print('No')

func_yesno()


def month_season(season_of_year):
    if season_of_year == 12 or season_of_year == 1 or season_of_year == 2 :
        print("Зима")
    elif season_of_year == 3 or season_of_year == 4 or season_of_year == 5 :
        print('Весна')
    elif season_of_year == 6 or season_of_year == 7 or season_of_year == 8 :
        print('Лето')
    elif season_of_year == 9 or season_of_year == 10 or season_of_year == 11 :
        print('Осень')
    else:
        print('Введите корректный месяц')

month_season(6)



def check_numbers(a=11 , b=12, c=15):
    if a > 10 and b > 10 and c > 10:
        print('Yes')
    else:
        print('No')

check_numbers()



