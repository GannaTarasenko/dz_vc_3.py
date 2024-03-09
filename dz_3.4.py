from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date().replace(year=today.year)

        if birthday_date < today:
            birthday_date = birthday_date.replace(year=today.year + 1) # День народження вже минув у цьому році, розглядаємо на наступний рік

        days_until_birthday = (birthday_date - today).days # Визначаємо різницю між днем народження та поточним днем

        if 0 <= days_until_birthday <= 7:
            if birthday_date.weekday() >= 5: # Перевірка, чи день народження припадає на вихідний
                birthday_date += timedelta(days=(7 - birthday_date.weekday())) # Якщо припадає на вихідний, переносимо на наступний понеділок

            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': birthday_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

# Приклад використання
users = [
    {"name": "Надія", "birthday": "2016.03.10"},
    {"name": "Свят", "birthday": "2018.03.12"},
    {"name": "Вова", "birthday": "1986.03.03"},
    {"name": "Ганна", "birthday": "1988.03.21"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
