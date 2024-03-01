from collections import defaultdict

from datetime import datetime


def get_birthdays_per_week(users):
    # Готуємо defaultdict(list) для зберігання результатів
    result = defaultdict(list)

    # Отримуємо поточну дату системи для подальшого порівняння з датами народження користувачів
    today = datetime.today().date()

    # Проходимо по списку користувачів та аналізуємо їх дати народження
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()  # Конвертуємо до типу date
        try:
            birthday_this_year = birthday.replace(year=today.year)
        except ValueError:
            if birthday.month == 2 and birthday.day == 29:
                    birthday_this_year = birthday.replace(year=today.year, day=28)
        
        # Перевіряємо, чи вже минув день народження цього року
        if birthday_this_year < today:
            try:
                birthday_this_year = birthday.replace(year=(today.year + 1))
            except ValueError:
                if birthday.month == 2 and birthday.day == 29:
                    birthday_this_year = birthday.replace(year=(today.year + 1), day=28)

        # Визначаємо різницю між днем народження та поточним днем, щоб знайти дні народження на тиждень вперед
        delta_days = (birthday_this_year - today).days

        # Якщо ДН протягом тижня, визначаємо день тижня дня народження (якщо це вихідний, переносимо на понеділок)
        if delta_days < 7:
            week_day = get_weekday(birthday_this_year)

            # та додаємо в defaultdict
            result[week_day].append(name)
        
    sorted_result_keys = sorted(result.keys(), key=sort_by_weekday)

    # Виводимо результати з іменами людей, у яких день народження у найближчі 7 днів
    for key in sorted_result_keys:
        names = ', '.join(result[key])
        print(f"{key}: {names}")
    
    return result

# Сортуємо ключі defaultdict згідно послідовності днів у тижні (без вихідних, бо вони не використовуються)
def sort_by_weekday(day):
    week_days_order = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4
    }
    return week_days_order[day]

def get_weekday(birthday_this_year):
    if birthday_this_year.weekday() in [5, 6]:  # Субота або неділя
        return "Monday"
    return birthday_this_year.strftime('%A')