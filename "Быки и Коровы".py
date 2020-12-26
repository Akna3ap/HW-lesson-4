import random

print("Коровы и быки")
print('''Правила игры:
1.Компьютер задумывает четыре различные цифры от 0 до 9. Игрок делает ходы, чтобы угадать эти цифры и их порядок.
2.Каждый ход состоит из четырёх цифр 
3.«Быки» — правильные цифры на правильных местах.  
4.«Коровы» — правильные цифры на неправильных местах.
''')

def num_generator():
    com_num = random.sample("0123456789", 4)
    com_num = "".join(com_num)
    return com_num

def player_input():
    while True:
        try:
            global player_num
            k = player_num = input("Введите свои числа:")
            int(k)

            if len(player_num) != 4:
                print("Введите 4-х значное число")
                continue
        except ValueError:
            print("Вы ввели букву, введите число")
        else:
            x = 0
            for i in range(0, 4):
                x = x+player_num.count(player_num[i])
            if x != 4:
                print("Введите числа с разными цифрами")
                continue
            else:
                return

def num_comparison(a, b):
    a = str(a)
    b = str(b)
    for i in range(0, 4):
        for j in range(0, 4):
            if(i == j) and (a[i] == b[j]):
                global bull_count
                bull_count += 1
            elif(i != j) and (a[i] == b[j]):
                global cow_count
                cow_count += 1
            else:
                pass
player_num = 0
user_choice = True
while user_choice:
    cow_count = 0
    bull_count = 0
    game_num = num_generator()

    score_counter = 0
    while True:
        player_input()
        score_counter = score_counter+1
        num_comparison(game_num, player_num)
        if bull_count == 4:
            print("Вы победили")
            print("Вы завершили игру, использовав ", str(score_counter), "попыток")
            print("Хотите еще раз сыграть?")
            print("Введите \"y\" чтобы поиграть заново")
            print("Для отмены введите любую другую букву")
            choice = input("Выберите: ")
            if choice == "y":
                user_choice = True
            else:
                user_choice = False
            break
        else:
            print("количество быков", bull_count)
            print("количество коров", cow_count)

            cow_count = 0
            bull_count = 0
