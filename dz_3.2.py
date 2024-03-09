import random

def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= max <= 1000) or not (1 <= quantity <= max - min + 1): #перевірка коректності вхідних параметрів
        return []

    unique_numbers = set() #створення порожньої множини
    while len(unique_numbers) < quantity:
        unique_numbers.add(random.randint(min, max)) #генерація випадкових унікальних чисел

    return sorted(list(unique_numbers)) #відсортований список унікальних чисел

# Приклад використання
lottery_numbers = get_numbers_ticket(1, 1000, 9)
print("Ваші лотерейні числа:", lottery_numbers)

