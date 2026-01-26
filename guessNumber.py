
import random

def gues_number():
    number = random.randint(1, 100)

    attemps = 0
    print("Я загадал число, угадывай")

    while(True):
        try:
            guess = int(input("Твоя догадка: "))

            if number > guess:
                print("Не угадал, число больше")
                attemps += 1
            elif number < guess:
                print("Не угадал, число меньше")
                attemps += 1
            elif number == guess:
                print(f"В точку! Тебе потебовалось {attemps} попыток")
                break
        except ValueError:
            print("Введите число")

gues_number()

