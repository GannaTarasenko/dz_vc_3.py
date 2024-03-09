import random

def get_numbers_ticket(minimum, maximum, quantity):
    # Перевірка коректності вхідних параметрів
    if not (1 <= minimum <= maximum <= 1000) or not (1 <= quantity <= maximum - minimum + 1):
        return []

    # Використання множини для забезпечення унікальності чисел
    unique_numbers = set()

    # Генерація випадкових унікальних чисел
    while len(unique_numbers) < quantity:
        unique_numbers.add(random.randint(minimum, maximum))

    # Повернення відсортованого списку унікальних чисел
    return sorted(list(unique_numbers))

# Приклад використання
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

