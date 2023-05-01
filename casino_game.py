import random
from decouple import config

def play_game():
    initial_money = int(config('MY_MONEY'))

    slots = list(range(1, 31))

    while True:
        print(f"Ваш текущий капитал: {initial_money}$")

        bet = int(input("Введите номер слота (целое число от 1 до 30): "))
        money_bet = int(input("Введите сумму ставки (целое число от 1 до 1000): "))

        if bet not in slots:
            print("Номер слота должен быть целым числом от 1 до 30.")
            continue

        winning_slot = random.choice(slots)

        if bet == winning_slot:
            winnings = money_bet * 2
            print(f"Поздравляем! Вы выиграли {winnings}$.")
            initial_money += winnings
        else:
            print(f"К сожалению, вы проиграли {money_bet}$.")
            initial_money -= money_bet

        if initial_money <= 0:
            print("У вас закончились деньги. Игра окончена.")
            break

        answer = input("Хотите сыграть еще? (да/нет) ")
        if answer.lower() != "да":
            break

    print(f"Игра окончена. Ваш итоговый капитал: {initial_money}$.")