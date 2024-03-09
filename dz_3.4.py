from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date().replace(year=today.year)

        if birthday_date < today:
            # День народження вже минув у цьому році, розглядаємо на наступний рік
            birthday_date = birthday_date.replace(year=today.year + 1)

        # Визначаємо різницю між днем народження та поточним днем
        days_until_birthday = (birthday_date - today).days

        if 0 <= days_until_birthday <= 7:
            # Перевірка, чи день народження припадає на вихідний
            if birthday_date.weekday() >= 5:
                # Якщо припадає на вихідний, переносимо на наступний понеділок
                birthday_date += timedelta(days=(7 - birthday_date.weekday()))

            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': birthday_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

# Приклад використання
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
