'''
4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
Программа должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного числа используйте код:

from random import
randint num = randint(LOWER_LIMIT, UPPER_LIMIT)
'''


from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAX_ATTEMPTS = 10

# Генерируем случайное число, которое нужно угадать
secret_number = randint(LOWER_LIMIT, UPPER_LIMIT)

print("Добро пожаловать в игру 'Угадай число'!")
print(f"Я загадал число от {LOWER_LIMIT} до {UPPER_LIMIT}. У вас есть {MAX_ATTEMPTS} попыток.")

for attempt in range(1, MAX_ATTEMPTS + 1):
    try:
        guess = int(input(f"Попытка {attempt}: Ваше предположение: "))
    except ValueError:
        print("Пожалуйста, введите корректное целое число.")
        continue

    if guess == secret_number:
        print(f"Поздравляю! Вы угадали число {secret_number} за {attempt} попыток.")
        break
    elif guess < secret_number:
        print("Число больше.")
    else:
        print("Число меньше.")
else:
    print(f"Вы проиграли! Загаданное число было {secret_number}.")
