import re

def normalize_phone(phone_number):
    cleaned_number = re.sub(r'[^0-9+]', '', phone_number) # Видаляємо всі символи, крім цифр та '+'

    if not cleaned_number.startswith('+'): # Перевіряємо, чи номер починається з '+'
        cleaned_number = '+38' + cleaned_number[1:] # Якщо немає міжнародного коду, вважаємо,що номер місцевий та додаємо '+38'
    return cleaned_number

# Приклад використання
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     +490163451234",
    "(050)8889900",
    "38050-111-22-22",
    "+34624467660   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормальні номери телефонів для SMS-розсилки:", sanitized_numbers)
